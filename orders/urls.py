from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('new-order', views.new_order_view, name='new-order'),
    path('', views.order_view, name='orders'),
]