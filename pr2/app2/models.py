from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os
class Student1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='', null=True, blank=True)
    marksheet = models.FileField(upload_to='', null=True, blank=True)
    
    @property
    def __str__(self) ->str:
       return self.name
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo:
            # Construct the file path within the media directory
            media_photo_path = os.path.join(settings.MEDIA_ROOT, 'students', self.photo.name)
            # Ensure the directory exists
            os.makedirs(os.path.dirname(media_photo_path), exist_ok=True)
            # Write the photo content to the file
            with open(media_photo_path, 'wb+') as f:
                f.write(self.photo.read())

        if self.marksheet:
            # Construct the file path within the media directory
            media_marksheet_path = os.path.join(settings.MEDIA_ROOT, 'students', self.marksheet.name)
            # Ensure the directory exists
            os.makedirs(os.path.dirname(media_marksheet_path), exist_ok=True)
            # Write the marksheet content to the file
            with open(media_marksheet_path, 'wb+') as f:
                f.write(self.marksheet.read())
        