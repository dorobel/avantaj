from django.views import generic
from . import forms
from django.urls import reverse_lazy
from . import models
from django.http import Http404


class CreateClient( generic.CreateView):
    form_class = forms.ClientsForm     # sets class attribute -- Contextul va folosi acest form pt afisarea in pagina
    model = models.Clients             # sets class attribute   

                                                 
             
class ClientView(generic.DetailView):
    context_object_name = 'client_details'
    model = models.Clients
  
  

#https://stackoverflow.com/questions/39842386/django-simple-search-form  
class ClientList (generic.ListView):
    template ='clients_list.html'
    #context_object_name = 'client_details'
    model = models.Clients
    
    def get_queryset(self):
        try:  
            qcnp = self.request.GET.get('qcnp')             # Group.objects.filter
            qfname = self.request.GET.get('qfname')
            qlname = self.request.GET.get('qlname')
            
            if qcnp or (qfname and qlname):
                return models.Clients.objects.filter(cnp_nbr__exact=qcnp)
            elif qfname and qlname:
                return models.Clients.objects.filter(first_name__exact=qfname,last_name__exact=qlname)
        except models.Clients.DoesNotExist:
            raise Http404
        
        else:
            return models.Clients.objects.all()
        
        
        
    