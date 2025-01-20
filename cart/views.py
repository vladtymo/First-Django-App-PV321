from django.shortcuts import redirect, render
from django.contrib import messages

from cart.cart import add_to_cart, clear_cart, get_cart_items
from users.models import User

def index(request):
    items = get_cart_items(request.session)

    users = User.objects.filter(id__in=items.keys())

    with_quantity = [{ **user.__dict__, 'quantity': items[str(user.id)]} for user in users]

    return render(request, 'cart/index.html', {'users': with_quantity})

def add(request, id):

    if User.objects.get(pk=id) is None:
        messages.error(request, 'User not found!')
        return redirect('/cart')

    add_to_cart(request.session, id)
    messages.success(request, 'User added to cart')

    return redirect('/cart')

def clear(request):
    clear_cart(request.session)
    return redirect('/cart')