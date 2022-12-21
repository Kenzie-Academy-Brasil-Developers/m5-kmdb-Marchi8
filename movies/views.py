from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.models import Movie
from movies.serializers import MovieSerializer
from users.models import User
from users.permissions import CreateMoviePermissions
from django.shortcuts import get_object_or_404
import ipdb


class MovieView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [CreateMoviePermissions]

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.user.pk)
        serializer.save(user_id=user.id)
