from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from newspaper.models import Redactor, Topic, Newspaper


class TestModel(TestCase):

    def test_redactor_str(self) -> None:
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

    def test_redactor_has_years_of_experience(self) -> None:
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

    def test_newspaper_str(self) -> None:
        self.user = Redactor.objects.create_user(
            username="test_name",
            password="12345testpassword"
        )
        self.topic = Topic.objects.create(topic="topic_test")
        publishers = [self.user]
        newspaper = Newspaper.objects.create(
            title="www",
            content="test content",
            published_date=timezone.now,
            topic=self.topic,
        )
        newspaper.publishers.set(publishers)
        self.assertEqual(
            str(newspaper),
            f"{newspaper.publishers} wrote {newspaper.title} on"
            f" ({newspaper.published_date.strftime('%d-%m-%Y %H:%M:%S')})"
        )
