from catalog.forms      import commentForm
from catalog.models     import product, PRODUCT_TYPE
from django.conf        import settings
from django.contrib     import messages
from django.http        import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts   import render, get_list_or_404, get_object_or_404, reverse
from django.utils       import timezone


def home(request):
    productList = product.objects.all()
    return render(request, 'base.html', context={ 'SITE_NAME' : settings.SITE_NAME, 'PRODUCT_TYPE' : PRODUCT_TYPE, 'CATEGORY' : "Каталог",  'productList' : productList })


def category(request, p_type):
    productList = product.objects.filter(p_type = p_type)
    for a in PRODUCT_TYPE:
        if a[0] == p_type:
            category = a[1]
    if category:
        return render(request, 'base.html', { 'SITE_NAME' : settings.SITE_NAME, 'PRODUCT_TYPE' : PRODUCT_TYPE, 'CATEGORY' : category, 'productList' :  productList })
    else: return Http404('Категория не найдена!')


def contacts(request):
    return render(request, 'contacts.html', 
    { 'SITE_NAME' : settings.SITE_NAME, 'PRODUCT_TYPE' : PRODUCT_TYPE, 'CATEGORY' : "Контакты" })


def search(request):
    results = get_list_or_404(product, name=request.GET.get("query"))
    return render(request, 'search.html', 
    { 'SITE_NAME' : settings.SITE_NAME, 'PRODUCT_TYPE' : PRODUCT_TYPE, 'CATEGORY' : "Результаты поиска", "results" : results })