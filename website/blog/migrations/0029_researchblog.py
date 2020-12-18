# Generated by Django 2.2.17 on 2020-12-18 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20200113_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchBlog',
            fields=[
                ('bloglistingpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.BlogListingPage')),
            ],
            options={
                'verbose_name': 'Research Blog',
            },
            bases=('blog.bloglistingpage',),
        ),
    ]
