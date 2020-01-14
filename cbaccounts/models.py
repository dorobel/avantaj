from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Accounts(models.Model):
    
    account_number=models.PositiveIntegerField()
    
    
#acct_nbr int,
#balance int not null,
#acct_type varchar(2) not null,
#customer_id int not null,
#primary key (acct_nbr),
#constraint cust_id_fk foreign key (customer_id) references customer(customer_id),
#constraint acct_type_ck check(acct_type in ('B','D','C')))
    
    def get_absolute_url(self):
        return reverse( kwargs={"pk": self.pk } )
                       
    def __str__(self):
        return self.user.username
    
    
    
