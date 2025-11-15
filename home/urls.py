from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('view_product/<slug:pk>/',views.view_product, name='view_product'),
    path('category_product/<slug:pk>/',views.category_product,name='category_product'),
]