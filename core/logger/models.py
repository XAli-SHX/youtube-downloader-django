from django.db import models
from enum import Enum


class Logger(models.Model):
    class Status(Enum):
        SUCCESS = 'success'
        ERROR = 'error'

    name = models.CharField(max_length=255)
    path = models.TextField()
    link = models.TextField()
    status = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
