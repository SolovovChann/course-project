from catalog.models import product
from django.contrib.auth.forms import User
from django.db      import models
from catalog.models import product


class order(models.Model):
    user    = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='Пользователь')
    fio     = models.CharField('ФИО пользователя', max_length=256)
    total   = models.FloatField('Итоговая стоимость')
    address = models.CharField('Адрес доставки', max_length=256)
    post_code = models.CharField('Почтовый код', max_length=10)
    date    = models.DateField('Дата оформления заказа', auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return self.fio


class order_product(models.Model):
    order    = models.ForeignKey(order, on_delete=models.CASCADE, verbose_name='Код заказа')
    product  = models.ForeignKey(product, null=True, on_delete=models.SET_NULL, verbose_name='Код продукта')
    quantity = models.PositiveIntegerField('Количество')