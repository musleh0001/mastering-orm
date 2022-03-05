from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=5000)
    slug = models.SlugField()
    status = models.CharField()
    published_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
