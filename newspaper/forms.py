from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from newspaper.models import Redactor, Newspaper, Topic


class CreateRedactorForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )


class CreateNewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Newspaper
        fields = (
            "title",
            "topic",
            "publishers",
            "content",
        )


class RedactorSearchForm(forms.Form):
    name_user = forms.CharField(
        max_length=50,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username..."}
        )
    )


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=50,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by title..."}
        )
    )
