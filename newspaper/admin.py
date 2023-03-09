from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from newspaper.models import Topic, Newspaper, Redactor


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    search_fields = ["title"]


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ["title", "published_date", "topic", "username_publishers"]
    search_fields = ["title"]
    list_filter = ["title", "publishers"]

    def username_publishers(self, obj):
        return ", ".join([publisher.username for publisher in obj.publishers.all()])


@admin.register(Redactor)
class RedactorArmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {
            "fields": ("first_name", "last_name", "years_of_experience",)
        }),
    )
    list_filter = ["username", "last_name"]
    search_fields = ["username", "last_name", "first_name"]
