from scarlet.utils.lookups import get_model_from_setting
from . import settings


def get_glossary_term_model():
    return get_model_from_setting(settings, "GLOSSARY_TERM_MODEL")


def get_glossary_disclosure_model():
    return get_model_from_setting(settings, "GLOSSARY_DISCLOSURE_MODEL")
