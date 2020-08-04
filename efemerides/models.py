from django.db import models

from .managers import CommemorationManager


class Commemoration(models.Model):
    """Commemoration of events by date."""
    date = models.DateField()
    event = models.CharField(max_length=1000, null=False, blank=False)
    objects = CommemorationManager()
