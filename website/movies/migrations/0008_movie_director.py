# Generated by Django 2.2.6 on 2019-11-04 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_remove_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]