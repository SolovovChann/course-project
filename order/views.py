from .                  import forms
from .models            import order, order_product
from cart.cart          import Cart
from cart.context_processor import get_total
from catalog.models     import product
from django.contrib     import messages
from django.shortcuts   import render, redirect


def home(request):
    if request.user.is_authenticated:
        return render(request, 'order/index.html', { 'TITLE' : 'Оформление заказа' })
    else:
        messages.error(request, 'Вы должны быть авторизированы, что бы оформить заказ')
        return redirect('home')


def make_order(request):
    if request.user.is_authenticated:
        Order = order(
            user=request.user,
            fio=request.POST.get('fio'),
            total=get_total(request),
            address=request.POST.get('address'),
            post_code=request.POST.get('post_code')
        )
        Order.save()
        for code, item in request.session['cart'].items():
            Product = product.objects.get(pk=item['product_id'])

            Product_order = order_product.objects.create(order=Order, product=Product, quantity=item['quantity'])
            Product_order.save()

            Product.was_bought(item['quantity'])
            Product.save()
    else:
        messages.error(request, 'Вы должны быть авторизированы, что бы оформить заказ')
        return redirect('user:login')

    cart = Cart(request)
    cart.clear()

    messages.success(request, 'Заказ успешно оформлен')
    return redirect('user:my_orders')