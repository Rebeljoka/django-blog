from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration class for the Blog app.
    Sets the default auto field and app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
