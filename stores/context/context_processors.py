from stores.models import RetailStores, CartItems

def retailstore_renderer(store_id):
    try:
        store_obj = RetailStores.objects.get(id=store_id)
    except RetailStores.DoesNotExist:
        store_obj = None

    return {'store_obj': store_obj}

def cart_renderer(request):
    session = str(request.META.get('HTTP_COOKIE')).removeprefix('csrftoken=')
    cart_items = CartItems.objects.filter(order__session_id=session).all()
    cart = cart_items.count()
    
    return {'cart': cart}