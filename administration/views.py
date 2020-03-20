from django.views import generic
from . import forms
from . import models
from django.db.models import Q
from django.forms import ValidationError
from django.template.context_processors import request
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers


# Un user nu poate sa creeze/caute/updateze clienti samd pt ca in codul HTML are restrictia '{% if request.user.is_authenticated  %}"
# Un user nelogat ce acceseaza un URL al unuia din viewuri va vedea o pagina goala
# Pentru a i se afisa un ecran de ogin adugam  LoginRequiredMixin!
# Vezi https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.views.PasswordChangeView
class CreateClient(LoginRequiredMixin, generic.CreateView):
    form_class = forms.ClientsForm     # sets class attribute -- Contextul va folosi acest form pt afisarea in pagina
    model = models.Clients             # sets class attribute   


class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):              
    model = models.Clients  
    context_object_name = 'client_details'
    fields = ('username','first_name', 'last_name','cnp_nbr','address', 'email')  
    
      
class ClientView(LoginRequiredMixin, generic.DetailView):
    context_object_name = 'client_details'
    model = models.Clients
    template_name = "administration/client_details.html"

class ClientsSearch(LoginRequiredMixin, generic.FormView):
    form_class = forms.SearchForm
    template_name = "administration/clients_search.html"
    success_url = reverse_lazy('administration:searchresults')
    
    def form_valid(self, form):     # doar verifica ca datele au fost introduse in form corect!
        self.request.session['cnp_nbr'] = form.cleaned_data['cnp_nbr']
        self.request.session['first_name'] = form.cleaned_data['first_name']
        self.request.session['last_name'] = form.cleaned_data['last_name']
        return super().form_valid(form)

class SearchResults (LoginRequiredMixin, generic.ListView):
    model = models.Clients
    template_name='administration/search_results.html'
    context_object_name = 'all_search_results'
    
     
    def get_queryset(self): 
            return self.model.objects.filter(
            Q(cnp_nbr__exact=self.request.session['cnp_nbr']) | Q(first_name__iexact=self.request.session['first_name']) & Q(last_name__iexact=self.request.session['last_name']) 
        ) 


'''
Nu merge asa (cumva forms.as_p nu seteaza "name" sau ceva)

    def get_queryset(self): 
            return self.model.objects.filter(
            Q(cnp_nbr__exact=self.request.POST.get("cnp_nbr")) | Q(first_name__iexact=self.request.POST.get("first_name")) & Q(last_name__iexact=self.request.POST.get("last_name")) 
        ) 

        
Asa merrge:

 def get_queryset(self): 
            return self.model.objects.filter(
            Q(cnp_nbr__exact=self.request.session['cnp_nbr']) | Q(first_name__iexact=self.request.session['first_name']) & Q(last_name__iexact=self.request.session['last_name']) 
        ) 

'''
        
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
        
    
 
    
    
    
    