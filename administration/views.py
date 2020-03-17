from django.views import generic
from . import forms
from . import models
from django.db.models import Q
from django.forms import ValidationError
from django.template.context_processors import request
from django.urls import reverse_lazy,reverse


class CreateClient( generic.CreateView):
    form_class = forms.ClientsForm     # sets class attribute -- Contextul va folosi acest form pt afisarea in pagina
    model = models.Clients             # sets class attribute   


class ClientUpdateView(generic.UpdateView):              
    model = models.Clients  
    context_object_name = 'client_details'
    fields = ('username','first_name', 'last_name','cnp_nbr','address', 'email')  
    
      
class ClientView(generic.DetailView):
    context_object_name = 'client_details'
    model = models.Clients
    template_name = "administration/client_details.html"
  
  
class ClientsSearch(generic.FormView):
    form_class = forms.SearchForm
    template_name = "administration/clients_search.html"
    success_url = reverse_lazy('administration:searchresults')
    
    def form_valid(self, form):     # doar verifica ca datele au fost introduse in form corect!
        self.request.session['cnp_nbr'] = form.cleaned_data['cnp_nbr']
        self.request.session['first_name'] = form.cleaned_data['first_name']
        self.request.session['last_name'] = form.cleaned_data['last_name']
        return super().form_valid(form)

class SearchResults (generic.ListView):
    model = models.Clients
    template_name='administration/search_results.html'
    context_object_name = 'all_search_results'
    
    def get_queryset(self): 
            return self.model.objects.filter(
            Q(cnp_nbr__exact=self.request.session['cnp_nbr']) | Q(first_name__iexact=self.request.session['first_name']) & Q(last_name__iexact=self.request.session['last_name']) 
        )
        
    

'''
class ClientsSearch(generic.FormView):
    form_class = forms.SearchForm
    model = models.Clients
    template_name = "administration/clients_search.html"
    

class SearchResults (generic.ListView):
    model = models.Clients
    template_name='administration/search_results.html'
    context_object_name = 'all_search_results'
    
    def get_queryset(self): 
        form = forms.SearchForm(self.request.GET)
        if form.is_valid():
            return self.model.objects.filter(
            Q(cnp_nbr__exact=form.cleaned_data['cnp_nbr']) | Q(first_name__exact=form.cleaned_data['first_name']) & Q(last_name__exact=form.cleaned_data['last_name'])
        )
        else:
            form = forms.SearchForm
        
    '''
        
    
 
    
    
    
    