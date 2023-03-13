from django.shortcuts import render
from django.views import generic

from newspaper.models import Topic, Redactor, Newspaper


def index(request):
    count_topic = Topic.objects.count()
    count_redactor = Redactor.objects.count()
    count_newspaper = Newspaper.objects.count()

    context = {
        "count_topic": count_topic,
        "count_redactor": count_redactor,
        "count_newspaper": count_newspaper
    }

    return render(request, "newspaper/index.html", context=context)


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 5
    template_name = "newspaper/redactor_list.html"
    context_object_name = "redactor_list"


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 5
    template_name = "newspaper/topic_list.html"
    context_object_name = "topic_list"


class NewspaperListView(generic.ListView):
    model = Newspaper
    paginate_by = 5
    template_name = "newspaper/newspaper_list.html"
    context_object_name = "newspaper_list"
    queryset = Newspaper.objects.select_related("topic")
