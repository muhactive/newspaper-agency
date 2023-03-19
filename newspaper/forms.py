from django import forms
from django.contrib.auth.forms import UserCreationForm

from newspaper.models import Redactor


class CreateRedactorForm(UserCreationForm):
    class Meta:
        model = Redactor
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )

