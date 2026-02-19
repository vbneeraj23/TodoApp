from django.urls import path
from .views import (HomeView, AboutView, ContactView, UserLoginView, UserLogoutView, SignUpView, TaskListView, TaskDetailView, TaskDeleteView, TaskCreateView, TaskUpdateView)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("login/",UserLoginView.as_view(),name="login"),
    path("logout/",UserLogoutView.as_view(), name="logout"),
    path("signup/",SignUpView.as_view(),name="signup"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path('taskdetail/<int:pk>/', TaskDetailView.as_view(), name="Details"),
    path("deletetask/<int:pk>/", TaskDeleteView.as_view(), name="taskdelete"),
    path("tasks/add/", TaskCreateView.as_view(),name="task-create"),
    path("tasks/edit/<int:pk>/", TaskUpdateView.as_view(),name="task-edit"),
]