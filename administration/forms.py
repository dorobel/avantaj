from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from administration.models import Clients
from django.forms.widgets import Input, TextInput
from django.forms.forms import Form
'''
Widgeturile sunt legate de clase CSS/Bootstrap

'''   

class ClientsForm(UserCreationForm):
    cnp_nbr =forms.IntegerField(label='CNP', widget=forms.TextInput(attrs={'class': 'form-control'}))  
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Your email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    verify_email = forms.EmailField (label='Re-enter you email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta(UserCreationForm.Meta):
        model = Clients
        fields = UserCreationForm.Meta.fields + ('password1','password2','first_name', 'last_name','cnp_nbr','address', 'email','verify_email')
        
        
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
    
    
class SearchForm(forms.Form):  
    cnp_nbr = forms.IntegerField(label='CNP', widget=forms.TextInput(attrs={'class': 'form-control' }), required=False)  
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}),  required=False)  
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}),  required=False)
    
    class Meta():
        model = Clients                                
        fields = ('cnp_nbr','first_name','last_name')
        
    def clean(self):  # most used!!!
        all_clean_data = super().clean()
        cnp_nbr = all_clean_data.get('cnp_nbr')
        first_name = all_clean_data.get('first_name')
        last_name = all_clean_data.get('last_name')

        if  cnp_nbr is None and (first_name =='' or last_name ==''): #That's because a not required IntegerField will be None if it's empty, whereas a not required CharField will be '' (the empty string) if it's empty.
            raise forms.ValidationError("Enter either CNP either first_name&last_name")
            super().clean()
            
                # Boolean OR operator returns true if any one operand is true
                # Boolean AND operator returns true if both operands return true
                # The NOT operator returns true if its operand is a false expression and returns false if it is true.
                
                # DC cnp_nbr este null (TRUE)  si conditia ( first_name =='' or last_name =='' ) intoarce TRUE       ==> TRUE => Validation Error
                
                # Dc cnp_nbr are valoare (FALSE)  si conditia ( first_name =='' or last_name =='' ) intoarce TRUE    ==> FALSE => NO Validation error
                
                # DC cnp_nbr este null (TRUE) si conditia ( first_name =='' or last_name =='' ) intoarce FALSE       ==> FALSE => NO Validation error
                
                # DC cnp_nbr are valoare (FALSE) si conditia ( first_name =='' or last_name =='' ) intoarce FALSE    ==> FALSE => NO Validation error
                
        
            
   
    
