# Generated by Django 2.2.6 on 2019-11-11 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_countdown'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countdown',
            name='stop_at_zero',
        ),
    ]
