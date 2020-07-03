from .models        import order
from django.contrib import admin

@admin.register(order)
class AdminTable(admin.ModelAdmin):
    filter_horizontal = ('cart', )
    list_display = ( 'fio', 'pubDate', 'total', 'phone', 'email', 'address' )