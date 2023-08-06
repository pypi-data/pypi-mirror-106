import pathlib
import yaml

from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Model

from scarlet.pagebuilder.base_models import BasePage
from scarlet.pagebuilder import get_page_model


class Command(BaseCommand):
    help = "Generate blank pages with modules from YML schema"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            help="Path to file with YAML schema",
            type=pathlib.Path,
        )
        parser.add_argument(
            "--allow-duplicates",
            action="store_true",
            help="Allows to create pages with existing slug",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        Page: BasePage = get_page_model()

        filename = (
            options.get("file") or
            settings.APPS_DIR / "pages/scaffold-schema.yml"
        )
        with open(filename, "r") as f:
            schema = yaml.load(f, Loader=yaml.Loader)

        # Simple validation
        for page_name, data in schema.items():
            keys = data.keys()
            if 'slug' not in keys:
                return self.stdout.write(self.style.ERROR(
                    f"No 'slug' in {page_name}"
                ))

            if not options.get("allow_duplicates"):
                if Page.objects.filter(slug=data["slug"]).exists():
                    return self.stdout.write(self.style.ERROR(
                        f"Page with slug `{data['slug']}` already exists"
                    ))

            for module in data.get("modules", []):
                try:
                    apps.get_model("pages", f"{module}Module")
                except LookupError:
                    return self.stdout.write(self.style.ERROR(
                        f"Invalid module: {module}"
                    ))

        for page_name, data in schema.items():
            modules = data.pop("modules")
            page = get_page_model().objects.create(title=page_name, **data)
            for module in modules:
                model: Model = apps.get_model("pages", f"{module}Module")
                model.objects.create(page=page)

        self.stdout.write(self.style.SUCCESS("Success"))
