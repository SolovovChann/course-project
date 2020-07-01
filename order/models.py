from catalog.models import product
from django.db      import models

class order(models.Model):
    fio     = models.CharField("ФИО", max_length=100)
    product = models.ForeignKey(product, verbose_name=("Продукт"), on_delete=models.CASCADE)
    amount  = models.PositiveIntegerField("Количество")
    address = models.CharField("Адрес", max_length=120)