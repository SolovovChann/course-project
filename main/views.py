from django.shortcuts        import render, get_list_or_404, get_object_or_404, Http404, redirect, HttpResponse
from catalog.models          import product, product_type
from django.contrib          import messages
from django.contrib.postgres import search


def home(request):
    return render(request, 'catalog/index.html', { 'TITLE' : 'Главная страница', 'catalog' : product.objects.all() })


def category(request, category):
    pt = get_object_or_404(product_type, name=category)
    result = get_list_or_404(product, product_type=pt)
    return render(request, 'catalog/category.html', { 'TITLE' : pt.verbose, 'catalog' : result })


def search(request):
    query = request.POST.get('query').lower()

    if query is None:
        messages.error(request, 'Запрос пуст')
        return redirect('home')
    
    result = product.objects.filter(name__contains=query)
    return render(request, 'catalog/category.html', { 'TITLE' : 'Результаты поиска', 'catalog' : result })