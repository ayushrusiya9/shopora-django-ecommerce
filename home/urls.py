from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('view_product/<slug:pk>/',views.view_product, name='view_product')
]