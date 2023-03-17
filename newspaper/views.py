from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import CreateRedactorForm
from newspaper.models import Topic, Redactor, Newspaper


@login_required
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
        "num_visit": num_visit
    }

    return render(request, "newspaper/index.html", context=context)


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 5
    template_name = "newspaper/redactor_list.html"
    context_object_name = "redactor_list"


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    template_name = "newspaper/redactor_detail.html"
    context_object_name = "redactor_detail"


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = CreateRedactorForm
    success_url = reverse_lazy("newspaper:redactor-list")
    template_name = "newspaper/redactor_form.html"


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    paginate_by = 5
    template_name = "newspaper/topic_list.html"
    context_object_name = "topic_list"


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    template_name = "newspaper/topic_form.html"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    models = Topic
    template_name = "newspaper/topic_delete.html"
    success_url = reverse_lazy("newspaper:topic-list")
    queryset = Topic.objects.select_related("newspaper")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    template_name = "newspaper/topic_form.html"
    success_url = reverse_lazy("newspaper:topic-list")


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 5
    template_name = "newspaper/newspaper_list.html"
    context_object_name = "newspaper_list"
    queryset = Newspaper.objects.select_related("topic")


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    template_name = "newspaper/newspaper_detail.html"
    context_object_name = "newspaper_detail"


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    fields = "__all__"
    template_name = "newspaper/newspaper_form.html"
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    template_name = "newspaper/newspaper_form.html"
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    template_name = "newspaper/newspaper_delete.html"
    success_url = reverse_lazy("newspaper:newspaper-list")
    queryset = Newspaper.objects.select_related("topic")
