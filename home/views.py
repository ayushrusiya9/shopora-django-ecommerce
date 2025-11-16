from django.shortcuts import render
from products.models import Product,ProductImage,Category
from django.db.models import Q

# Create your views here.
def home(request):
    get_user = request.session.get('id',None)
    
    #for price sort 
    sort = request.GET.get('sort')

    # for search box
    search = request.GET.get('search')

    # price range filtering
    if search:
        product_list = Product.objects.filter(Q(name__icontains=search) | Q(description__icontains=search) | Q(price__icontains=search))

    elif sort == "low":
        product_list = Product.objects.all().order_by("price")
    elif sort == "high":
        product_list = Product.objects.all().order_by("-price")
    elif sort == "latest":
        product_list = Product.objects.all().order_by("-created_at")

    else:
        product_list = Product.objects.all()
    
    context = {"products": product_list,
               "categories":Category.objects.all(),
               "get_user":get_user,
               "search":search}
    
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

