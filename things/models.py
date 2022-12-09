from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Model


class Thing(models.Model):
    name = models.CharField(default="", max_length=30, unique=True)
    description = models.CharField(
        default="", max_length=120, unique=False, blank=True)
    quantity = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
