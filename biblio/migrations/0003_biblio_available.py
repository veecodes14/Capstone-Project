# Generated by Django 5.2 on 2025-04-10 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0002_biblio_isbn_biblio_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='biblio',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
