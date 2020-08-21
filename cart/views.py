from cart.cart              import Cart
from django.shortcuts       import render, redirect
from catalog.models         import product
from django.contrib         import messages
from django.conf            import settings


def home(request):
    return render(request, 'cart/cart.html', context = { 'TITLE' : 'Корзина' })


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
    return redirect("cart:home")


def item_increment(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    cart.add(product=Product)
    return redirect("cart:home")


def item_decrement(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    cart.decrement(product=Product)
    return redirect("cart:home")


def item_add(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    quantity = int(request.POST.get('quantity'))
    if quantity <= 0 or quantity > Product.on_stock:
        cart.remove(product=Product)
    else:
        cart.add(product=Product, quantity=quantity)
    return redirect('cart:home')


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart:home")