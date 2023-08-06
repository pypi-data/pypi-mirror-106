from types import ModuleType

from django.apps import apps as djapps
from django.core.exceptions import ImproperlyConfigured


def get_model_from_setting(settings: ModuleType, setting_name: str):
    """
    Get the model from a settings in the provided settings module.
    :param settings: A settings module containing the setting.
    :param setting_name: The name of the settings (e.g. "PAGE_MODEL")
    :return: The model class
    """

    try:
        app_label, model_name = getattr(settings, setting_name).rsplit(".", 1)
    except ValueError:
        raise ImproperlyConfigured(
            f"{setting_name} must be of the form 'app_label.model_name'"
        )

    return djapps.get_model(app_label, model_name)
