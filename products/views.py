
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Product

from categories.models import Category

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

  
class ProductListView(generic.ListView):
    model = Product
    paginate_by = 2
    template_name = 'product_list.html'
    ordering = '-price'

    def get_object(self):
        return get_object_or_404(self.model, pk=self.kwargs['pk'])    



class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'
    paginate_by = 2

    def get_object(self):
        return get_object_or_404(Product, pk=self.kwargs.get('pk'))

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context    

@method_decorator(login_required, name='dispatch')
class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')
    template_name = 'product_form.html'


@method_decorator(login_required, name='dispatch')
class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')
    template_name = 'product_update.html'


@method_decorator(login_required, name='dispatch')
class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products')
    template_name = 'product_delete.html'


def index(request):
    """
    View for the Homepage
    """
    num_products = Product.objects.all().count()
    num_cat = Category.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_products': num_products,
                 'num_cat': num_cat, 'num_visits': num_visits},
    )


