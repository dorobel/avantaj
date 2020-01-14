from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

'''
# from django.contrib.auth import views "as auth_views"
'''

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'), # Un view precum ListView
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),       # (esti redirectat pe pagina thanks -- vezi settings.py)                          
                                                                                                    
    path('signup/', views.SignUp.as_view(), name="signup"),
]


