from django import forms
from django.contrib.auth.models import User
from django.conf import settings

class UserLoginForm(forms.Form):
    username = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'name@example.com'}),
        label="Email"
    )

class UserDetailsForm(forms.ModelForm):

    cuisine = forms.MultipleChoiceField(choices=settings.CUISINE_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ("first_name","last_name")