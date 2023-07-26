from django.contrib.auth.models import User
from django.db import models


class Pet(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        related_name="pets",
    )
    name = models.CharField(max_length=50, verbose_name="Кличка")
    species = models.CharField(max_length=50, verbose_name="Вид")
    breed = models.CharField(max_length=50, verbose_name="Порода")
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")
    photo = models.ImageField(
        upload_to="pet_photos/",
        verbose_name="Фото питомца",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"
        unique_together = ["owner", "name", "species", "breed", "age"]

    @property
    def human_age(self):
        """Calculate and return the age of the pet in human years."""
        return self.age * 7
