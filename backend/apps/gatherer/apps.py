from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GathererConfig(AppConfig):
    name = "apps.gatherer"
    verbose_name = _("gatherer")
