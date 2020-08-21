from .              import views
from django.urls    import path, include


app_name = 'order'

urlpatterns = [
    path('', views.home, name='home'),
    path('makeorder', views.make_order, name='makeorder'),
]