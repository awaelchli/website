# Generated by Django 2.2.6 on 2019-10-24 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_googleanalytics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googleanalytics',
            name='tracking_id',
            field=models.CharField(max_length=15, verbose_name='Tracking ID'),
        ),
    ]
