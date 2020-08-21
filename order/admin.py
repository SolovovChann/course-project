from django.contrib import admin
from .models import order, order_product


@admin.register(order)
class AdminTable(admin.ModelAdmin):
    list_display = ('fio', 'total', 'address', 'post_code', 'date')