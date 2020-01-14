from django.db import models
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User
from cbaccounts.models import Accounts



class Clients(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    
    account_number=models.ForeignKey(Accounts, related_name="accounts",on_delete=models.DO_NOTHING(None, None, None, None))
    
    def get_absolute_url(self):
        return reverse( kwargs={"username": self.user.username, "pk": self.pk } )
                       
    def __str__(self):
        return self.user.username
    
    








