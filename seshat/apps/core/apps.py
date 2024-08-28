from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "seshat.apps.core"

    def ready(self):
        import seshat.apps.core.signals  # TODO: Is this import needed here?
