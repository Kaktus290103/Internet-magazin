from typing import Any
from django.shortcuts import render, get_object_or_404
from .models import Category, Tovary

def catalog_page(request):
    return render(request, "catalog.html")

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Tovary.objects.filter(colsklad=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  './catalog.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Tovary,
                                id=id,
                                slug=slug,
                                colsklad=True)
    return render(request,
                  './catalog.html',
                  {'product': product})