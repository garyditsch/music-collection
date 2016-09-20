from django.db import models
from datetime import datetime 

# Create your models here.

class Track(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    genres = models.ManyToManyField('Genre')
    artists = models.ManyToManyField('artists.Artist')
    album = models.ManyToManyField('Album')

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    genres = models.ManyToManyField('Genre')
    artists = models.ManyToManyField('artists.Artist')

    def __str__(self):
        return self.title