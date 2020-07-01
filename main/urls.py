from .                          import views
from catalog                    import urls as catalog_urls
from django.conf                import settings
from django.conf.urls.static    import static
from django.contrib             import admin
from django.urls                import path, include

urlpatterns = [
    path('', views.home, name="home"),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('category/<str:p_type>', views.category, name="category"),
    path('contacts/', views.contacts, name="contacts"),
    path('search/', views.search, name="search"),
    path('product/', include(catalog_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)