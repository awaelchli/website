# Generated by Django 2.2.6 on 2019-10-26 15:04

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_auto_20191026_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('bannerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.BannerPage')),
            ],
            options={
                'verbose_name': 'Home Page',
            },
            bases=('core.bannerpage',),
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=128)),
                ('number', models.IntegerField()),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='home.HomePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
