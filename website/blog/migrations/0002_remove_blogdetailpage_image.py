# Generated by Django 2.2.6 on 2019-10-26 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdetailpage',
            name='image',
        ),
    ]
