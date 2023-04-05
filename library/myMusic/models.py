from django.db import models

# Create your models here.
class Artist(models.Model):
  name = models.CharField(max_length=300)
  bio = models.TextField(null=True)
  albums = models.ManyToManyField('Album')

  # image = models.URLField(null=True)
  # song = models.ForeignKey(
  #   'Song', 
  #   on_delete=models.PROTECT,
  #   null=True
  # )

class Album(models.Model):
  name = models.CharField(max_length=500)
  # artist = models.ForeignKey(
  #   'Artist', 
  #   on_delete=models.PROTECT,
  #   null=True
  # )

  releaseDate = models.DateField(null=True)
  songs = models.ManyToManyField('Song')
  # artwork = models.URLField(null=True)

class Song(models.Model):
  name = models.CharField(max_length=500)
  genres = models.ManyToManyField('Genre')


class Genre(models.Model):
  """Model representing the genre of a song or album."""
  name = models.CharField(max_length=100)

  # SO WE CAN SEE THE NAMES OF THE GENRES IN THE ADMIN PANEL
  # def __str__(self):
  #   return self.name

