from django.urls import reverse_lazy
from django.views import generic
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("home-page")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("home-page")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("home-page")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tag-list")
