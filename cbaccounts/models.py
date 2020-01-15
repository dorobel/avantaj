from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from encrypted_model_fields.fields import EncryptedCharField
import random
import string
#pip install django-encrypted-model-fields
#https://stackoverflow.com/questions/1743764/how-can-i-pass-a-user-model-into-a-form-field-django

class Accounts(models.Model):
    acct_nbr  = EncryptedCharField(max_length=16)
    balance   = models.IntegerField()
    acct_type = models.CharField(max_length=2)
    customer_id = models.ForeignKey(User, related_name="user_accounts_id",on_delete=models.DO_NOTHING(None, None, None, None)),
    username = models.ForeignKey(User, related_name="user_accounts_name",on_delete=models.DO_NOTHING(None, None, None, None)),
    
    
    def save(self, *args, **kwargs):
        def acct_nbr_generator(size=16, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))
        self.acct_nbr = acct_nbr_generator()
        super().save(*args, **kwargs)
        
    def decrypt_acct(self):
        if self.acct_nbr != None:
            self.acct_nbr._decrypt()
    
    def get_absolute_url(self):
        return reverse( kwargs={"pk": self.pk } )
                       
    def __str__(self):
        return self.user.username
    
    
    
