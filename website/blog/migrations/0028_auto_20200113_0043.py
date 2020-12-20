# Generated by Django 2.2.6 on 2020-01-12 23:43

import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations

import streams.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20200112_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content',
            field=wagtail.core.fields.StreamField([('richtext', streams.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.TextBlock(required=False))])), ('code', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.TextBlock(required=False)), ('prefix', wagtail.core.blocks.ChoiceBlock(choices=[('line-numbers', 'Line Numbers'), ('prompt', 'Command Line Prompt')])), ('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash + Shell'), ('batch', 'Batch'), ('c', 'C'), ('cpp', 'C++'), ('css', 'CSS'), ('django', 'Django/Jinja2'), ('git', 'Git'), ('java', 'Java'), ('html', 'HTML'), ('javascript', 'JavaScript'), ('json', 'JSON'), ('latex', 'LaTeX'), ('makefile', 'Makefile'), ('markdown', 'Markdown'), ('matlab', 'MATLAB'), ('python', 'Python'), ('regex', 'Regex'), ('sql', 'SQL'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))])), ('HTML', wagtail.core.blocks.RawHTMLBlock(icon='fa-html5')), ('Terminal', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.StreamBlock([('line', wagtail.core.blocks.StructBlock([('prompt', wagtail.core.blocks.CharBlock(default='>', required=False)), ('line', wagtail.core.blocks.CharBlock(required=False))])), ('multiline', wagtail.core.blocks.StructBlock([('lines', wagtail.core.blocks.TextBlock(required=False))]))], required=True))])), ('latex', wagtail.core.blocks.StructBlock([('equation', wagtail.core.blocks.TextBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[(100, '100%'), (150, '150%'), (200, '200%'), (250, '250%')])), ('caption', wagtail.core.blocks.TextBlock(required=False))])), ('blockquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(required=True)), ('source', wagtail.core.blocks.TextBlock(required=False))])), ('youtube', wagtail.core.blocks.StructBlock([('video_id', wagtail.core.blocks.RegexBlock(label='Video ID', max_length=11, min_length=11, regex='^[a-zA-Z0-9_-]{11}$', required=True)), ('aspect_ratio', wagtail.core.blocks.ChoiceBlock(choices=[('1by1', '1:1'), ('4by3', '4:3'), ('16by9', '16:9'), ('21by9', '21:9')], label='Aspect Ratio'))]))], blank=True),
        ),
    ]
