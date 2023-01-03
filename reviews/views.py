from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.models import Movie
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from users.models import User
from users.permissions import CreateReviewPermissions
from django.shortcuts import get_object_or_404


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CreateReviewPermissions]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.user.pk)
        movie = get_object_or_404(Movie, id=self.kwargs["movie_id"])
        serializer.save(movie_id=movie.id, critic=user)

    def get_queryset(self):
        movie = get_object_or_404(Movie, id=self.kwargs["movie_id"])
        return self.queryset.filter(movie_id=movie.id)
