from django.db import models

from pii_mask.pii_field import PiiField


class Person(models.Model):
    name = PiiField(max_length=200)
    fav_colour = models.CharField(max_length=200)
