from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers


def get_image_urls(obj, field, sizes=None):
    if sizes is None:
        sizes = {'base': None}

    images = {}
    for size in sizes:
        img_field = f"{field}_urls"
        try:
            images[size] = (
                getattr(obj, img_field).get(size) if getattr(obj, img_field) else None
            )
        except:
            images[size] = ""
    return images


class BaseImageSerializer(serializers.Serializer):
    altText = serializers.CharField()

    def __init__(self, *args, **kwargs):
        """TODO: Figure out a way to get/generate schema from sizes param"""
        self.sizes = kwargs.pop('sizes', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        module = self.parent.instance
        images_json = get_image_urls(module, self.field_name, self.sizes)
        images_json["altText"] = getattr(module, f"{self.field_name}_alt_text", None)
        return images_json


class ImageSerializer(BaseImageSerializer):
    base = serializers.CharField(required=False)
