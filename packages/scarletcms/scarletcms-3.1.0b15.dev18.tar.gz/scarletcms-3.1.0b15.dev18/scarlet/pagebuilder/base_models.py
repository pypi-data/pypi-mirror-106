from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils import timezone
from django.core.validators import RegexValidator

from scarlet.assets.fields import AssetsFileField
from scarlet.assets.models import Asset
from scarlet.cms.fields import HTMLTextField, OrderField
from scarlet.versioning.models import Cloneable

from . import settings

validate_slug = RegexValidator(
    r"^[-a-zA-Z0-9_/]+\Z",
    "Only letters, numbers, underscores, hyphens and forward slashes",
    "invalid",
)


class BasePage(models.Model):
    """
    Page fields contain metadata and SEO elements for the page.
    """

    title = models.CharField(max_length=255)
    internal_name = models.CharField(
        max_length=255, blank=True, null=True, help_text="For internal use only."
    )
    slug = models.CharField(
        max_length=255,
        help_text="- For Homepage use slug `index`.</br>- Slugs may include / to make pages appear nested (ie. blog/articles) ",
        validators=[validate_slug],
    )
    seo_description = models.CharField(max_length=500, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    og_image = AssetsFileField(
        type=Asset.IMAGE, blank=True, null=True, verbose_name="Open Graph Image"
    )

    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return self.internal_name if self.internal_name else self.title

    @property
    def kind(self) -> str:
        return "page"

    @property
    def site_name(self):
        raise NotImplementedError

    @property
    def status(self):
        if self.is_published:
            return "Published"
        else:
            return "Unpublished"

    def get_absolute_url(self):
        try:
            url = reverse("page-detail", kwargs={"slug": self.slug})
        except NoReverseMatch:
            url = None
        return url

    class Meta:
        abstract = True


class AbstractSupportingModule(models.Model):
    truncate_at = 100
    order = OrderField()
    styles = None
    behaviors = None
    internal_name = models.CharField(max_length=255, blank=True, null=True)
    style = models.CharField(
        max_length=255, blank=True, null=True, choices=(), editable=False
    )
    behavior = models.CharField(
        max_length=255, blank=True, null=True, choices=(), editable=False
    )

    def __init__(self, *args, **kwargs):
        if hasattr(self, "styles") and self.styles:
            self._meta.get_field("style").editable = True
            self._meta.get_field("style").choices = self.styles

        if hasattr(self, "behaviors") and self.behaviors:
            self._meta.get_field("behavior").editable = True
            self._meta.get_field("behavior").choices = self.behaviors

        super().__init__(*args, **kwargs)

    @property
    def kind(self) -> str:
        raise NotImplementedError

    def _truncate_for_display(self, str: str) -> str:
        response = str
        if len(str) > self.truncate_at:
            response = f"{str[:self.truncate_at]}…"
        return response

    @property
    def display_name(self) -> str:
        display_name = "No Display Name Set"
        if self.internal_name:
            display_name = self.internal_name
        elif hasattr(self, "title"):
            display_name = self.title
        return display_name

    def __str__(self) -> str:
        return f"{self.display_name} ({self.kind} Module)"

    class Meta:
        abstract = True


class BaseHeroModule(AbstractSupportingModule):
    image = AssetsFileField(
        type=Asset.IMAGE,
        required_tags=("hero",),
        image_sizes=settings.WIDE_IMAGE_SIZES,
        blank=True,
        null=True,
    )
    header = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Header Text"
    )
    subheader = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Subheader Text"
    )
    button_url = models.URLField(blank=True, null=True)
    button_text = models.CharField(max_length=100, blank=True, null=True)

    @property
    def kind(self) -> str:
        return settings.HERO_MODULE

    class Meta:
        abstract = True


class BaseTwoColumnModule(AbstractSupportingModule):
    left_image = AssetsFileField(
        type=Asset.IMAGE,
        required_tags=("two column",),
        image_sizes=settings.SQUARE_IMAGE_SIZES,
        blank=True,
        null=True,
    )
    left_header = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Header Text"
    )
    left_description = HTMLTextField(blank=True, null=True, config="useMinimal")
    left_button_url = models.URLField(blank=True, null=True)
    left_button_text = models.CharField(max_length=100, blank=True, null=True)
    right_image = AssetsFileField(
        type=Asset.IMAGE,
        required_tags=("two column",),
        image_sizes=settings.SQUARE_IMAGE_SIZES,
        blank=True,
        null=True,
    )
    right_header = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Header Text"
    )
    right_description = HTMLTextField(blank=True, null=True, config="useMinimal")
    right_button_url = models.URLField(blank=True, null=True)
    right_button_text = models.CharField(max_length=100, blank=True, null=True)

    @property
    def kind(self) -> str:
        return settings.TWO_COLUMN_MODULE

    class Meta:
        abstract = True


class BaseIconListModule(AbstractSupportingModule):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    footnote = models.CharField(max_length=255, blank=True, null=True)

    @property
    def kind(self) -> str:
        return settings.ICON_LIST_MODULE

    class Meta:
        abstract = True


class BaseIconListItem(models.Model):
    icon = AssetsFileField(type=Asset.SVG_IMAGE)
    text = HTMLTextField(blank=True, null=True, config="useMinimal")
    order = OrderField(default=0)

    @property
    def kind(self) -> str:
        return settings.ICON_LIST_ITEM

    class Meta:
        abstract = True


class BaseHeaderModule(AbstractSupportingModule):
    header = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Header Text"
    )
    subheader = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Subheader Text"
    )

    @property
    def kind(self) -> str:
        return settings.HEADER_MODULE

    class Meta:
        abstract = True


class BaseFAQModule(AbstractSupportingModule):
    @property
    def kind(self) -> str:
        return settings.FAQ_MODULE

    class Meta:
        abstract = True


class BaseFAQItem(AbstractSupportingModule):
    question = models.CharField(max_length=255)
    answer = HTMLTextField(config="useMinimal")

    @property
    def kind(self) -> str:
        return settings.FAQ_ITEM

    class Meta:
        abstract = True


class BaseLocationModule(AbstractSupportingModule):
    @property
    def kind(self) -> str:
        return settings.LOCATION_MODULE

    class Meta:
        abstract = True


class BaseLocationItem(AbstractSupportingModule):
    title = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255, help_text="Street address, P.O. Box")
    address2 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Apartment, suite, unit, building, floor, etc",
    )
    city = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(
        max_length=255, verbose_name="State/Province/Region", blank=True, null=True
    )
    zip_code = models.CharField(
        max_length=10, verbose_name="Zip/Postal Code", blank=True, null=True
    )
    country = models.CharField(max_length=100, blank=True, null=True)
    hours = HTMLTextField(config="useMinimal", blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    @property
    def kind(self) -> str:
        return settings.LOCATION_ITEM

    class Meta:
        abstract = True


class BaseImageGalleryModule(AbstractSupportingModule):
    @property
    def kind(self) -> str:
        return settings.GALLERY_MODULE

    class Meta:
        abstract = True


class BaseGalleryImage(AbstractSupportingModule):
    image = AssetsFileField(
        type=Asset.IMAGE,
        required_tags=("gallery image",),
        image_sizes=settings.GALLERY_IMAGE_SIZES,
        blank=True,
        null=True,
    )

    @property
    def kind(self) -> str:
        return settings.GALLERY_ITEM

    class Meta:
        abstract = True


class BaseCarouselModule(AbstractSupportingModule):
    button_url = models.URLField(blank=True, null=True)
    button_text = models.CharField(max_length=100, blank=True, null=True)

    @property
    def kind(self) -> str:
        return settings.CAROUSEL_MODULE

    class Meta:
        abstract = True


class BaseCarouselItem(AbstractSupportingModule):
    """
    Abstract class for carousel items that make up a carousel module.

    Implemented CarouselItems should add a ForeignKey field to their
    module with blank=True, and null=True to allow CMS front end to
    properly save incremental progress for admins.
    """

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    image = AssetsFileField(
        type=Asset.IMAGE,
        required_tags=("carousel image",),
        image_sizes=settings.CAROUSEL_IMAGE_SIZES,
        blank=True,
        null=True,
    )
    button_url = models.URLField(blank=True, null=True)
    button_text = models.CharField(max_length=100, blank=True, null=True)

    @property
    def kind(self) -> str:
        return settings.CAROUSEL_ITEM

    class Meta:
        abstract = True
