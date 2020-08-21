from django.contrib import admin
from .models import product, comment, characteristic, paramether, thumbnail, product_type


admin.site.register(thumbnail)

admin.site.register(product_type)

@admin.register(product)
class AdminTable(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'sale', 'on_stock', 'avalible', 'product_type')


@admin.register(comment)
class AdminTable(admin.ModelAdmin):
    list_display = ('product', 'author', 'text', 'date', 'rate')


@admin.register(characteristic)
class AdminTable(admin.ModelAdmin):
    list_display = ('product', 'paramether', 'value')


@admin.register(paramether)
class AdminTable(admin.ModelAdmin):
    list_display = ('name', 'units')