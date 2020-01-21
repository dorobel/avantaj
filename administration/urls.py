from django.urls import path
from . import views

app_name='administration'

urlpatterns = [
    path("new/", views.CreateClient.as_view(), name="create"),
    path("client/<pk>", views.ClientView.as_view(), name="client_detail"),
    path("clientssrc", views.ClientsSearch.as_view(), name="search"),
    #path("clientslist", views.ClientsList.as_view(), name="clientslist")
]
