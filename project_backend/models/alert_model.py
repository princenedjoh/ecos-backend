from django.db import models
from project_backend.types import types

class Alert(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    severity = models.CharField(
        max_length=20,
        choices=types.severity
    )
    category = models.CharField(
        max_length=20,
        choices=types.alert_category
    )
    image = models.CharField(max_length=500)