from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        name = Song
        fields = ['title', 'artist', 'album', 'release_date', 'genre']