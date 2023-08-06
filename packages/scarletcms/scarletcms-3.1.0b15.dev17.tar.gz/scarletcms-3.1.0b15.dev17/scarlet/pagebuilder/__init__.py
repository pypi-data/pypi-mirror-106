from . import settings
from scarlet.utils.lookups import get_model_from_setting


def get_page_model():
    return get_model_from_setting(settings, "PAGE_MODEL")


def get_hero_model():
    return get_model_from_setting(settings, "HERO_MODULE_MODEL")


def get_header_model():
    return get_model_from_setting(settings, "HEADER_MODULE_MODEL")


def get_two_column_model():
    return get_model_from_setting(settings, "TWO_COLUMN_MODEL")


def get_icon_list_model():
    return get_model_from_setting(settings, "ICON_LIST_MODEL")


def get_icon_item_model():
    return get_model_from_setting(settings, "ICON_LIST_ITEM_MODEL")


def get_faq_model():
    return get_model_from_setting(settings, "FAQ_MODULE_MODEL")


def get_faq_item_model():
    return get_model_from_setting(settings, "FAQ_ITEM_MODEL")


def get_location_model():
    return get_model_from_setting(settings, "LOCATION_MODULE_MODEL")


def get_location_item_model():
    return get_model_from_setting(settings, "LOCATION_ITEM_MODEL")


def get_image_gallery_model():
    return get_model_from_setting(settings, "GALLERY_MODULE_MODEL")


def get_gallery_item_model():
    return get_model_from_setting(settings, "GALLERY_ITEM_MODEL")


def get_carousel_model():
    return get_model_from_setting(settings, "CAROUSEL_MODULE_MODEL")


def get_carousel_item_model():
    return get_model_from_setting(settings, "CAROUSEL_ITEM_MODEL")
