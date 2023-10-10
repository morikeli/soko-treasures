from stores.models import RetailStores

def retailstore_renderer(store_id):
    try:
        store_obj = RetailStores.objects.get(id=store_id)
    except RetailStores.DoesNotExist:
        store_obj = None

    return {'store_obj': store_obj}