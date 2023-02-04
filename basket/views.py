from django.shortcuts import render, redirect


def basket(request):
    """
    renders shopping basket
    """
    return render(request, 'basket/basket.html')


# Source code: https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/21e3b111100f5c8daa4bc6e9565bde09980b33d8/bag/views.py#:~:text=def%20add_to_bag(,(redirect_url)  # noqa
def add_to_basket(request, item_id):
    """
    allows items to be added to basket
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)
