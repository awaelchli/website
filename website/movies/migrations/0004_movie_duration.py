# Generated by Django 2.2.6 on 2019-11-04 00:33

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_auto_20191104_0128"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="duration",
            field=models.DurationField(blank=True, default=datetime.timedelta(0)),
            preserve_default=False,
        ),
    ]
