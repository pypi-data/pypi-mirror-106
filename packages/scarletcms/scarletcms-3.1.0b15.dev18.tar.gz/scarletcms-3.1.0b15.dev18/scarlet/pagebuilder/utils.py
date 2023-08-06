import warnings

from scarlet.utils.assets import get_image_urls as new_get_image_urls


def get_image_urls(obj, field, sizes=None):
    warnings.warn("get_image_urls has been moved to scarlet.utils.assets "
                  "and will be removed from this module in a future version.",
                  category=DeprecationWarning, stacklevel=2)
    return new_get_image_urls(obj, field, sizes)
