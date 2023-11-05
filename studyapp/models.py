from django.db import models


# Create your models here.
class Assignment(models.Model):
    title: models.CharField(max_length=50)
    course: models.CharField(max_length=100)
    description: models.CharField(max_length=255)
    dueDate: models.DateTimeField()

    def __str__(self):
        return self.title
