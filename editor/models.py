from django.db import models

# Create your models here.


class Media(models.Model):
    pdf = models.FileField(upload_to="pdfs/")
    audio_files = models.ManyToManyField("AudioFile")


class AudioFile(models.Model):
    audio = models.FileField(upload_to="audios/")
