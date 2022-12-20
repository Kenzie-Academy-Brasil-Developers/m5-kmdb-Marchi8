from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView
from users.permissions import GetUserPermissions
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [GetUserPermissions]

    # def get_object(self):
    #     obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
    #     self.check_object_permissions(self.request, obj)
    #     return obj

    def get(self, request: Request) -> Response:
        """
        Listagem de usuários
        """
        users = self.queryset
        result_page = self.paginate_queryset(users)
        self.check_object_permissions(request, users)
        serializer = UserSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


# class UserView(APIView, PageNumberPagination):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [GetUserPermissions]

#     def get(self, request: Request) -> Response:
#         """
#         Listagem de usuários
#         """
#         users = User.objects.all()
#         result_page = self.paginate_queryset(users)
#         self.check_object_permissions(request, users)
#         serializer = UserSerializer(result_page, many=True)

#         return self.get_paginated_response(serializer.data)

#     def post(self, request: Request) -> Response:
#         """
#         Registro de usuários
#         """
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         serializer.save()

#         return Response(serializer.data, status.HTTP_201_CREATED)
