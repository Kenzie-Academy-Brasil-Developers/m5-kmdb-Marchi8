from rest_framework import serializers

from genres.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
