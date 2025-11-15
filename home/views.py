from django.shortcuts import render
from products.models import Product,ProductImage,Category

# Create your views here.
def home(request):
    get_user = request.session.get('id',None)
    
    sort = request.GET.get('sort')

    # price range filtering
    if sort == "low":
        product_list = Product.objects.all().order_by("price")
    elif sort == "high":
        product_list = Product.objects.all().order_by("-price")
    elif sort == "latest":
        product_list = Product.objects.all().order_by("-created_at")
    else:
        product_list = Product.objects.all()
    
    context = {"products": product_list,"categories":Category.objects.all(),"get_user":get_user}
    
    return render(request, 'home/index.html',context)

def view_product(request,pk):
    product = Product.objects.get(uid=pk)

    images = product.images.all()
    first_image = images[0].image.url if images else None

    context = {
        "product":product,
        "images":images,
        "first_image":first_image
    }

    return render(request, 'product/product.html',context)

def category_product(request,pk):
    category = Product.objects.filter(category_id=pk)
    context = {"products": category,"categories":Category.objects.all()}
    return render(request, 'home/index.html',context)

