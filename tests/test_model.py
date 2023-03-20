from django.test import TestCase

from newspaper.models import Redactor, Topic


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

    def test_redactor_has_years_of_experience(self):
        username = "Lilu"
        password = "123456789lilu"
        years_of_experience = 2
        redactor = Redactor.objects.create_user(
            username="Lilu",
            password="123456789lilu",
            years_of_experience=2
        )
        self.assertEqual(redactor.username, username)
        self.assertTrue(redactor.check_password(password))
        self.assertEqual(redactor.years_of_experience, years_of_experience)

    def test_topic_str(self) -> None:
        topic = Topic.objects.create(topic="test")
        self.assertEqual(str(topic), f"{topic.topic}")

