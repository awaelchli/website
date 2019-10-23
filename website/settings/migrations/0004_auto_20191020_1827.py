# Generated by Django 2.2.6 on 2019-10-20 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='num_posts_per_page',
            field=models.PositiveIntegerField(default=5, help_text='The number of blog posts that appear in one page. ', verbose_name='Posts per page'),
        ),
    ]