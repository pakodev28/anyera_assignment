from django.contrib.auth.models import User
from rest_framework import serializers

from pets.models import Pet

from .fields import Base64ImageField


class UserSerializer(serializers.ModelSerializer):
    """Serializer for Django User model.
    Only the following fields are used: id, username, password.
    Creates a new user with username and password."""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user


class PetSerializer(serializers.ModelSerializer):
    """Serializer for Pet model.
    photo - pet's image in Base64 format
    human_age - pet's age in human years (property method from Pet Model)."""

    photo = Base64ImageField(required=False)
    human_age = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Pet
        fields = "__all__"


class UserPetsSerializer(serializers.ModelSerializer):
    """Serializer for User with their pets."""

    pets = PetSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "pets"]
