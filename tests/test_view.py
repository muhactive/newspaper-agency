from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic, Newspaper


class PublicTopicTaste(TestCase):

    def test_public_presentation_page_topic_list(self):
        response = self.client.get(
            reverse("newspaper:topic-list")
        )
        self.assertNotEqual(response.status_code, 200)


class PublicNewspaperTaste(TestCase):

    def test_public_presentation_page_newspaper_list(self) -> None:
        response = self.client.get(
            reverse("newspaper:newspaper-list")
        )
        self.assertNotEqual(response.status_code, 200)


class PrivateTopicTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="user",
            password="12345password"
        )
        self.client.force_login(self.user)

    def test_private_presentation_topic_list(self) -> None:
        Topic.objects.create(topic="UPG")
        topic = Topic.objects.all()
        response = self.client.get(reverse("newspaper:topic-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["topic_list"]),
            list(topic)
        )
        self.assertTemplateUsed(response, "newspaper/topic_list.html")


class PrivateNewspaperTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="Al",
            password="5454646asdfasd"
        )
        self.client.force_login(self.user)

    def test_private_presentation_newspaper_list(self) -> None:
        topic = Topic.objects.create(topic="Police")
        Newspaper.objects.create(
            topic=topic,
            title="TEstTitle",
            content="testetestetstetetss",
        )

        newspaper = Newspaper.objects.all()
        response = self.client.get(
            reverse("newspaper:newspaper-list")
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(newspaper)
        )


class TestPublicListRedactor(TestCase):

    def test_login_required(self) -> None:
        response = self.client.get(reverse("newspaper:redactor-list"))
        self.assertNotEqual(response.status_code, 200)