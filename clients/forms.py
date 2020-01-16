from django import forms
from .models import Clients
from django.contrib.auth.models import User
from _overlapped import NULL

'''
Widgeturile sunt legate de clase CSS/Bootstrap

'''   

class ClientsForm(forms.ModelForm):
    cnp_nbr =forms.IntegerField(label='CNP', widget=forms.TextInput(attrs={'class': 'form-control'}))  
    first_name = forms.CharField(label='Your name', widget=forms.TextInput(attrs={'class': 'form-control'}))  
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Your email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    verify_email = forms.EmailField (label='Re-enter you email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    
    class Meta:
        model = Clients
        fields = ('first_name','last_name','cnp_nbr', 'address', 'email','verify_email')

        
    def clean(self):  # most used!!!
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        cnp=all_clean_data['cnp_nbr']
        first_name = all_clean_data['first_name']
        last_name = all_clean_data['last_name']
        address = all_clean_data['address']
        
        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
        
        if cnp is NULL and len(cnp)<13:
            raise forms.ValidationError("CNP cant be null or less than 13 ")
        
        if first_name is NULL:
            raise forms.ValidationError("first_name cant be null ")
        
        if last_name is NULL:
            raise forms.ValidationError("last_name cant be null ")
        
        if address is NULL:
            raise forms.ValidationError("Address cant be null ")
        
        