from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
# from .fields import NameListingField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class ArtistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artist
    fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
  class Meta:
    model = Album
    fields = "__all__"



class GenreSerializer(serializers.ModelSerializer):
  # album_list = NameListingField(many=True)
  class Meta:
    model = Genre
    fields = "__all__"


class SongSerializer(serializers.ModelSerializer):    
  artist = ArtistSerializer()
  album = AlbumSerializer()
  genre = GenreSerializer()
  class Meta:
    model = Song
    fields = "__all__"
