from django.views import generic
from . import forms
from . import models
from django.db.models import Q
from django.forms import ValidationError

class CreateClient( generic.CreateView):
    form_class = forms.ClientsForm     # sets class attribute -- Contextul va folosi acest form pt afisarea in pagina
    model = models.Clients             # sets class attribute   

                                                 
             
class ClientView(generic.DetailView):
    context_object_name = 'client_details'
    model = models.Clients
    template_name = "administration/client_details.html"
  
  
class ClientsSearch(generic.FormView):
    form_class = forms.SearchForm
    model = models.Clients
    template_name = "administration/clients_search.html"

class SearchResults (generic.ListView):
    model = models.Clients
    template_name='administration/search_results.html'
    context_object_name = 'all_search_results'
    form = forms.SearchForm
    
    def get_queryset(self): 
        form = forms.SearchForm(self.request.GET)
        if form.is_valid():
                return self.model.objects.filter(
            Q(cnp_nbr__exact=form.cleaned_data['cnp_nbr']) | Q(first_name__exact=form.cleaned_data['first_name']) & Q(last_name__exact=form.cleaned_data['last_name'])
        )
            
        return models.Clients.objects.all()
    
    '''
    Whatever the data submitted with a form, once it has been successfully validated by calling is_valid() (and is_valid() has returned True), 
    the validated form data will be in the form.cleaned_data dictionary. This data will have been nicely converted into Python types for you.
    
    def get_queryset(self): 
        form = forms.SearchForm(self.request.GET)
        
        if form.is_valid():
            return self.model.objects.filter(
            Q(cnp_nbr__exact=form.cleaned_data['cnp_nbr']) | Q(first_name__exact=form.cleaned_data['first_name']) & Q(last_name__exact=form.cleaned_data['last_name'])
        )
            
        return models.Clients.objects.all()
    '''
        
    
 
    
    
    
    