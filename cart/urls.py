from .                          import views
from django.conf                import settings
from django.conf.urls.static    import static
from django.urls                import path, include

app_name = 'cart'

urlpatterns = [
#   Cart urls
    path('add/<int:id>/', views.cart_add, name='cart_add'),
    path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart-detail/',views.cart_detail,name='cart_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)