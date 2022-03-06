from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify
from category.models import Category


class Post(models.Model):
    POST_STATUS_CHOICES = (
        ("P", "Pending for Approval"),
        ("R", "Rejected"),
        ("A", "Approved"),
        ("B", "Blocked"),
    )
    title = models.CharField(
        "Post Title",
        max_length=250,
        error_messages={"max_length": "You can't add more than 250 characters"},
    )
    body = models.TextField("Post Description", max_length=5000)
    slug = models.SlugField(
        max_length=300, unique=True, null=True, blank=True, editable=False
    )
    status = models.CharField(max_length=1, choices=POST_STATUS_CHOICES, default="P")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Post Author"
    )
    category = models.ManyToManyField(Category, blank=True)
    published_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Post"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        def unique_code():
            return str(datetime.datetime.now().timestamp() * pow(10, 6))

        if not self.slug:
            self.slug = slugify(self.title + unique_code())
        return super().save(*args, **kwargs)
