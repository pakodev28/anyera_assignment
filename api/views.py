from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets

from pets.models import Pet

from .filters import PetSpeciesFilter
from .serializers import PetSerializer, UserPetsSerializer, UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    """View for user registration. Allows any to create an account."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class PetViewSet(viewsets.ModelViewSet):
    """ViewSet for Pet model.
    Allows authenticated users to perform CRUD operations on their pets.
    Supports filtering by pet species."""

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PetSpeciesFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class UserPetsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for users and their pets.
    Allows authenticated users to view pets of any authenticated user.
    Modifications are not available."""

    queryset = User.objects.all()
    serializer_class = UserPetsSerializer
    permission_classes = [permissions.IsAuthenticated]
