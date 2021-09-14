from django.urls import path, re_path
from django.conf.urls import url
from .views import catalog_page
from . import views

urlpatterns = [
    path("",catalog_page, name="catalog_page"),
    #path("catalog/",views.product_list, name='product_list'),
    re_path(r'^$', views.product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]


