from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Category, Product

class NewCategoryForm(forms.Form):
    c_name = forms.CharField(help_text="Enter A New Product Category...", required=True)

    def clean_renewal_date(self):
        data = self.cleaned_data['c_name']
 
        # Remember to always return the cleaned data.
        return data    