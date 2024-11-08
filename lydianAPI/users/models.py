from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # image field
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
