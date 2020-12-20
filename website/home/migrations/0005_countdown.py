# Generated by Django 2.2.6 on 2019-11-10 16:29

import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0004_auto_20191103_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('target', models.DateTimeField()),
                ('stop_at_zero', models.BooleanField(blank=True, default=False)),
                ('teaser_text', wagtail.core.fields.RichTextField(blank=True)),
                ('reveal_text', wagtail.core.fields.RichTextField(blank=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='countdowns', to='home.HomePage')),
                ('reveal_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
