from django.test import TestCase

from newspaper.models import Redactor


class TestModel(TestCase):

    def test_redactor_str(self):
        redactor = Redactor.objects.create_user(
            username="Bob",
            first_name="Luk",
            last_name="Won",
            email="test@test.test"
        )
        self.assertEqual(
            str(redactor),
            f"{redactor.first_name} {redactor.last_name}"
        )
