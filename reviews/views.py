from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.models import Movie
from movies.serializers import MovieSerializer
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from users.models import User
from users.permissions import (
    CreateMoviePermissions,
    CreateReviewPermissions,
    GetUserPermissions,
)
from django.shortcuts import get_object_or_404
import ipdb
from rest_framework.authentication import TokenAuthentication


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CreateReviewPermissions]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        # ipdb.set_trace()
        user = get_object_or_404(User, id=self.request.user.pk)
        movie = get_object_or_404(Movie, id=self.kwargs["movie_id"])
        # self.check_object_permissions(self.request.user, user)
        serializer.save(movie_id=movie, user_id=user.id)

    def get_queryset(self):
        movie = get_object_or_404(Movie, id=self.kwargs["movie_id"])
        # ipdb.set_trace()
        return self.queryset.filter(movie_id=movie.id)
