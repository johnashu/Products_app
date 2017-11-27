from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^products/$', views.ProductListView.as_view(), name='products'),
    url(r'^products/(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product-detail'),

    url(r'^products/create/$', views.ProductCreate.as_view(), name='product-create'),
    url(r'^products/(?P<pk>\d+)/update/$', views.ProductUpdate.as_view(), name='product-update'),
    url(r'^products/(?P<pk>\d+)/delete/$', views.ProductDelete.as_view(), name='product-delete'),

    ]
