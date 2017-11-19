
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
]

urlpatterns += [
    url(r'^products/', include('products.urls'), name='products'),
    url(r'^accounts/', include('accounts.urls'), name='accounts'),
]

urlpatterns += [
    url(r'^$', RedirectView.as_view(url='/products/', permanent=True)),
]
