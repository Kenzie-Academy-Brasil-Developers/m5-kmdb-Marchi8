from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.models import Movie
from movies.serializers import MovieSerializer
from users.models import User
from users.permissions import CreateMoviePermissions
from django.shortcuts import get_object_or_404


class MovieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CreateMoviePermissions]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.user.pk)
        serializer.save(user=user)
