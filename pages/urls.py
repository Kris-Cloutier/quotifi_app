from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='home'),
    path('newCustomer/', views.newCustomer, name='newCustomer'),
    path('newOrder/', views.newOrder, name='newOrder'),
]