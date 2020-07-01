from .forms             import commentForm
from .models            import product, comment, PRODUCT_TYPE, cart
from django.conf        import settings
from django.conf        import settings
from django.contrib     import messages
from django.http        import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts   import render, reverse, get_list_or_404, get_object_or_404
from django.utils       import timezone

def productDetail(request, productId):
    query = get_object_or_404(product, id = int(productId))
    return render(request, 'detail.html', 
    { 'SITE_NAME' : settings.SITE_NAME, 'CATEGORY' : query.name,  'product' : query, 'PRODUCT_TYPE' : PRODUCT_TYPE, 'commentForm' : commentForm  })


def leaveComment(request, productId):
    if 'has_commented' not in request.session:
        request.session['has_commented'] = list()
        request.session.modified = True

    if int(productId) in request.session['has_commented']:
        messages.error(request, 'Вы уже оставили комментарий')
        return HttpResponseRedirect(reverse('catalog:productDetail', args=[productId]))

    prod = get_object_or_404(product, pk=productId)
    form = commentForm(request.POST)
    
    if form.is_valid():
        post = form.save(commit=False)
        post.product = prod
        if 'username' in request.session:
            post.authorName = request.session['username']
        else:
            post.authorName = 'Аноним'
        post.pubDate = timezone.now()
        post.save()
        request.session['has_commented'].append(int(productId))
        request.session.modified = True
        messages.success(request, 'Комментарий успешно добавлен!')
    else:
        form = commentForm()
    return HttpResponseRedirect(reverse('catalog:productDetail', args=[prod.id]))


def rateComment(request, productId, commentId, vote):
    #   define massive of comments that was already voted
    if 'raited_comments' not in request.session:
        request.session['raited_comments'] = list()
        request.session.modified = True

    if int(commentId) in request.session['raited_comments']:
        messages.error(request, 'Вы уже оценили этот комментарий')
        return HttpResponseRedirect(reverse('catalog:productDetail', args=[productId]))
    Comment = get_object_or_404(comment, pk=int(commentId))
    if (vote == 'upvote'):
        Comment.likes += 1 
    elif (vote == 'downvote'):
        Comment.dsilikes += 1
    else:
        messages.error(request, 'Не удалось добавить комментарий')
        return reverse('catalog:productDetail', args=[productId])
    Comment.save()
    request.session['raited_comments'].append(int(commentId))
    messages.success(request, 'Комментарий успешно добавлен')
    request.session.modified = True
    return HttpResponseRedirect(reverse('catalog:productDetail', args=[productId]))


def addToCart(request, productId):
    CART = cart(request)
    prod = get_object_or_404(product, pk=productId)
    if request.POST.get('quantity'):
        quantity = int(request.POST.get('quantity'))
    else:
        quantity = 1
    CART.add(product=prod, quantity=quantity, update_quantity=True)
    return HttpResponseRedirect( 'catalog:checkout' )


def checkout(request):
    return render(request, 'cart.html', 
    { 'SITE_NAME' : settings.SITE_NAME, 'CATEGORY' : 'Корзина',  'PRODUCT_TYPE' : PRODUCT_TYPE, })