# Generated by Django 2.2.6 on 2019-11-04 00:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_auto_20191103_2221"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="genre",
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name="movie",
            name="release_date",
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="movie",
            name="trailer",
            field=models.URLField(blank=True),
        ),
    ]
