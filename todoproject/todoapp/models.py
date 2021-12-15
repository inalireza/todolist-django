from django.db import models
from django.db.models.fields import BooleanField

class TodoItem(models.Model):
    work = models.CharField(max_length=100)
    checked = models,BooleanField(default=False)

    def __str__(self):
        return self.work