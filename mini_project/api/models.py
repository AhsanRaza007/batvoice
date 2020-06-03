from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Transcript(models.Model):
    transcription= models.CharField(max_length=500,null=True,blank=True, default=None)
    audio = models.FilePathField(path='./media')
    transcribed = models.BooleanField(default=False)
    user = models.CharField(max_length=150, null=True,blank=True, default=None)



class Charset(models.Model):
    charset = models.CharField(max_length=500)
