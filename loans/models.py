from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Loans(models.Model):
    loan_nbr  = models.PositiveIntegerField(primary_key=True)
    loan_type = models.CharField(max_length=2)
    loan_amt  = models.PositiveIntegerField
    start_date = models.DateTimeField(blank=True, null=True)
    close_date = models.DateTimeField(blank=True, null=True)
    customer_id = models.ForeignKey(User, related_name="user_accounts",on_delete=models.DO_NOTHING(None, None, None, None)),
    
   
    def get_absolute_url(self):
        return reverse( kwargs={"pk": self.pk } )
                       
    def __str__(self):
        return self.user.username
    
