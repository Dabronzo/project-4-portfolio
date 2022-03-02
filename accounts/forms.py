from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import NewUserDj


class RegistrationForm(UserCreationForm):
    """Custom Registration Form"""
    email = forms.EmailField(
        max_length=50, help_text="Required a emal to registration"
    )

    class Meta:
        model = NewUserDj
        fields = ("email", "user_name", "password1", "password2")
