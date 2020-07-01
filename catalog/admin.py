from .models        import product, comment, reviews
from django.contrib import admin

admin.site.register(product)
admin.site.register(reviews)

@admin.register(comment)
class AdminTable(admin.ModelAdmin):
    list_display = ( 'product', 'rate', 'authorName', 'text', 'pubDate', 'likes', 'dsilikes' )