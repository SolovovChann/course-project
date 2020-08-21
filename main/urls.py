from .                          import views
from django.conf                import settings
from django.conf.urls.static    import static
from django.contrib             import admin
from django.urls                import path, include

# App urls
import cart.urls    as cart_urls
import catalog.urls as catalog_urls
import order.urls   as order_urls
import user.urls    as user_urls


urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Category
    path('category/<str:category>/', views.category, name='category'),

    # Search
    path('search/', views.search, name='search'),

    # Admin table
    path('admin/',  admin.site.urls),

    # Includes
    path('cart/',   include(cart_urls)),
    path('product/',include(catalog_urls)),
    path('checkout/',  include(order_urls)),
    path('user/',   include(user_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)