import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import JsonResponse
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
    product = Product.objects.get(uid=pk)

    if not request.user.is_authenticated:
        return redirect('login')  

    # always return single object
    cart = Cart.objects.filter(user=request.user).first()

    if not cart:
        cart = Cart.objects.create(user=request.user)

    cart_item = CartItem.objects.filter(cart=cart, product=product).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        CartItem.objects.create(cart=cart, product=product, quantity=1)
    
    return redirect('cart_item')
    # return redirect(request.META.get('HTTP_REFERER', 'home'))


# razorpay create order
def create_order(request):

    if not request.user.is_authenticated:
        return redirect('login')

    # Get cart
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        return redirect('cart_item')

    cart_items = CartItem.objects.filter(cart=cart)
    subtotal = sum([item.product.price * item.quantity for item in cart_items])

    if subtotal <= 0:
        return redirect('cart_item')

    # Razorpay amount in paisa
    amount = int(subtotal * 100)

    client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
    )
    print("key: ",settings.RAZORPAY_KEY_ID)

    order = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": 1
    })

    return render(request, "product/checkout.html", {
        "order": order,
        "cart_items": cart_items,
        "subtotal": subtotal,
        "razorpay_key": settings.RAZORPAY_KEY_ID
    })

@csrf_exempt
def payment_status(request):
    import json
    data = json.loads(request.body)

    client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
    )
    print("paymnt order id:",data["razorpay_order_id"])
    print(" payment id:",data["razorpay_payment_id"])
    print(" signature: :",data["razorpay_signature"])
    try:
        client.utility.verify_payment_signature({
            "razorpay_order_id": data["razorpay_order_id"],
            "razorpay_payment_id": data["razorpay_payment_id"],
            "razorpay_signature": data["razorpay_signature"]
        })

        return JsonResponse({"status":True})

    except:
        return JsonResponse({"status": False})


def success(request):
    status = request.GET.get("status")
    print(status)
    return render(request,'product/success.html',{"status":status})