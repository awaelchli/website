# Generated by Django 2.2.6 on 2019-11-08 22:00

from django.db import migrations, models

import subscription.utils


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0004_newslettersubscription_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslettersubscription',
            name='uuid',
            field=models.CharField(blank=True, default=subscription.utils.generate_subscriber_uuid, max_length=128),
        ),
    ]
