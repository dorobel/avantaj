from django.views import generic
from . import forms
from django.urls import reverse_lazy
from . import models
from django.http import Http404
import operator
from django.db.models import Q
from functools import reduce

class CreateClient( generic.CreateView):
    form_class = forms.ClientsForm     # sets class attribute -- Contextul va folosi acest form pt afisarea in pagina
    model = models.Clients             # sets class attribute   

                                                 
             
class ClientView(generic.DetailView):
    context_object_name = 'client_details'
    model = models.Clients
  
  

#https://stackoverflow.com/questions/39842386/django-simple-search-form  
   # template_name = 'administration/clients_search.html'    
    #form_class = forms.SearchForm
class ClientsSearch(generic.DetailView):
    form_class = forms.SearchForm
    model = models.Clients
    template_name = "administration/clients_search.html"
    
    #ClientsList is missing a QuerySet. Define ClientsList.model, ClientsList.queryset, or override ClientsList.get_queryset().
    def get_queryset(self):
        result = super().get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(cnp_nbr__exact=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(first_name__exact=q) for q in query_list))
            )

        return result

class ClientsList (generic.ListView):
    model = models.Clients
    context_object_name = 'clients_list'
    
    #ClientsList is missing a QuerySet. Define ClientsList.model, ClientsList.queryset, or override ClientsList.get_queryset().
    def get_queryset(self):
        result = super().get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(cnp_nbr__exact=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(first_name__exact=q) for q in query_list))
            )

        return result 
'''
    try:  
            qcnp = self.request.GET.get('qcnp')             # Group.objects.filter
            qfname = self.request.GET.get('qfname')
            qlname = self.request.GET.get('qlname')
            
            if qcnp or (qfname and qlname):
                result = models.Clients.objects.filter(cnp_nbr__exact=qcnp)
                return result
            elif qfname and qlname:
                result = models.Clients.objects.filter(first_name__exact=qfname,last_name__exact=qlname)
                return result
        except models.Clients.DoesNotExist:
            raise Http404
        
        else:
            result = None
       
'''            
 
    
    
    
    