from django.db import models
from django.contrib.auth.models import AbstractUser
from embed_video.fields import EmbedVideoField
# Create your models here.

class User(AbstractUser):
    pass

class Nuggets(models.Model):
    video = EmbedVideoField()

class Image(models.Model):
    image = models.ImageField(upload_to = 'alic-pics/')

class Hangout(models.Model):
    video = EmbedVideoField()

class Hiphop(models.Model):
    video = EmbedVideoField()
    
class Afrobeat(models.Model):
    video = EmbedVideoField()

class Reels(models.Model):
    video = EmbedVideoField()

class Amapiano(models.Model):
    video = EmbedVideoField()

class Dancehall(models.Model):
    video = EmbedVideoField()