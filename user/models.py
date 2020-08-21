from django.db                  import models
from django.contrib.auth.models import User
from catalog.models             import product


class UserProfile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar      = models.ImageField('Аватар пользователя', upload_to='user', null=False, default='avatar_default.png')
    address     = models.CharField('Адрес доставки', max_length=512, blank=True, null=True, default='Не указан')
    phone       = models.CharField('Номер телефона', max_length=12, blank=True, null=True, default='Не указан')
    post_index  = models.CharField('Почтовый индекс', max_length=7, blank=True, null=True, default='Не указан')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return str(self.user)



class Favorites(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite    = models.ManyToManyField(product)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return str(self.user)