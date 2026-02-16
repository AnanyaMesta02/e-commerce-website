from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product': product})
from django.shortcuts import redirect

def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    print("Before:", cart)

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session['cart'] = cart
    print("After:", cart)

    return redirect('product_list')


def cart_view(request):
    cart = request.session.get('cart', {})
    print("SESSION CART:", cart)

    product_ids = [int(id) for id in cart.keys()]
    print("PRODUCT IDS:", product_ids)

    products = Product.objects.filter(id__in=product_ids)
    print("PRODUCTS FOUND:", products)

    cart_items = []
    total = 0

    for product in products:
        quantity = cart[str(product.id)]
        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

from django.shortcuts import redirect

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        del cart[str(id)]

    request.session['cart'] = cart
    return redirect('cart')
