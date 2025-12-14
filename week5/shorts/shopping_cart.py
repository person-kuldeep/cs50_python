def checkout(cart_items, discount=None):
    total = sum(item['price'] for item in cart_items)
    if discount == "HALO20":
        total = total * 0.8

    return round(total, 2)


"""
what to test for checkout function

1. no discount
2. HALO20 discount
3. invalid discount
4. empty cart

"""