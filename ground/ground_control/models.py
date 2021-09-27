from django.db import models
from django.db.models.deletion import PROTECT
from django.utils import timezone

# Create your models here.
class Satellite(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class Task(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    # assigned_to = models.ForeignKey(Satellite, on_delete=PROTECT)
    assigned_to = models.CharField(max_length=100) #TODO: use foreingKey
    completed = models.BooleanField()

    def __str__(self):
        return self.name
