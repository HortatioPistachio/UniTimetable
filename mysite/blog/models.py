from django.db import models

# Create your models here.
class timetable(models.Model):
    colors = [
        ("1", "Lavender"), #a4bdfc
        ("2", "Aqua"), #7ae7bf
        ("3", "Grape"), #dbadff
        ("4", "Flamingo"), #ff887c
        ("5", "Honeycomb"), #fbd75b
        ("6", "Tangerine"), #ffb878
        ("7", "Light Blue"), #46d6db
        ("8", "Graphite"), #e1e1e1
        ("9", "Dark Blue"), #5484ed
        ("10", "Basil"), #51b749
        ("11", "Tomato"), #dc2127

    ]
    email = models.EmailField()
    colour = models.CharField(max_length=5, choices=colors, default="Lavender")
    raw_data = models.TextField()

class Project(models.Model):
    name = models.CharField(max_length=100)
    blurb = models.CharField(max_length=500)
    about = models.TextField()
    img1 = models.ImageField()
    img2 = models.ImageField(null=True, blank=True)
    img3 = models.ImageField(null=True, blank=True)
    year = models.IntegerField()