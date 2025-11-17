from django.urls import path,include
from . import views


urlpatterns = [
    path('add_to_cart/<slug:pk>/',views.add_to_cart,name='add_to_cart'),
    path('cart_item/',views.cart_item,name='cart_item'),
    path('create_order/',views.create_order,name='create_order'),
    # path('pay/', views.p, name="payment"),
    path('payment-status/',views.payment_status,name='payment-status'),
    path('success/',views.success,name='success'),
]