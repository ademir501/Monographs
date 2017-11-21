from django.db import models


class Monograph(models.Model):
    number = models.IntegerField(unique=True)
    primary_name = models.CharField(max_length=100, blank=True, null=True)
    secondary_name = models.CharField(max_length=100, blank=True, null=True)
