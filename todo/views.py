from django.shortcuts import render

from todo.models import Task


def index(request):
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    context = {
        "title": "welcome",
        "task_list": tasks
    }
    return render(request, "todo/index.html", context=context)
