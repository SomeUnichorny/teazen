from .models import OrderItem

def cart_item_count(request):
    if request.user.is_authenticated:
        cart_items_count = OrderItem.get_cart_items_count(request.user)
    else:
        cart_items_count = 0
    return {'cart_items_count': cart_items_count}