from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from genres.models import Genre
from genres.serializers import GenreSerializer
from movies.models import Movie
from movies.serializers import MovieSerializer
from users.permissions import GetUserPermissions
import ipdb


class MovieView(generics.ListCreateAPIView):
    # genres = GenreSerializer
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [GetUserPermissions]

    # def post(self, request, *args, **kwargs):
    #     users = self.queryset
    #     self.check_object_permissions(request, users)
    #     genres_list = request.data["genres"]
    #     # movie = Movie.objects.create(**request.data)
    #     for genre in genres_list:
    #         genre_obj = Genre.objects.get_or_create(**genre)[0]
    #         # return genre_obj
    #     # ipdb.set_trace()
    #     return self.create(request, *args, **kwargs)
