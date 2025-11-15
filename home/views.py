from django.shortcuts import render
from products.models import Product,ProductImage,Category

# Create your views here.
def home(request):
    get_user = request.session.get('id',None)
    print(get_user)
    context = {"products": Product.objects.all(),"categories":Category.objects.all(),"get_user":get_user}
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

