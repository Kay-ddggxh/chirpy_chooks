from decimal import Decimal
from django.conf import settings


# Source code with variation: https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/9c2aa64f4edffb25e330d722ee66542e553edb80/bag/contexts.py  # noqa
def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    delivery = 0
    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
