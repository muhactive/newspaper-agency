from django import forms

from newspaper.models import Redactor


class CreateRedactorForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )
