from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from administration.models import Clients


    
class WelcomePage(TemplateView):
    template_name = 'welcome.html'
    model = Clients

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'
