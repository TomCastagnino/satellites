from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField()
    assigned_to = models.CharField(max_length=100) #TODO: use foreingKey
    completed = models.BooleanField()

    def __str__(self):
        return self.name