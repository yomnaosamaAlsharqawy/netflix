from django.apps import AppConfig
from django.db.models.signals import post_migrate


class ResourcesConfig(AppConfig):
    name = 'resources'

    def ready(self):
        from resources import signals
        post_migrate.connect(signals.init_genres, sender=self)
