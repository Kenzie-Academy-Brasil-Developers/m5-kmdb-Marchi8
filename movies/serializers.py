from rest_framework import serializers
from genres.models import Genre
from movies.models import Movie
import ipdb


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "overview",
            "budget",
            "genres",
        ]

    # def create(self, validated_data):
    #     ipdb.set_trace()
    #     genres_list = validated_data.pop("genres")
    #     movie = Movie.objects.create(**validated_data)
    #     for genre in genres_list:
    #         genre_obj = Genre.objects.get_or_create(**genre)[0]
    #         movie.genres.add(genre_obj)
    #     return Movie.objects.create(**validated_data)

    # def perform_create(self, serializer):
    #     print()
    #     ipdb.set_trace()
    #     serializer.save(user=self.request.user)
