from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is currently empty.")
        return redirect(reverse('categories'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MLQrhIlP7xhfz97VLJrReFxSD2P5fWdPNYB6BaQueWxn3HnWQUtfOT367lpGHQVNndPSQ6Ir7W97WtrRjZjIYQg00CMi4MnAX',  # noqa
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
