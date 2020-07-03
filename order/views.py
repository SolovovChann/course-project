from .forms                 import orderForm
from cart.cart              import Cart
from cart.context_processor import cart_total_amount
from catalog.models         import product, comment, PRODUCT_TYPE
from django.conf            import settings
from django.shortcuts       import render, redirect
from django.contrib         import messages

def home(request):
    return render(request, 'makeorder.html', context=
    { 'SITE_NAME' : settings.SITE_NAME, 'CATEGORY' : "Оформление заказа",  'PRODUCT_TYPE' : PRODUCT_TYPE, 'form' : orderForm })


def makeorder(request):
    form = orderForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.total = float(cart_total_amount(request).get('cart_total_amount'))
        post.save()
        for key,value in request.session['cart'].items():
            post.cart.add( product.objects.get(pk = value['product_id']))
        cart = Cart(request)
        cart.clear()
        messages.success(request, 'Заказ успешно оформлен!')

    else:
        messages.error(request, 'Форма заполнена неверно!')
    return redirect('home')