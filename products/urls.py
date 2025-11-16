from django.urls import path,include
from . import views


urlpatterns = [
    path('add_to_cart/<slug:pk>/',views.add_to_cart,name='add_to_cart'),
    path('cart_item/',views.cart_item,name='cart_item')
]