from django.contrib.auth.forms  import User
from django.shortcuts           import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth        import authenticate, login as auth_login
from django.contrib             import messages
from .models                    import UserProfile, Favorites
from catalog.models             import product
from .forms                     import EditProfileForm


def home(request):
    return render(request, 'user/index.html', { 'TITLE' : 'Моя страница'})


def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Вы успешно авторизировались')
            else:
                messages.error(request, 'Что-то пошло не так, мы не смогли вас авторизовать 😥')
    else:
        messages.error(request, 'Вы уже авторизованы')
        
    return redirect('home')


def register(request):
    return render(request, 'user/register.html', { 'TITLE' : 'Регистрация нового пользователя' })


def registrate(request):
    if request.POST.get('password') == request.POST.get('confirm'):
        user = User.objects.create_user(
            username= request.POST.get('username'),
            email= request.POST.get('email'),
            password= request.POST.get('password'),
            first_name= request.POST.get('first_name'),
            last_name= request.POST.get('last_name')
        )
        if user:
            messages.success(request, 'Профиль успешно создан')
            auth_login(request, user)
            profile = UserProfile(user=user)
            profile.save()

            favorite = Favorites(user=user)
            favorite.save()
        else:
            messages.success(request, 'Произошла ошибка создание профиля')
        return redirect('home')
    else:
        messages.error(request, 'Пароли не совпадают')
        return redirect('user:register')


def edit(request):
    form = EditProfileForm()
    return render(request, 'user/edit_profile.html', { 'TITLE' : 'Изменение информации профиля', 'form' : form })


def edit_profile(request):
    if request.method == 'POST':

        user = request.user

        profile = UserProfile.objects.filter(user=user)
        profile.set(avatar=request.POST.get('avatar'), adress=request.POST.get('adress'), phone=request.POST.get('phone'), post_index=request.POST.get('post_index'))
        profile.save()

        messages.success(request, 'Изменения сохранены')
    else:
        messages.error(request, 'Никакие данные не были введены')
    return redirect('user:home')


def del_profile(request):
    user = request.user
    try:
        user.delete()
        messages.success(request, 'Профиль успешно удалён')
    except:
        messages.error(request, 'Произошла ошибка удаления профиля')
    return redirect('home')


def favorites(request):
    return render(request, 'user/favorites.html', { 'TITLE' : 'Избранное', 'catalog' : get_list_or_404(Favorites ,user=request.user) })


def add_to_fav(request, product_id):
    if request.user.is_authenticated:
        item = get_object_or_404(product, id=product_id)
        fav = Favorites(user=request.user)
        fav.favorite.set(item)
        fav.save()

        messages.success(request, 'Продукт успешно добавлен в избранное')

    else:
        messages.error(request, 'Вы должны быть авторизованы что бы добавить продукт в избранное')
        return redirect('home')
    return redirect(request.META.get('HTTP_REFERER', '/'))


def del_from_fav(request, product_id):
    item = get_object_or_404(product)
    fav = Favorites(user=request.user, favorite=item)
    fav.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


def my_orders(request):
    return render(request, 'user/orders.html', { 'TITLE' : 'Мои заказы' })