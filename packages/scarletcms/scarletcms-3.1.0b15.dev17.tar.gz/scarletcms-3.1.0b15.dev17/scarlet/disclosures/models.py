import re

from django.db import models
from scarlet.cms.fields import HTMLTextField

from . import settings, get_glossary_term_model


class BaseGlossaryTerm(models.Model):
    _clone_related = ("glossarydisclosures",)

    keyword = models.CharField(
        max_length=255,
        unique=True,
        help_text="The word or short phrase that will appear with a disclosure. Case insensitive.",
    )

    class Meta:
        abstract = True


class BaseGlossaryDisclosure(models.Model):
    term = models.ForeignKey(settings.GLOSSARY_TERM_MODEL,
                             on_delete=models.PROTECT,
                             related_name="glossarydisclosures")
    title = models.CharField(max_length=255)
    body = HTMLTextField(config="useMinimal")

    class Meta:
        abstract = True


class DisclosureMixin:
    """
    Using this mixin allows you to add disclosure markup to any string field on
    a model. The mixin assumes there is a model imported called GlossaryTerm but
    you can change that by overriding the get_glossary_model function. A glossary
    model must have at least an id field, and a keyword field.

    On model:
        Use this mixin, set disclosure_fields to be a list of all field names on the model that should
        get annotated, and add self.add_disclosures() call to save() method.

    For serialization:
        In order to pull the disclosures that go with the marked up text fields call
        get_disclosures_from_fields, this will return a list of Glossary model objects
        for you to serialize.
    """
    disclosure_fields = []

    @staticmethod
    def _span_wrap(matchobj):
        return "<span data-disclosure-id={{term_id}}>{keyword}</span>".format(
            keyword=matchobj.group(0)
        )

    def _get_disclosed_text(self, term, text):
        escaped = re.escape(term.keyword)
        search = re.compile(rf'(?<!<span data-disclosure-id={term.id}>){escaped}',
                            re.IGNORECASE)
        wrapped_str = search.sub(self._span_wrap, text)
        return wrapped_str.format(term_id=term.id)

    def add_disclosures(self):
        for field in self.disclosure_fields:
            value = getattr(self, field, None)
            if value:
                glossary = self.get_glossary()
                for term in glossary:
                    if term.keyword.lower() in value.lower():
                        value = self._get_disclosed_text(term, value)
                setattr(self, field, value)

    def _get_ids_from_text(self, text):
        return set(re.findall(r'(?<=span data-disclosure-id=)\d', text))

    def get_disclosures_from_fields(self):
        term_ids = []
        for field in self.disclosure_fields:
            value = getattr(self, field, None)
            if value:
                term_ids += self._get_ids_from_text(value)
        return self.get_glossary_model().objects.filter(id__in=term_ids)

    def get_glossary_model(self):
        return get_glossary_term_model()

    def get_glossary(self):
        return self.get_glossary_model().objects.all()
