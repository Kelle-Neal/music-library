from django.db import models

# Create your models here.
class Artist(models.Model):
  name = models.CharField(max_length=300)
  bio = models.TextField(null=True, blank=True)
  image = models.URLField(null=True, blank=True)
  albums = models.ManyToManyField('Album', blank=True)

  def __str__(self):
    return f'{self.name}'

class Album(models.Model):
  name = models.CharField(max_length=500)
  artists= models.ForeignKey('Artist', on_delete=models.PROTECT, null=True, blank=True)
  releaseDate = models.DateField(null=True, blank=True)
  artwork = models.URLField(null=True, blank=True)
  genres = models.ManyToManyField('Genre', blank=True)
  songs = models.ManyToManyField('Song', blank=True)

  def __str__(self):
    return f'{self.name}'

class Song(models.Model):
  name = models.CharField(max_length=500)
  artist = models.ForeignKey(Artist, on_delete=models.PROTECT, null=True, blank=True)
  albumName = models.ForeignKey(Album, on_delete=models.PROTECT, null=True, blank=True)

  def __str__(self):
    return f'{self.name}'

class Genre(models.Model):
  """Model representing the genre of a song or album."""
  name = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return f'{self.name}'  

class Playlist(models.Model):
  name = models.CharField(max_length=150)
  description = models.TextField(null=True, blank=True)
  songs = models.ManyToManyField('Song', blank=True)
  albums = models.ManyToManyField('Album', blank=True)
  artists = models.ManyToManyField('Artist', blank=True)

  def __str__(self):
    return f'{self.name}'











# info_321