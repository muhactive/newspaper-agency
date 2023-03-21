from django.test import TestCase

from newspaper.forms import CreateRedactorForm


class FormsTest(TestCase):

    def setUp(self) -> None:
        self.form_data = {
            "username": "Pol",
            "password1": "123456789qqq",
            "password2": "123456789qqq",
            "first_name": "Gim",
            "last_name": "Vikrom",
            "email": "ddd@gog.com",
            "years_of_experience": 1
        }
        self.form = CreateRedactorForm(self.form_data)

    def test_redactor_creation_form(self) -> None:
        """TEst check that the fields in the form have been correctly
         added such us: username, first_name, last_name, email,
         years_of_experience"""

        self.assertTrue(self.form.is_valid())
