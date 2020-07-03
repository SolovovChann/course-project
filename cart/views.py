from cart.cart              import Cart
from django.shortcuts       import render, redirect
from catalog.models         import product, PRODUCT_TYPE
from django.contrib         import messages
from django.conf            import settings

def cart_add(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    cart.add(product=Product)
    messages.success(request, 'Вы успешно добавили продукт в корзину')
    return redirect(request.META.get('HTTP_REFERER'))


def item_clear(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    cart.remove(Product)
    return redirect("cart:cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    cart.add(product=Product)
    return redirect("cart:cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    cart.decrement(product=Product)
    return redirect("cart:cart_detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart:cart_detail")


def cart_detail(request):
    return render(request, 'cart.html', context = { 'SITE_NAME' : settings.SITE_NAME, 'PRODUCT_TYPE' : PRODUCT_TYPE, 'CATEGORY' : "Корзина" })