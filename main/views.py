# views.py

from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home_view(request):
    products = Product.objects.all()[:5]
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'portfolio/index.html', context)

def product_view(request, category_slug=None):
    categories = Category.objects.all()

    if category_slug:
        requested_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=requested_category)
    else:
        requested_category=None
        products=Product.objects.all()

    context = {'products': products, 'categories': categories, 'requested_category': requested_category}
    return render(request, 'portfolio/product_list.html', context)

def description_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'portfolio/product_detail.html', {'product': product})
