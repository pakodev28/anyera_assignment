import random

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from faker import Faker

from pets.models import Pet

NUM_USERS = 5
NUM_PETS_PER_USER = 3

DOG_BREEDS = ["Labrador", "Golden Retriever", "Bulldog"]
CAT_BREEDS = ["Persian", "Maine Coon", "Sphynx"]
FISH_BREEDS = ["Goldfish", "Guppy", "Nemo"]
BIRD_BREEDS = ["Parrot", "Canary", "Mockingbird"]


class Command(BaseCommand):
    help = "Generate test data for pets"

    def generate_fake_image(self):
        """Generate a fake image using Faker."""
        fake = Faker()
        image = fake.image()
        return ContentFile(image, name="test_image.jpg")

    def create_users_and_pets(self):
        """Create random users and their pets using Faker and random."""
        fake = Faker()

        for _ in range(NUM_USERS):
            username = fake.unique.user_name()
            password = fake.password()

            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(password)
                user.save()
                print(f"Created user: {username}")
            else:
                print(f"User already exists: {username}")

            for _ in range(NUM_PETS_PER_USER):
                name = fake.first_name()
                species = random.choice(["Dog", "Cat", "Fish", "Bird"])
                age = random.randint(1, 15)

                photo = self.generate_fake_image()
                if species == "Dog":
                    breed = random.choice(DOG_BREEDS)
                elif species == "Cat":
                    breed = random.choice(CAT_BREEDS)
                elif species == "Fish":
                    breed = random.choice(FISH_BREEDS)
                else:
                    breed = random.choice(BIRD_BREEDS)

                pet, created = Pet.objects.get_or_create(
                    owner=user,
                    name=name,
                    species=species,
                    breed=breed,
                    age=age,
                    photo=photo,
                )

                if created:
                    print(f"\t\tCreated pet: {pet}")
                else:
                    print(f"\t\tPet already exists: {pet}")

    def handle(self, *args, **options):
        self.create_users_and_pets()
