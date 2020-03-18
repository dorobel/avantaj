from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

app_name='administration'

urlpatterns = [
    path("new/", views.CreateClient.as_view(), name="create"),
    path("client/<pk>", views.ClientView.as_view(), name="client_details"),
    path("search", views.ClientsSearch.as_view(), name="search"),
    path("searchresults",cache_page(60 * 15)(views.SearchResults.as_view()), name="searchresults"),
    path('update/<int:pk>/',views.ClientUpdateView.as_view(),name='update'), 
]
