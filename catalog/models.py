from django.contrib.auth.forms import User
from django.db          import models
from django.shortcuts   import get_list_or_404
from django.conf        import settings


class product_type(models.Model):
    verbose = models.CharField('Название', max_length=75)
    plural  = models.CharField('Название мн. ч', max_length=75)
    name    = models.CharField('Название исп. для ссылок', max_length=50)

    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Типы продуктов'

    def __str__(self):
        return self.verbose


class product(models.Model):
    name            = models.CharField('Название', max_length=30, null=False, blank=False)
    description     = models.TextField('Описание', max_length=250, null=True, blank=True)
    price           = models.FloatField('Цена', null=False, blank=False)
    sale            = models.PositiveIntegerField('Скидка (указывать в процентах)', null=True, blank=True)
    image           = models.ImageField('Превью', upload_to='product', null=False, blank=False, default='default.png')
    on_stock        = models.PositiveIntegerField('Доступно на складе')
    avalible        = models.BooleanField('Доступно для покупки', default=bool(on_stock))
    product_type    = models.ForeignKey(product_type, verbose_name='Тип продукта', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_price(self):
        if self.sale:
            if 0 < self.sale < 100:
                return round(self.price - (self.price * (self.sale / 100)), 2)
            else:
                return 0
        else:
            return self.price

    def get_rate(self):
        if self.comment_set.all():
            result = [a.rate for a in self.comment_set.all()]
            return self.comment_set.all().rate / self.comment_set.count()
    
    def was_bought(self, amount):
        if self.on_stock >= amount:
            self.on_stock -= amount
            if self.on_stock == 0:
                self.avalible = False
        else: raise ValueError

        


class thumbnail(models.Model):
    product = models.ForeignKey(product, verbose_name='Продукт', on_delete=models.CASCADE)
    image   = models.ImageField('Изображение', upload_to='thumbnail')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.product


class paramether(models.Model):
    name = models.CharField('Название', max_length=50)
    units = models.CharField('Еденицы измерения', max_length=10)
    
    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'

    def __str__(self):
        return self.name


class characteristic(models.Model):
    product = models.ForeignKey(product, verbose_name='Продукт', on_delete=models.CASCADE)
    paramether = models.ForeignKey(paramether, verbose_name='Параметр', on_delete=models.CASCADE)
    value   = models.CharField('Значение параметра', max_length=150)

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return str(self.value)


class comment(models.Model):
    product = models.ForeignKey(product, verbose_name='Продукт', on_delete=models.CASCADE)
    author  = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    text    = models.CharField('Текст комментария', max_length=150)
    date    = models.DateField('Дата оставления заказа', auto_now=True)
    rate    = models.SmallIntegerField('Оценка')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return str(self.product)

    def get_star_bright(self):
        return range(self.rate)

    def get_star_dusk(self):
        return range(5 - self.rate)