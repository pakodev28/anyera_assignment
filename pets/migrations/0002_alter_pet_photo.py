# Generated by Django 4.2.1 on 2023-07-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="photo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="pet_photos/",
                verbose_name="Фото питомца",
            ),
        ),
    ]
