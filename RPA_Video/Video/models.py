from django.db import models

# Create your models here.
class Video(models.Model):
    video = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=255) # title of the video extracted from the file name
    size = models.FloatField(default=0.0) # size of file in MB
    length = models.FloatField(default=0.0) # length of video in seconds
    upload_date = models.DateField(auto_now_add=True) # video upload date

    def __str__(self):
        return self.title