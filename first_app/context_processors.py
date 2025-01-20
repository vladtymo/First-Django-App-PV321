from cart.cart import get_cart_size

def cart_count(request):
    return {'cart_count': get_cart_size(request.session)}