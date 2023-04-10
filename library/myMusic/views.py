from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (
  UserSerializer, 
  GroupSerializer, 
  ArtistSerializer, 
  AlbumSerializer, 
  GenreSerializer, 
  SongSerializer
  )
from .models import Artist, Album, Genre, Song

class UserViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows users to be viewed or edited."""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class GroupViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows groups to be viewed or edited. """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny] 


class ArtistViewSet(viewsets.ModelViewSet):
  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
  queryset = Album.objects.all()
  serializer_class = AlbumSerializer


class GenreViewSet(viewsets.ModelViewSet):
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer

class SongViewSet(viewsets.ModelViewSet):
  queryset = Song.objects.all()
  serializer_class = SongSerializer

























# from django.shortcuts import render
# from django.http import HttpResponse
# import datetime
# from .models import *


# def all_artists(request):
#   all_artists = Artist.objects.all(artist_name)
#   return HttpResponse('<h1>Artist: %s </h1>' % all_artists.name)

# def songs_by_genre(request, genre_id):
#   songs_by_genre = Song.objects.filter(genre__id = genre_name)
#   print(songs)
#   for song in songs:
#     print(song.name)
#   return HttpResponse('<h1>Genre: %s </h1>' % songs_by_genre.name)  

# def what_info(request):

