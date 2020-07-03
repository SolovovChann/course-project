from decimal                import Decimal
from django.conf            import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db              import models
import math

PRODUCT_TYPE = (
    ('gamepad' , 'Контроллеры'),
    ('accessory'  , 'Аксессуары'),
    ('keyboard'   , 'Клавиатуры'),
    ('mouse'      , 'Мыши'),
    ('headset'    , 'Гарнитуры'),
)


class product(models.Model):
    name     = models.CharField('Название', max_length=30, null=False, blank=False)
    price    = models.FloatField('Цена', null=False, blank=False)
    sale     = models.IntegerField('Скидка (указывать в процентах)', null=True, blank=True)
    image   = models.ImageField('Превью', upload_to='product', null=False, blank=False)
    on_stock = models.PositiveIntegerField('Доступно на складе')
    avalible = models.BooleanField('Доступно для покупки', default=bool(on_stock) )
    p_type   = models.CharField('Тип продукта', max_length=25, choices=PRODUCT_TYPE, null=True, blank=True)
    description = models.TextField('Описание', max_length=250, null=True, blank=True)

    def getSale(self):
        if self.sale:
            return round(self.price - (self.price * (self.sale / 100)), 0)
        else:
            return self.price
    def getRating(self):
        result = 0
        if self.comment_set.all():
            for a in self.comment_set.all():
                result += a.rate
            return math.ceil(result / self.comment_set.count()) * '🌝' + (5 - math.ceil(result / self.comment_set.count())) * '🌚'
        else:
            return 5 * '🌚'
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class reviews(models.Model):
    product     = models.ForeignKey(product, on_delete=models.CASCADE)
    image       = models.ImageField('Изображение', upload_to='product', null=False)

    def __str__(self):
        return self.product.name
    class Meta:
        verbose_name = 'Превью'
        verbose_name_plural = 'Превью'


class comment(models.Model):
    product     = models.ForeignKey(product, on_delete=models.CASCADE)
    rate        = models.PositiveIntegerField('Оценка', null=False, blank=False, validators=[MaxValueValidator(5)])
    authorName  = models.CharField('Имя автора', max_length=50)
    text        = models.TextField('Текст комментария')
    pubDate     = models.DateTimeField('Дата оставления комметнария', auto_now=True)
    likes       = models.PositiveIntegerField('Лайки', null=False, blank=False, default=0)
    dsilikes    = models.PositiveIntegerField('Дислайки', null=False, blank=False, default=0)

    def getCommentRating(self):
        result = self.likes - self.dsilikes
        return result

    def __str__(self):
        return self.authorName
    def getRate(self):
        return self.rate * '🌝' + (5 - self.rate) * '🌚'
        
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class characteristic(models.Model):
    product     = models.ForeignKey(product, on_delete=models.CASCADE)
    parameter   = models.CharField('Параметр', max_length=50)
    value       = models.CharField('Значение', max_length=120)

    class Meta:
        verbose_name = ('Характеристика')
        verbose_name_plural = ('Характеристики')

    def __str__(self):
        return self.name