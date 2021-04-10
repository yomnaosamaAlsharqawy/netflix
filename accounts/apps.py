from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from . import signals
        post_migrate.connect(signals.init_plans, sender=self)
