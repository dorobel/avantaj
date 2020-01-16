from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin  # pip install django-braces
from . import forms
from django.urls import reverse_lazy
from . import models
from .models import Clients
from django.contrib.auth import get_user_model



class CreateClient( generic.CreateView):
    form_class = forms.ClientsForm     # sets class attribute -- Contextul va folosi acest form pt afisarea in pagina
    model = models.Clients             # sets class attribute   

    success_url = reverse_lazy('post_list')
                                                 
             
 
        