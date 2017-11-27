
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .filters import CategoryFilter

from .models import Category

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


def search(request):
    cat_list = Category.objects.all()
    cat_filter = CategoryFilter(request.GET, queryset=cat_list)
    return render(request, 'cat_s_list.html', {'filter': cat_filter})