from .models import Cart

def cart_count(request):
    cart_counting = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user = request.user).first()
        if cart:
            cart_counting = cart.cart_item.count()
    return {"cart_count":cart_counting}