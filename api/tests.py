from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authentication import TokenAuthentication

from pets.models import Pet
from .serializers import PetSerializer


class UserRegistrationViewTestCase(APITestCase):
    def test_user_registration(self):
        url = reverse("user-registration")
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.data.get("username"), "testuser")


class PetViewSetTestCase(APITestCase):
    authentication_classes = [TokenAuthentication]
    url_list = reverse("pet-list")

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        cls.pet1 = Pet.objects.create(
            owner=cls.user,
            name="Pet 1",
            species="Dog",
            breed="Bulldog",
            age=3,
        )
        cls.pet2 = Pet.objects.create(
            owner=cls.user,
            name="Pet 2",
            species="Cat",
            breed="Siamese",
            age=2,
        )

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def create_pet(self, name, species, breed, age):
        data = {
            "name": name,
            "species": species,
            "breed": breed,
            "age": age,
        }
        return self.client.post(self.url_list, data, format="json")

    def test_list_pets(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pets = Pet.objects.filter(owner=self.user)
        serializer = PetSerializer(pets, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_pet(self):
        response = self.create_pet("New Pet", "Dog", "Golden Retriever", 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pet.objects.filter(owner=self.user).count(), 3)

    def test_retrieve_pet(self):
        url_detail = reverse("pet-detail", kwargs={"pk": self.pet1.id})
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = PetSerializer(self.pet1)
        self.assertEqual(response.data, serializer.data)

    def test_update_pet(self):
        url_detail = reverse("pet-detail", kwargs={"pk": self.pet1.id})
        data = {
            "name": "Updated Pet",
            "species": "Cat",
            "breed": "Siamese",
            "age": 4,
        }
        response = self.client.put(url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pet1.refresh_from_db()
        self.assertEqual(self.pet1.name, "Updated Pet")
        self.assertEqual(self.pet1.species, "Cat")
        self.assertEqual(self.pet1.breed, "Siamese")
        self.assertEqual(self.pet1.age, 4)

    def test_delete_pet(self):
        url_detail = reverse("pet-detail", kwargs={"pk": self.pet1.id})
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Pet.objects.filter(owner=self.user).count(), 1)
