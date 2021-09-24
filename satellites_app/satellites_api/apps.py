from django.apps import AppConfig
from satellites_api import setup


class SatellitesApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'satellites_api'
    
    def ready(self):
        setup.setUp()
