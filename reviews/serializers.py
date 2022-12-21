from rest_framework import serializers
from movies.models import Movie
from reviews.models import Review
import ipdb
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404


class ReviewSerializer(serializers.ModelSerializer):
    critic = UserSerializer(many=True, required=False)

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "movie_id",
            "critic",
        ]
        # read_only_fields = ["critic"]

    def create(self, validated_data):
        # ipdb.set_trace()
        movie = get_object_or_404(Movie, id=self.request.user.pk)
        return super().create(validated_data)
