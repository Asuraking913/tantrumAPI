from django.db import models
from .utils import generate_id


# Create your models here.
class Posts(models.Model):
    id = models.CharField(
        max_length=255, primary_key=True, null=False, blank=False, default=generate_id
    )
    post_email = models.EmailField()
    content = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    id = models.CharField(
        max_length=255, primary_key=True, null=False, blank=False, default=generate_id
    )
    comment_email = models.EmailField()
    content = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)
