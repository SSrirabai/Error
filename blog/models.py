# BlogNVlog/blog/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Update the 'updated_on' field before saving
        self.updated_on = timezone.now()
        super().save(*args, **kwargs)

    def display_created_on(self):
        return self.created_on.strftime('%b %d, %Y %I:%M %p')

    def display_updated_on(self):
        return self.updated_on.strftime('%b %d, %Y %I:%M %p')

    def __str__(self):
        return self.title
