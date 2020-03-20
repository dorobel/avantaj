from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView


# Create your views here.
class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("accounts:login")  # redirect spre pagina de logare
    template_name = "accounts/signup.html"
    form_valid_message = "You're signed up!"


class PasswordChangeByUser(PasswordChangeView):  #req login first
    template_name = "accounts/change_by_user.html"
    success_url = reverse_lazy("accounts:login")




class PasswordResetView(PasswordResetView):
    #form_class = forms.PasswordResetForm
    template_name = "accounts/password_reset.html"
    success_url = reverse_lazy("accounts:password_reset_done")
    #subject_template_name = "accounts/emails/password-reset-subject.txt"
    email_template_name = "accounts/password_reset_email.html"    
    
class PasswordResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"  
    
class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:password_reset_complete")
    
class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/password_resetconfirm_done.html"   
    
    
'''
Poti direct din URL sa faci referinta la acest view daca nu ai argumente aditionale pt a-l schimba

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('change-password/', auth_views.PasswordChangeView.as_view()),
]
'''
    
    