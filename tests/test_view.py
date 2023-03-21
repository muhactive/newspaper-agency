from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic


class PrivateTopicTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="user",
            password="12345password"
        )
        self.client.force_login(self.user)

    def test_private_presentation_topic_list(self):
        Topic.objects.create(topic="UPG")
        topic = Topic.objects.all()
        response = self.client.get(reverse("newspaper:topic-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["topic_list"]),
            list(topic)
        )