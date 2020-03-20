from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

'''
# from django.contrib.auth import views "as auth_views"
'''

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html", ),name='login'), # Un view precum ListView - nu apare in views.py
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),       # (esti redirectat pe pagina thanks -- vezi settings.py)                          
                                                                                                    
    path('signup/', views.SignUp.as_view(), name="signup"),  #http://127.0.0.1:8000/accounts/signup/
    path('passwordch/', views.PasswordChangeByUser.as_view(), name="pwdchange"),
    
    path('password_reset/', views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', views.PasswordResetView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]


