from django.shortcuts import render, redirect, reverse

def view_cart(request):
    ''' Display contents of the cart '''
    return render(request, 'cart.html')


def add_to_cart(request, id):
    ''' Add product to the cart '''
    cart = {}
    cart[id] = cart.get(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_cart(request, id):
    ''' Remove a product from the cart '''
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
