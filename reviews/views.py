from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.serializers import MovieSerializer
from reviews.models import Review
from users.permissions import GetUserPermissions


class ReviewView(generics.ListCreateAPIView):
    ...
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [GetUserPermissions]

    # queryset = Review.objects.all()
    # serializer_class = MovieSerializer
