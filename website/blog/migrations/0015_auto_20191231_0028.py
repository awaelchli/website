# Generated by Django 2.2.6 on 2019-12-30 23:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailimages', '0001_squashed_0021'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20191026_1704'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('blog', '0014_delete_creativehub'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreativeHub2',
            new_name='CreativeHub',
        ),
        migrations.AlterModelOptions(
            name='creativehub',
            options={'verbose_name': 'Creative Hub'},
        ),
    ]