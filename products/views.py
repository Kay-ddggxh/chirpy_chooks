from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def all_categories(request):
    """
    Renders all poultry procucts
    """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'products/categories.html', context)


def products(request):
    """
    Renders all products of same category
    """
    products = Product.objects.all()
    category_select = request.GET['category']

    if request.GET:
        if 'category' in request.GET:
            category_select = request.GET['category']
            products = products.filter(category__name=category_select)

    context = {
        'products': products,
        'current_category': category_select,
    }

    return render(request, 'products/products.html', context)


# Source code: Code Institute Boutique Ado walkthrough https://github.com/Kathrin-ddggxh/CI_boutique-ado/blob/main/products/views.py#:~:text=def%20product_detail(,%2C%20context)  # noqa
def product_detail(request, product_id):
    """
    Displays product details
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
