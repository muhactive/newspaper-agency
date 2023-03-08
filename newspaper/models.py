from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField()

    class Meta:
        ordering = ["username"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Topic(models.Model):
    topic = models.CharField(max_length=100)

    class Meta:
        ordering = ["topic"]

    def __str__(self) -> str:
        return f"{self.topic}"


class Newspaper(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="newspaper"
    )
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="newspaper"
    )

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return (
            f"{self.publishers} wrote {self.title}"
            f" on ({self.published_date.strftime('%d-%m-%Y %H:%M:%S')})"
        )
