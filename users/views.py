from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView
from users.permissions import GetUserPermissions
from .models import User
from .serializers import UserSerializer


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [GetUserPermissions]

    queryset = User.objects.all()
    serializer_class = UserSerializer
