from django.urls import path

from newspaper.views import (
    index,
    RedactorListView,
    TopicListView,
    NewspaperListView,
    RedactorDetailView,
    NewspaperDetailView,
    TopicCreateView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list"
    ),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list"
    ),
    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspaper-list"
    ),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
    path(
        "newspapers/<int:pk>",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topic-create"
    )
]

app_name = "newspaper"
