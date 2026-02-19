from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task
from .models import Contact

class SignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class TaskForm(forms.ModelForm):
    class Meta:
         model=Task
         fields=['title','description','completed']  

class Contactform(forms.ModelForm):
    class Meta:
         model=Contact
         fields = ['name','email','contact','message']

