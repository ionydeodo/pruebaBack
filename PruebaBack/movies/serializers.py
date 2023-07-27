from rest_framework import serializers
from .models.movie import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'genre', 'type', 'views', 'score']
