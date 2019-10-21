from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, InlinePanel, FieldRowPanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.core.fields import RichTextField


class ContactPage(AbstractEmailForm):
    template = 'contact/main.html'

    intro_text = RichTextField(blank=True)
    success_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro_text'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('success_text'),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel('from_address', classname='col-6'),
                        FieldPanel('to_address', classname='col-6'),
                    ]
                ),
                FieldPanel('subject'),
            ],
            heading='Email Settings'
        )
    ]


class FormField(AbstractFormField):
    page = ParentalKey(
        ContactPage,
        on_delete=models.CASCADE,
        related_name='form_fields',
    )



