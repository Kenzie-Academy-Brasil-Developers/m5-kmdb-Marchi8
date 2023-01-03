from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "bio",
            "is_critic",
            "is_superuser",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "is_superuser",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "validators": [
                    UniqueValidator(queryset=User.objects.all()),
                ],
                "required": True,
            },
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ],
            },
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
