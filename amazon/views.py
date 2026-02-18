from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist
from django.contrib.auth.decorators import login_required



@login_required
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

    messages.success(request, "Item added to cart successfully 🛒")


    return redirect('product_list')


@login_required
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
    messages.warning(request, "Item removed from cart ❌")

    return redirect('cart')

def increase_quantity(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] += 1

    request.session['cart'] = cart
    return redirect('cart')


def decrease_quantity(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] -= 1

        if cart[str(id)] <= 0:
            del cart[str(id)]

    request.session['cart'] = cart
    return redirect('cart')

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'store/register.html', {'form': form})

from .models import Order, OrderItem
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('cart')

    order = Order.objects.create(user=request.user)

    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity
        )
        total += product.price * quantity

    order.total_price = total
    order.save()
    messages.success(request, "Order placed successfully 🎉")

    request.session['cart'] = {}

    return render(request, 'store/order_success.html', {'order': order})

@login_required
def add_to_wishlist(request, id):
    product = Product.objects.get(id=id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    messages.success(request, "Added to wishlist ❤️")
    return redirect('product_list')


@login_required
def wishlist_view(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, 'store/wishlist.html', {'items': items})


@login_required
def remove_from_wishlist(request, id):
    product = Product.objects.get(id=id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    messages.warning(request, "Removed from wishlist")
    return redirect('wishlist')
