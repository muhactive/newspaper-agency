from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="12345admin"
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create(
            username="Dog",
            password="987456321nnn",
            years_of_experience=2
        )

    def test_admin_page_has_years_of_experience(self):
        url = reverse("admin:newspaper_redactor_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.redactor.years_of_experience)

