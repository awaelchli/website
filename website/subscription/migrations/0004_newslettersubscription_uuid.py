# Generated by Django 2.2.6 on 2019-11-08 21:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0003_newslettersubscription_subscriptionpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslettersubscription',
            name='uuid',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=128),
        ),
    ]
