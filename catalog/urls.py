from django.urls    import path, include
from . import views

app_name = 'catalog'

urlpatterns = [
    path('detail/<int:product_id>/', views.detail, name='detail'),
    path('leavecomment/<int:product_id>', views.leave_comment, name='leave_comment'),
]