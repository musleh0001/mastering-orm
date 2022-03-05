from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=5000)
