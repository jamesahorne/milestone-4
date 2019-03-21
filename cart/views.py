from django.shortcuts import render, redirect, reverse

def view_cart(request):
    ''' Cart contents page '''
    return render(request, 'cart.html')


def add_to_cart(request, id):
    ''' Add product (and quantity) to cart '''
    quantity=int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return redirect(reverse('products'))


def edit_cart(request, id):
    ''' Edit quantity of a product in the cart '''
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
