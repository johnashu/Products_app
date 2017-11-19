from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^products/$', views.ProductListView.as_view(), name='products'),
    url(r'^products/(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product-detail'),

    url(r'^categories/$', views.CategoryListView.as_view(), name='categories'),
    url(r'^categories/(?P<pk>\d+)/$', views.CategoryDetailView.as_view(), name='category-detail'),
    
    url(r'^categories/create/$', views.CategoryCreate.as_view(), name='category-create'),
    url(r'^categories/(?P<pk>\d+)/update/$', views.CategoryUpdate.as_view(), name='category-update'),
    url(r'^categories/(?P<pk>\d+)/delete/$', views.CategoryDelete.as_view(), name='category-delete'),

    url(r'^products/create/$', views.ProductCreate.as_view(), name='product-create'),
    url(r'^products/(?P<pk>\d+)/update/$', views.ProductUpdate.as_view(), name='product-update'),
    url(r'^products/(?P<pk>\d+)/delete/$', views.ProductDelete.as_view(), name='product-delete'),

    url(r'^search/$', views.search, name='search'),
    

    ]
