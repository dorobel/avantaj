from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from administration.models import Clients

'''
Widgeturile sunt legate de clase CSS/Bootstrap

'''   

class ClientsForm(UserCreationForm):
    cnp_nbr =forms.IntegerField(label='CNP', widget=forms.TextInput(attrs={'class': 'form-control'}))  
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Your email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    verify_email = forms.EmailField (label='Re-enter you email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta(UserCreationForm.Meta):
        model = Clients
        fields = UserCreationForm.Meta.fields + ('password1','password2','cnp_nbr','address', 'email','verify_email')
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
        self.fields["password1"].label = "Passsword"
        self.fields["password2"].label = "Retype Passsword"

        
    def clean(self):  # most used!!!
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']
        
        if email != v_email:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!!")
        
        super().clean()
    
    
class SearchForm(forms.ModelForm):  
    cnp_nbr = forms.IntegerField(label='CNP', widget=forms.TextInput(attrs={'class': 'form-control'}))  
    first_name = forms.IntegerField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))  
    last_name = forms.IntegerField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta():
        model = Clients                                
        fields = ('cnp_nbr','first_name','last_name')
        
    def clean(self):
        super().clean()
        
        
        