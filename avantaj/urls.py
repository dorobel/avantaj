from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views


app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.HomePage.as_view(), name="home"),
    path('welcome/', views.WelcomePage.as_view(), name="welcome"),
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    
    
    path('accounts/', include("accounts.urls", namespace="accounts")),
    
    
    path('administration/', include("administration.urls", namespace="administration")),
    
    
    #path ('', include('django.contrib.auth.urls'))
]
