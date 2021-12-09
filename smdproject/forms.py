from django import forms

from .models import VaultOwner


class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Your email")
    name = forms.CharField(label="Your name")
    affiliation = forms.CharField(label="Your affiliation")
