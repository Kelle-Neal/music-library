from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import (
  Artist,
  Album,
  Genre,
  Song,
  # Playlist,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ArtistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artist
    fields = ['id', 'name']

class AlbumSerializer(serializers.ModelSerializer):
  class Meta:
    model = Album
    fields = ['id', 'name']


class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genre
    fields = ['id', 'name']

class SongSerializer(serializers.ModelSerializer):    
  artist = ArtistSerializer
  album = AlbumSerializer
  genre = GenreSerializer
  class Meta:
    model = Song
    fields = [
      'name',
      'artist',
      'album',
      'genre',
    ]