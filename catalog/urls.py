from .                          import views
from django.conf                import settings
from django.conf.urls.static    import static
from django.urls                import path, include

app_name = 'catalog'

urlpatterns = [
    path('cart/', views.checkout, name='chechout'),
    path('<int:productId>/addToCart/', views.addToCart, name='addToCart'),
    path('<str:productId>/', views.productDetail, name='productDetail'),
    path('<str:productId>/leaveComment/', views.leaveComment, name='leaveComment'),
    path('<str:productId>/ratecomment/<str:commentId>/<str:vote>', views.rateComment, name='rateComment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)