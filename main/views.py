# views.py

from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

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

def about_us(request):
    #about_us page
    return render(request, 'portfolio/about_us.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('main:contactus')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact_us.html', {'form': form})

def privacy (request):
    #privacy page
    return render(request,'portfolio/terms.html')

def terms (request):
    #Request page
    return render(request,'portfolio/privacy.html')
