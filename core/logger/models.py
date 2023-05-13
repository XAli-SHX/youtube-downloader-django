from django.db import models


class Logger(models.Model):
    name = models.CharField(max_length=255)
    path = models.TextField()
    link = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
