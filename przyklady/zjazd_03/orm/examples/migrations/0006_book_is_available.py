# Generated by Django 5.1.5 on 2025-02-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("examples", "0005_create_book_summary_view"),
    ]

    operations = [
        # First drop the view
        migrations.RunSQL(
            "DROP VIEW IF EXISTS book_summary;",
            reverse_sql="",  # No reverse operation needed
        ),
        # Add the new field
        migrations.AddField(
            model_name="book",
            name="is_available",
            field=models.BooleanField(default=False),
        ),
        # Recreate the view
        migrations.RunSQL(
            """
            CREATE VIEW book_summary AS
            SELECT examples_book.id, examples_book.title, examples_author.name AS author_name, examples_book.price, examples_book.is_available
            FROM examples_book
            JOIN examples_author ON examples_book.author_id = examples_author.id;
            """,
            reverse_sql="DROP VIEW IF EXISTS book_summary;"
        ),
    ]
