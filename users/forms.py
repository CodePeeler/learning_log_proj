from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclude labels from all fields
        for field_name in self.fields:
            self.fields[field_name].label = False

        # Optionally, you can set placeholders for the fields instead of labels
        self.fields['username'].widget.attrs['placeholder'] = _('Username')
        self.fields['password1'].widget.attrs['placeholder'] = _('Password')
        self.fields['password2'].widget.attrs['placeholder'] = _('Confirm Password')
