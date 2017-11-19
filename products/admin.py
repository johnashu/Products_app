from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('p_name', 'description', 'category', 'price', 'quantity')
    #fields = ['p_name', 'description', 'category', ('quantity', 'price'),  'featured_image']
    fieldsets = (
        (None, {
            'fields': ('p_name', 'description', 'category')
        }),
        ('Amounts', {
            'fields':  ('quantity', 'price')
        }),
        ('Image URL', {
            'fields':  ('featured_image', )
        }),
    )
    list_filter = ('quantity', 'category', 'p_name', 'price')

  

admin.site.register(Product, ProductAdmin)