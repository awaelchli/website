# Generated by Django 2.2.6 on 2019-11-03 19:07

import django.core.validators
from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blogdetailpage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content',
            field=wagtail.core.fields.StreamField([('richtext', streams.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.TextBlock(required=False))])), ('code', wagtail.core.blocks.StreamBlock([('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash + Shell'), ('batch', 'Batch'), ('c', 'C'), ('cpp', 'C++'), ('css', 'CSS'), ('django', 'Django/Jinja2'), ('git', 'Git'), ('java', 'Java'), ('javascript', 'JavaScript'), ('json', 'JSON'), ('latex', 'LaTeX'), ('makefile', 'Makefile'), ('markdown', 'Markdown'), ('matlab', 'MATLAB'), ('python', 'Python'), ('regex', 'Regex'), ('sql', 'SQL'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code')), ('caption', wagtail.core.blocks.TextBlock(required=False))])), ('HTML', wagtail.core.blocks.RawHTMLBlock()), ('latex', wagtail.core.blocks.StructBlock([('equation', wagtail.core.blocks.TextBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[(100, '100%'), (150, '150%'), (200, '200%'), (250, '250%')])), ('caption', wagtail.core.blocks.TextBlock(required=False))])), ('blockquote', wagtail.core.blocks.BlockQuoteBlock()), ('youtube', wagtail.core.blocks.StructBlock([('video_id', wagtail.core.blocks.CharBlock(required=True, validators=[django.core.validators.RegexValidator(message='Enter a valid YouTube video ID.', regex='[a-zA-Z0-9_-]{11}')]))]))], blank=True),
        ),
    ]
