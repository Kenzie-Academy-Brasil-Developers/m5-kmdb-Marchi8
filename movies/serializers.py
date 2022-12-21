from rest_framework import serializers
from genres.models import Genre
from genres.serializers import GenreSerializer
from movies.models import Movie
import ipdb


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "budget",
            "overview",
            "genres",
        ]

    def create(self, validated_data):
        genres_list = validated_data.pop("genres")
        movie = Movie.objects.create(**validated_data)
        for genre in genres_list:
            genre_obj = Genre.objects.get_or_create(**genre)[0]
            movie.genres.add(genre_obj)
        return movie
