from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category

def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    return render(request, 'catalog/contacts.html')


def index(request):
    return render(request, 'catalog/base.html')


def products(request):
    product_list = Product.objects.all()
    context = {'products': product_list}
    return render(request, 'catalog/products.html', context)


def product_info(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_info.html', context)

