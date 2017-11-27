from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('p_name', 'description', 'price', 'quantity')
    #fields = ['p_name', 'description', 'category', ('quantity', 'price'),  'featured_image']
    fieldsets = (
        (None, {
            'fields': ('p_name', 'description', 'categories')
        }),
        ('Amounts', {
            'fields':  ('quantity', 'price')
        }),
        ('Image URL', {
            'fields':  ('featured_image', )
        }),
    )
    list_filter = ('quantity', 'categories', 'p_name', 'price')

  

admin.site.register(Product, ProductAdmin)