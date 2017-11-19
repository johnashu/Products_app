
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Category, Product

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 5
    template_name = 'category_list.html'
    ordering = 'c_name'


class CategoryDetailView(generic.DetailView):
    template_name = 'category_detail.html'
    paginate_by = 2
    model = Category

    def get_object(self):
        return get_object_or_404(Category, pk=self.kwargs.get('pk'))

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        context['products'] = self.get_object().products.all()
        return context
   

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
class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('categories')
    template_name = 'category_form.html'


@method_decorator(login_required, name='dispatch')
class CategoryUpdate(UpdateView):
    model = Category
    fields = ['c_name']
    success_url = reverse_lazy('categories')
    template_name = 'category_update.html'


@method_decorator(login_required, name='dispatch')
class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('categories')
    template_name = 'category_delete.html'


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


from .filters import CategoryFilter

def search(request):
    cat_list = Category.objects.all()
    cat_filter = CategoryFilter(request.GET, queryset=cat_list)
    return render(request, 'cat_s_list.html', {'filter': cat_filter})