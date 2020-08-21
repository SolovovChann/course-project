from .settings      import SITE_NAME
from catalog.models import product_type
from user.models import UserProfile


def global_vars(request):
    user = request.user

    profile = UserProfile.objects.get(user=user) if user.is_authenticated else None

    return { 'SITE_NAME' : SITE_NAME, 'PRODUCT_TYPE' : product_type.objects.all(), 'profile' : profile }