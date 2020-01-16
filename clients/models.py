from django.db import models
from django.urls import reverse
from cbaccounts.models import Accounts
from encrypted_model_fields.fields import EncryptedCharField

#pip install django-encrypted-model-fields
#https://stackoverflow.com/questions/37741339/how-to-encrypt-textfield-before-saving-in-database
#https://stackoverflow.com/questions/1743764/how-can-i-pass-a-user-model-into-a-form-field-django

class Clients(models.Model):
    
    first_name = models.CharField(max_length=50,default="", null=False)
    last_name = models.CharField(max_length=50,default="", null=False)
    email =  models.CharField(max_length=80,default="", unique=True)
    address = models.CharField(max_length=100, default="",null=False)
    created_at = models.DateTimeField(auto_now=True)
    cnp_nbr  = EncryptedCharField(max_length=13,default="", null=False)
    
    
    def get_absolute_url(self):
        return reverse( kwargs={ "pk": self.pk } )
                       
    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ["-created_at"]
        unique_together = ["first_name", "last_name"]








