# Generated by Django 4.2.7 on 2023-11-05 18:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("studyapp", "0002_assignment_completed"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="assignment",
            name="completed",
        ),
    ]
