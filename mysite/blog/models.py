from django.db import models

# Create your models here.
class timetable(models.Model):
    cal_choices = [
    ('Google', 'Google'),
    ('iCal', 'iCal'),
    ]

    email = models.EmailField()
    raw_data = models.TextField()
    cal_type = models.CharField(max_length=6, choices=cal_choices,default='Google')

class Project(models.Model):
    name = models.CharField(max_length=100)
    blurb = models.CharField(max_length=500)
    about = models.TextField()
    img1 = models.ImageField()
    img2 = models.ImageField(null=True, blank=True)
    img3 = models.ImageField(null=True, blank=True)
    year = models.IntegerField()

class iCal_calendar(models.Model):
    name = models.CharField(max_length=100)
    cal = models.TextField()