from django.db import models
from django.urls import reverse
from django.contrib import auth


#from encrypted_model_fields.fields import EncryptedCharField
#pip install django-encrypted-model-fields
#https://stackoverflow.com/questions/37741339/how-to-encrypt-textfield-before-saving-in-database
#https://stackoverflow.com/questions/1743764/how-can-i-pass-a-user-model-into-a-form-field-django

class Clients(auth.models.User,auth.models.PermissionsMixin):
    address = models.CharField(max_length=100, default="",null=False)
    created_at = models.DateTimeField(auto_now=True)
    cnp_nbr  = models.PositiveIntegerField()
    
    def get_absolute_url(self):
        return reverse( "administration:client_details", kwargs={ "pk": self.pk } ) 
    
     # puteai folosi reverse lazy in view si
     # return reverse( kwargs={ "pk": self.pk } )
      
      
    def __str__(self):
        #return "@{}".format(self.username)
        return f'@{self.username}'   # username e un atribut ce vine din auth.models.User





