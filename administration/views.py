from django.views import generic
from . import forms
from . import models
from django.db.models import Q



class CreateClient( generic.CreateView):
    form_class = forms.ClientsForm     # sets class attribute -- Contextul va folosi acest form pt afisarea in pagina
    model = models.Clients             # sets class attribute   

                                                 
             
class ClientView(generic.DetailView):
    context_object_name = 'client_details'
    model = models.Clients
    template_name = "administration/client_details.html"
  
  

#https://stackoverflow.com/questions/39842386/django-simple-search-form  
    # template_name = 'administration/clients_search.html'    
    #form_class = forms.SearchForm
    
class ClientsSearch(generic.FormView):
    form_class = forms.SearchForm
    model = models.Clients
    template_name = "administration/clients_search.html"

class SearchResults (generic.ListView):
    model = models.Clients
    template_name='administration/search_results.html'
    context_object_name = 'all_search_results'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        return self.model.objects.filter(
            Q(cnp_nbr__icontains=query) | Q(first_name__icontains=query)| Q(last_name__icontains=query)
        )
        
        
    
 
    
    
    
    