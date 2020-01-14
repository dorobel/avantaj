from django.db import models
from django.contrib import auth
from django.utils import timezone

'''
from django.contrib.auth.models import User  == auth.models.User

#   django.contrib.auth.forms  
'''

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        #return "@{}".format(self.username)
        return f'@{self.username}'   # username e un atribut ce vine din auth.models.User


