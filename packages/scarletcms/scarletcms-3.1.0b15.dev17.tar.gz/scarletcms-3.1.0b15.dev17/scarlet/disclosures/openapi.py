from rest_framework import serializers


class DisclosureItemSchema(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()


class DisclosureSchema(serializers.Serializer):
    disclosure = DisclosureItemSchema()
