CART_KEY = 'products-cart'

def add_to_cart(session, id):
    cart = session.get(CART_KEY, {})

    if id not in cart:
        cart[id] = 1
    else:
        cart[id] += 1

    session[CART_KEY] = cart
    
def get_cart_items(session):
    return session.get(CART_KEY, {})

def get_cart_size(session):
    return len(get_cart_items(session))

def clear_cart(session):
    session[CART_KEY] = {}