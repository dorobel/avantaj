from django.db import models
from django.urls import reverse
from administration.models import Clients


class Accounts(models.Model):
    acct_nbr  = models.PositiveIntegerField()
    balance   = models.IntegerField()
    acct_type = models.CharField(max_length=2)
    username = models.ForeignKey(Clients, related_name="user_accounts",on_delete=models.DO_NOTHING),
    
    
    def get_absolute_url(self):
        return reverse( kwargs={"pk": self.pk } )
                       
    def __str__(self):
        return self.user.username
    
    
    
