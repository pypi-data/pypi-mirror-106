from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from scarlet.disclosures import get_glossary_term_model
from scarlet.disclosures.openapi import DisclosureSchema


class GlossarySerializer(serializers.ModelSerializer):
    disclosure = serializers.SerializerMethodField()

    @extend_schema_field(DisclosureSchema)
    def get_disclosure(self, queryset):
        resp = {}
        for obj in queryset:
            resp[obj.id] = []
            for disclosure in obj.glossarydisclosures.all():
                resp[obj.id].append(
                    {"title": disclosure.title, "body": disclosure.body}
                )
        return resp

    class Meta:
        model = get_glossary_term_model()
        fields = ("id", "disclosure")
