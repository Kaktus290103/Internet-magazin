"""webmagazin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from webmagazin.catalog.views import product_list
#from webmagazin import catalog
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import include, url
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from catalog import views

urlpatterns = [
    path('home/',include("home.urls")),
    re_path(r'^admin/', admin.site.urls),
    path('catalog/',views.product_list, name='catalog_page'),
    re_path(r'^catalog/', include(('catalog.urls', 'catalog'), namespace='catalog')),  
    path("", lambda request: redirect("/home/")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

