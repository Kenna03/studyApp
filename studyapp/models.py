from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Assignment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    course = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title

    @property
    def due_now(self):
        return (self.dueDate <= timezone.now() + timezone.timedelta(days=1)) and (self.dueDate >= timezone.now())
