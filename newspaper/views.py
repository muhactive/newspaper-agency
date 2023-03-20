from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from newspaper.forms import CreateRedactorForm, CreateNewspaperForm, RedactorSearchForm, NewspaperSearchForm, \
    TopicSearchForm
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

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(RedactorListView, self).get_context_data(**kwargs)
        name_user = self.request.GET.get("name_user", "")
        context["search_form"] = RedactorSearchForm(
            initial={"name_user": name_user}
        )
        return context

    def get_queryset(self) -> QuerySet:
        form = RedactorSearchForm(self.request.GET)
        queryset = super(RedactorListView, self).get_queryset()

        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["name_user"]
            )
        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    template_name = "newspaper/redactor_detail.html"
    context_object_name = "redactor_detail"


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = CreateRedactorForm
    success_url = reverse_lazy("newspaper:redactor-list")
    template_name = "newspaper/redactor_form.html"


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = CreateRedactorForm
    template_name = "newspaper/redactor_form.html"

    def get_success_url(self) -> dict:
        return reverse(
            "newspaper:redactor-detail",
            kwargs={"pk": self.object.pk}
        )


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    template_name = "newspaper/redactor_delete.html"
    success_url = reverse_lazy("newspaper:redactor-list")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    paginate_by = 5
    template_name = "newspaper/topic_list.html"
    context_object_name = "topic_list"

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TopicListView, self).get_context_data(**kwargs)
        name_topic = self.request.GET.get("name_topic", "")
        context["search_form"] = TopicSearchForm(
            initial={"name_topic": name_topic}
        )
        return context

    def get_queryset(self) -> QuerySet:
        form = TopicSearchForm(self.request.GET)
        queryset = super(TopicListView, self).get_queryset()

        if form.is_valid():
            return queryset.filter(
                topic__icontains=form.cleaned_data["name_topic"]
            )
        return queryset


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

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        name_title = self.request.GET.get("name_title", "")
        context["search_form"] = NewspaperSearchForm(
            initial={"name_title": name_title}
        )
        return context

    def get_queryset(self) -> QuerySet:
        form = NewspaperSearchForm(self.request.GET)
        queryset = super(NewspaperListView, self).get_queryset()

        if form.is_valid():
            return queryset.filter(
                title__icontains=form.cleaned_data["name_title"]
            )
        return queryset


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    template_name = "newspaper/newspaper_detail.html"
    context_object_name = "newspaper_detail"


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = CreateNewspaperForm
    template_name = "newspaper/newspaper_form.html"
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = CreateNewspaperForm
    template_name = "newspaper/newspaper_form.html"
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    template_name = "newspaper/newspaper_delete.html"
    success_url = reverse_lazy("newspaper:newspaper-list")
    queryset = Newspaper.objects.select_related("topic")
