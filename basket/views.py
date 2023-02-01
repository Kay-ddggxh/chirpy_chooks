from django.shortcuts import render


def basket(request):
    """
    renders shopping basket
    """
    return render(request, 'basket/basket.html')
