# Generated by Django 5.1.4 on 2025-01-18 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0004_book_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="old_author",
        ),
    ]
