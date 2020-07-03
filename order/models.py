from catalog.models import product
from django.db      import models

class order(models.Model):
    fio     = models.CharField("ФИО", max_length=100)
    cart    = models.ManyToManyField(product)
    pubDate = models.DateTimeField('Дата оставления комметнария', auto_now=True)
    total   = models.FloatField("Сумма")
    phone   = models.CharField("Телефон", max_length=20)
    email   = models.EmailField("Email", max_length=254, null=True)
    address = models.TextField("Адрес доставки")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'