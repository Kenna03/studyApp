from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Assignment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='test')
    title = models.CharField(max_length=50, default='SOME STRING')
    course = models.CharField(max_length=100, default='SOME STRING')
    description = models.CharField(max_length=255, default='SOME STRING')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
