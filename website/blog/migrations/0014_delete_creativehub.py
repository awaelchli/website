# Generated by Django 2.2.6 on 2019-12-30 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        ("wagtailforms", "0003_capitalizeverbose"),
        ("wagtailredirects", "0006_redirect_increase_max_length"),
        ("blog", "0013_creativehub2"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CreativeHub",
        ),
    ]
