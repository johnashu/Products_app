from django.db import models
from django.urls import reverse

class Category(models.Model):
    """
    Model For a product category
    """

    c_name = models.CharField(max_length=200, help_text="Enter a Product Category: ")


    def __str__(self):
        """
        String Representation for the Model object
        """
        return self.c_name

    def get_absolute_url(self):
        """
        Return an absolute URL to access a category instance
        """
        return reverse('categories', args=[str(self.id)])    

class Product(models.Model):
    p_name = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
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

    
