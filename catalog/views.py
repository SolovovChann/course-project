from django.shortcuts   import render, get_object_or_404, HttpResponse, redirect
from catalog.models     import product, comment
from django.contrib     import messages


def detail(request, product_id):
    result = get_object_or_404(product, pk=product_id)
    return render(request, 'catalog/detail.html', { 'TITLE' : result.name, 'product' : result })


def leave_comment(request, product_id):
    if request.user.is_authenticated:
        commentary = comment(product=product.objects.get(pk=product_id), author=request.user, text=request.POST.get('text'), rate=request.POST.get('rate'))
        commentary.save()
    else:
        messages.error(request, 'Вы должны быть авторизированы что бы оставлять комментарии')
        return redirect('user:login')
    return redirect(request.META.get('HTTP_REFERER'))