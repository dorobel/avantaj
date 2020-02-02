from django.db import models
from django.urls import reverse
from administration.models import Clients
#from encrypted_model_fields.fields import EncryptedCharField


class Cards(models.Model):
    #card_nbr  = EncryptedCharField(max_length=16)
    #cvv_code  = EncryptedCharField(max_length=3)
    card_type = models.CharField(max_length=2)
    start_date = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    customer_id = models.ForeignKey(Clients, related_name="user_cards",on_delete=models.DO_NOTHING),
    
    
    def get_absolute_url(self):
        return reverse( kwargs={"pk": self.pk } )
                       
    def __str__(self):
        return self.user.username



