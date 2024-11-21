from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.CharField(max_length=500, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # New fields with predefined choices
    COLOR_CHOICES = [
        ('orange', 'Orange'),
        ('white', 'White'),
        ('beige', 'Beige'),
        ('black', 'Black'),
        ('other', 'Other'),
    ]

    SHAPE_CHOICES = [
        ('cylinder', 'Cylinder'),
        ('square', 'Square'),
        ('other', 'Other'),
    ]

    MATERIAL_CHOICES = [
        ('plastic', 'Plastic'),
        ('metal', 'Metal'),
        ('other', 'Other'),
    ]

    WEIGHT_CHOICES = [
        ('0-2.5kg', '0-2.5kg'),
        ('2.5-5kg', '2.5-5kg'),
        ('5-10kg', '5-10kg'),
        ('other', 'Other'),
    ]

    LOCATION_CHOICES = [
        ('europe', 'Europe'),
        ('asia', 'Asia'),
        ('north america', 'North America'),
        ('south america', 'South America'),
        ('africa', 'Africa'),
        ('australia', 'Australia'),
        ('antarctica', 'Antarctica'),
        ('other', 'Other'),
    ]

    HARDNESS_CHOICES = [
        ('soft', 'Soft'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
        ('rigid', 'Rigid'),
        ('other', 'Other'),
    ]

    TIME_PERIOD_CHOICES = [
        ('stone age', 'Stone Age'),
        ('iron age', 'Iron Age'),
        ('classical era', 'Classical Era'),
        ('medieval era', 'Medieval Era'),
        ('early modern era', 'Early Modern Era'),
        ('modern era', 'Modern Era'),
        ('other', 'Other'),
    ]
    
    SMELL_CHOICES = [
        ('woody', 'Woody'),
        ('fragrant', 'Fragrant'),
        ('fruity', 'Fruity'),
        ('minty', 'Minty'),
        ('sweet', 'Sweet'),
        ('popcorn', 'Popcorn'),
        ('lemon', 'Lemon'),
        ('chemical', 'Chemical'),
        ('pungent', 'Pungent'),
        ('decayed', 'Decayed'),
        ('none', 'None'),
        ('other', 'Other'),
    ]

    TASTE_CHOICES = [
        ('sweet', 'Sweet'),
        ('sour', 'Sour'),
        ('bitter', 'Bitter'),
        ('salty', 'Salty'),
        ('umami', 'Umami'),
        ('savory', 'Savory'),
        ('other', 'Other'),
    ]

    TEXTURE_CHOICES = [
        ('smooth', 'Smooth'),
        ('rough', 'Rough'),
        ('grainy', 'Grainy'),
        ('slimy', 'Slimy'),
        ('other', 'Other'),
    ]

    VALUE_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('luxury', 'Luxury'),
        ('other', 'Other'),
    ]

    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='other')
    shape = models.CharField(max_length=20, choices=SHAPE_CHOICES, default='other')
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES, default='other')
    weight = models.CharField(max_length=20, choices=WEIGHT_CHOICES, default='other')
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default='other')
    hardness = models.CharField(max_length=20, choices=HARDNESS_CHOICES, default='other')
    time_period = models.CharField(max_length=20, choices=TIME_PERIOD_CHOICES, default='other')
    smell = models.CharField(max_length=20, choices=SMELL_CHOICES, default='other')
    taste = models.CharField(max_length=20, choices=TASTE_CHOICES, default='other')
    texture = models.CharField(max_length=20, choices=TEXTURE_CHOICES, default='other')
    value = models.CharField(max_length=20, choices=VALUE_CHOICES, default='other')

    def __str__(self):
        return self.title
