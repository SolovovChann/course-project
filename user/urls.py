from .                      import views
from django.urls            import path, include
from django.contrib.auth    import views as auth_views

app_name = 'user'

urlpatterns = [
    # profile
    path('', views.home, name='home'),
    path('edit/',    views.edit, name = 'edit'),
    path('forget_password/', auth_views.PasswordResetView.as_view(template_name='user/form.html', extra_context={ 'TITLE' : 'Восстановление пароля' }), name = 'restore_password'),
    path('login/',   views.login, name = 'login'),
    path('logout/',  auth_views.LogoutView.as_view(), name = 'logout'),
    path('register/', views.register, name='register'),
    path('registrate/', views.registrate, name='registrate'),
    path('delete/', views.del_profile, name="del_profile"),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    # Favorites
    path('favorites/', views.favorites, name='favorites'),
    path('addfavorite/<int:product_id>', views.add_to_fav, name='add_to_fav'),
    path('delfavorite/<int:product_id>', views.del_from_fav, name='del_from_fav'),

    # My orders
    path('orders/', views.my_orders, name='my_orders'),
]