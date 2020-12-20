from crispy_forms.helper import FormHelper
from django import forms

from subscription.models import NewsletterSubscription


class NewsletterSubscriptionForm(forms.ModelForm):

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your email",
                "class": "form-control form-control-lg",
            }
        )
    )

    class Meta:
        model = NewsletterSubscription
        fields = ["email"]

    def __init__(self, *args, **kwargs):
        super(NewsletterSubscriptionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
