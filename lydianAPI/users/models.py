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

    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='other')
    shape = models.CharField(max_length=20, choices=SHAPE_CHOICES, default='other')
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES, default='other')
    weight = models.CharField(max_length=20, choices=WEIGHT_CHOICES, default='other')

    def __str__(self):
        return self.title
