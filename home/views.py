from django.shortcuts import render
from products.models import Product,ProductImage,Category

# Create your views here.
def home(request):
    context = {"products": Product.objects.all(),"categories":Category.objects.all()}
    return render(request, 'home/index.html',context)