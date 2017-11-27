from django.db import models
from django.urls import reverse

class Category(models.Model):
    """
    Model For a product category
    """
    categories = models.ManyToManyField('self', blank=True)
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

        class Meta:
            ordering = ('c_name',)