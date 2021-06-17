from django.db import models

# Create your models here.
class timetable(models.Model):
    email = models.EmailField()
    raw_data = models.TextField()