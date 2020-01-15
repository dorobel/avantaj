from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from encrypted_model_fields.fields import EncryptedCharField
import random
import string

#pip install django-encrypted-model-fields
#https://stackoverflow.com/questions/1743764/how-can-i-pass-a-user-model-into-a-form-field-django

class Cards(models.Model):
    card_nbr  = EncryptedCharField(max_length=16)
    cvv_code  = EncryptedCharField(max_length=3)
    card_type = models.CharField(max_length=2)
    start_date = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    customer_id = models.ForeignKey(User, related_name="user_accounts",on_delete=models.DO_NOTHING(None, None, None, None)),
    
    
    def save(self, *args, **kwargs):
        def card_nbr_generator(size=16, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))
        def cvv_generator(size=3, nums=string.digits):
            return ''.join(random.choice(nums) for _ in range(size))
        self.acct_nbr = card_nbr_generator()
        self.cvv_code = cvv_generator()
        super().save(*args, **kwargs)
    
    def decrypt_card_nbr(self):
        if self.card_nbr != None:
            self.card_nbr._decrypt()
    
    def decrypt_card_cvv(self):
        if self.card_cvv != None:
            self.card_cvv._decrypt()
          
    def get_absolute_url(self):
        return reverse( kwargs={"pk": self.pk } )
                       
    def __str__(self):
        return self.user.username
