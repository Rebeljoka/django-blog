from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configuration class for the About app.
    Sets the default auto field and app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
