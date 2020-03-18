from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.views import PasswordChangeView, PasswordResetCompleteView


# Create your views here.
class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("accounts:login")  # redirect spre pagina de logare
    template_name = "accounts/signup.html"


class PasswordChangeByUser(PasswordChangeView):  #req login first
    template_name = "accounts/change_by_user.html"
    success_url = reverse_lazy("accounts:login")
    
'''
Poti direct din URL sa faci referinta la acest view daca nu ai argumente aditionale pt a-l schimba

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('change-password/', auth_views.PasswordChangeView.as_view()),
]
'''
    
    