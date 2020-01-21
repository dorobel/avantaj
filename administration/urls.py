from django.urls import path
from . import views

app_name='administration'

urlpatterns = [
    path("new/", views.CreateClient.as_view(), name="create"),
    path("client/<pk>", views.ClientView.as_view(), name="client_detail")
    
    
]
