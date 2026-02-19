from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from.forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Task, Contact
from django.urls import reverse_lazy
from .forms import TaskForm, Contactform

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"       

class UserLoginView(LoginView):
    template_name = "login.html" 

class UserLogoutView(LogoutView):
    next_page="login"

class SignUpView(FormView):
    template_name = "signup.html"
    form_class = SignUpForm
    
    def form_valid(self, form):

        user = form.save()
        login(self.request, user)
        return redirect("task-list")           

class TaskListView(LoginRequiredMixin,ListView): 
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
      return Task.objects.filter(user=self.request.user)
    
class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = "taskdetails_list.html"
    context_object_name = "tasks"    

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = "deletetask.html"
    context_object_name = "deletetask"
    success_url = reverse_lazy('task-list')
        
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
 
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ContactView(ContactView):
  model = Contact
  form_class = Contactform
  template_name = "contact.html"
  success_url = reverse_lazy("home")
