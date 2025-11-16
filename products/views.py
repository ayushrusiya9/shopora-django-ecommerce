from django.shortcuts import render,redirect
from .models import Product,Cart,CartItem

# Create your views here.
def cart_item(request):

    # user login check
    if not request.user.is_authenticated:
        return redirect('login')

    cart_qs = Cart.objects.filter(user=request.user)

    if not cart_qs.exists():
        cart_items = []
        subtotal = 0
    else:
        cart = cart_qs.first()
        cart_items = CartItem.objects.filter(cart=cart)

        subtotal = 0
        for item in cart_items:
            subtotal += item.product.price * item.quantity

    context = {
        "cart_items": cart_items,
        "subtotal": subtotal
    }

    return render(request, 'product/cart_item.html', context)



def add_to_cart(request,pk):

    product = Product.objects.get(id=pk)

    cart = Cart.objects.get(user=request.user)

    if not cart:
        cart = Cart(request.user)
        cart.save()

    cart_item = CartItem.objects.get(cart=cart,product=product)

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = CartItem.objects.create(
            cart=cart,
            product=product
        )
    
    return redirect('cart_item')