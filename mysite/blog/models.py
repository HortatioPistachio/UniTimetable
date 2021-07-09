from django.db import models

# Create your models here.
class timetable(models.Model):
    email = models.EmailField()
    raw_data = models.TextField()

class Project(models.Model):
    name = models.CharField(max_length=100)
    blurb = models.CharField(max_length=500)
    about = models.TextField()
    img1 = models.ImageField()
    img2 = models.ImageField(null=True)
    img3 = models.ImageField(null=True)
    year = models.IntegerField()