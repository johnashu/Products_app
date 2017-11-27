from django.db import models
from django.urls import reverse

from categories.models import Category

class Product(models.Model):
    p_name = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category, blank=True)
    quantity = models.PositiveIntegerField()
    featured_image = models.CharField(max_length=300)

    def __str__(self):
        """
        String Representation for the Model object
        """
        return str(self.p_name) + str(self.price)
        
    def get_absolute_url(self):
        """
        Return an absolute URL to access a product instance
        """
        return reverse('products', args=[str(self.id)])  

    class Meta:
        ordering = ('price',)

    
