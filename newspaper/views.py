from django.shortcuts import render
from django.views import generic

from newspaper.models import Topic, Redactor, Newspaper


def index(request):
    count_topic = Topic.objects.count()
    count_redactor = Redactor.objects.count()
    count_newspaper = Newspaper.objects.count()

    num_visit = request.session.get("num_visit", 0)
    request.session["num_visit"] = num_visit + 1

    context = {
        "count_topic": count_topic,
        "count_redactor": count_redactor,
        "count_newspaper": count_newspaper,
        "num_visit": num_visit + 1
    }

    return render(request, "newspaper/index.html", context=context)


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 5
    template_name = "newspaper/redactor_list.html"
    context_object_name = "redactor_list"


class RedactorDetailView(generic.DetailView):
    model = Redactor
    template_name = "newspaper/redactor_detail.html"
    context_object_name = "redactor_detail"


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


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
    template_name = "newspaper/newspaper_detail.html"
    context_object_name = "newspaper_detail"
