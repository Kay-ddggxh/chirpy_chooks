from django.shortcuts import render
from .models import Product, Category


def all_products(request):
    """
    Renders all poultry procucts
    """
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'products/products.html', context)
