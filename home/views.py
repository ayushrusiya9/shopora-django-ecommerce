from django.shortcuts import render
from products.models import Product,ProductImage

# Create your views here.
def home(request):
    context = {"products": Product.objects.all(),"product_image":ProductImage.objects.all()}
    print()
    return render(request, 'home/index.html',context)