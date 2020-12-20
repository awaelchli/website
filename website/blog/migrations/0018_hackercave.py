# Generated by Django 2.2.6 on 2020-01-09 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0017_auto_20200103_0003"),
    ]

    operations = [
        migrations.CreateModel(
            name="HackerCave",
            fields=[
                (
                    "bloglistingpage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="blog.BlogListingPage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Hacker Cave",
            },
            bases=("blog.bloglistingpage",),
        ),
    ]
