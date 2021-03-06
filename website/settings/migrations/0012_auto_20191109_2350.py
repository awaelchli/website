# Generated by Django 2.2.6 on 2019-11-09 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0011_auto_20191109_0016"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="telegram_bot_token",
            field=models.CharField(
                blank=True, max_length=128, verbose_name="Bot API Key"
            ),
        ),
        migrations.AddField(
            model_name="subscription",
            name="telegram_channel_id",
            field=models.CharField(
                blank=True, max_length=128, verbose_name="Channel ID"
            ),
        ),
    ]
