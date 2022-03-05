from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=24, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    status = models.CharField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
