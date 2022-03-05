from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=24)
    description = models.TextField(max_length=500)
