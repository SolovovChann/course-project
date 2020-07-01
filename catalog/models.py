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
    review   = models.ImageField('Превью', upload_to='product', null=False, blank=False)
    on_stock = models.PositiveIntegerField('Доступно на складе')
    avalible = models.BooleanField('Доступно для покупки', default=bool(on_stock) )
    p_type   = models.CharField('Тип продукта', max_length=25, choices=PRODUCT_TYPE, null=True, blank=True)
    description = models.TextField('Описание', max_length=250, null=True, blank=True)

    def getSale(self):
        if 0 < self.sale < 101:
            return round(self.price - (self.price * (self.sale / 100)), 0)
        else:
            return 'Ошибка! Неверно указана скидка!'
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


class cart(object):
    def __init__(self, request):
        """
        Инициализируем корзину
        """

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            #   Save an empty cart in a session
            cart = self.session[ settings.CART_SESSION_ID ] = {}
            
        self.cart = cart


    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину по его ID
        """
        productId = str(product.id)

        if productId not in self.cart:
            self.cart[productId] = {
                'quantity'    : 0,
                'price'       : product.price
            }
        
        if update_quantity:
            self.cart[productId]['quantity'] = quantity
        else:
            self.cart[productId]['quantity'] += quantity
        self.save()

    
    def save(self):
        #   Cart session update
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    def remove(self, product):
        """
        Удаление товара из корзины
        """

        if str(product.id) in self.cart:
            del self.cart[ str( product.id )]
            self.save()


    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из БД
        """

        product_ids = self.cart.keys()
        #   get products
        products = product.objects.filter( id__in=product_ids )
        for Product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['quantity']
            yield item


    def __len__(self):
        """
        Подсчёт всех товаров в корзине
        """
        return sum( item['quantity'] for item in self.cart.values())


    
    def get_total_price(self):
        return sum( Decimal( item['price'] * item['quantity'] for item in self.cart.values()))


    def clear(self):
        del self.session[ settings.CART_SESSION_ID]
        self.session.modified = True