from django.db import models

# Create your models here.
class Artist(models.Model):
  name = models.CharField(max_length=300)
  bio = models.TextField(null=True)
  image = models.URLField(null=True)

  def __str__(self):
    return f'{self.name}'

class Album(models.Model):
  name = models.CharField(max_length=500)
  artists= models.ManyToManyField(Artist)
  releaseDate = models.DateField(null=True)
  artwork = models.URLField(null=True)

  def __str__(self):
    return f'{self.name}'

class Song(models.Model):
  name = models.CharField(max_length=500)
  artist = models.ManyToManyField(Artist)
  albumName = models.ForeignKey(Album, on_delete=models.PROTECT, null=True)

  def __str__(self):
    return f'{self.name}'

class Genre(models.Model):
  name = models.CharField(max_length=100)
  albums = models.ManyToManyField(Album)
  
  def __str__(self):
    return f'{self.name}'  

class Playlist(models.Model):
  name = models.CharField(max_length=150)
  description = models.TextField(null=True)
  songs = models.ForeignKey(Song, on_delete=models.PROTECT, null=True, blank=True)
  albums = models.ForeignKey(Album, on_delete=models.PROTECT, null=True, blank=True)
  artists = models.ForeignKey(Artist, on_delete=models.PROTECT, null=True, blank=True)

  def __str__(self):
    return f'{self.name}'











# info_321