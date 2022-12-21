import uuid
from django.db import models

# Create your models here.
from geoip.models import Combo
from django_celery_beat.models import PeriodicTask

class Setup(PeriodicTask):
    combo = models.OneToOneField(Combo, on_delete=models.CASCADE, default="")
