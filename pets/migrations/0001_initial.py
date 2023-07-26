# Generated by Django 4.2.1 on 2023-07-25 00:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Pet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, verbose_name="Кличка"),
                ),
                (
                    "species",
                    models.CharField(max_length=50, verbose_name="Вид"),
                ),
                (
                    "breed",
                    models.CharField(max_length=50, verbose_name="Порода"),
                ),
                (
                    "age",
                    models.PositiveSmallIntegerField(verbose_name="Возраст"),
                ),
                (
                    "photo",
                    models.ImageField(
                        upload_to="pet_photos/", verbose_name="Фото питомца"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Владелец",
                    ),
                ),
            ],
            options={
                "verbose_name": "Питомец",
                "verbose_name_plural": "Питомцы",
                "unique_together": {("owner", "name", "species", "breed", "age")},
            },
        ),
    ]