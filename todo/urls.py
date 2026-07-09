from django.urls import path

from todo.views import TagListView, TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="home-page"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]
