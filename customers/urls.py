from django.urls import path

from . import views

app_name = 'customers'
urlpatterns = [
    path('', views.index, name='home'),
    path('new-customer', views.new_customer, name='new_customer'),
    path('<int:customer_id>/', views.detail, name='detail')
]