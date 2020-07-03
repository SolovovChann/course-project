from .                          import views
from django.conf                import settings
from django.conf.urls.static    import static
from django.urls                import path, include

app_name = 'order'

urlpatterns = [
    path('', views.home, name='home'),
    path('makeorder/', views.makeorder, name='makeorder'),
]
