from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    movie_id = serializers.SerializerMethodField()
    critic = serializers.SerializerMethodField()

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

    def get_movie_id(self, obj: Review):
        return obj.movie.pk

    def get_critic(self, obj: Review):
        critic = {
            "id": obj.critic.pk,
            "first_name": obj.critic.first_name,
            "last_name": obj.critic.last_name,
        }
        return critic
