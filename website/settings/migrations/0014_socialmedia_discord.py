# Generated by Django 2.2.6 on 2020-01-03 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0013_subscription_telegram_invite_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='discord',
            field=models.URLField(blank=True),
        ),
    ]