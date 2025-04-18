# Generated by Django 5.1.4 on 2025-01-19 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gallery",
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
                ("title", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="GalleryImage",
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
                ("image", models.ImageField(upload_to="galleries/%Y/%m/%d/")),
                ("alt", models.CharField(max_length=255)),
                (
                    "gallery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="galleries.gallery",
                    ),
                ),
            ],
        ),
    ]
