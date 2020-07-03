from .                          import views
from cart                       import urls as cart_urls
from catalog                    import urls as catalog_urls
from django.conf                import settings
from django.conf.urls.static    import static
from django.contrib             import admin
from django.urls                import path, include
from grappelli                  import urls as grapelli_urls
from order                      import urls as order_urls

urlpatterns = [
    path('', views.home, name="home"),
    path('grappelli/', include(grapelli_urls)), # grappelli URLS
    path('admin/', admin.site.urls),
    path('category/<str:p_type>', views.category, name="category"),
    path('contacts/', views.contacts, name="contacts"),
    path('search/', views.search, name="search"),
    path('product/', include(catalog_urls)),
    path('cart/', include(cart_urls)),
    path('order/', include(order_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)