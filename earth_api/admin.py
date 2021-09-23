from django.contrib import admin
from earth_api import models

admin.site.register(models.Task)
admin.site.register(models.Satellite)