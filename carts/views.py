from django.shortcuts import render, redirect, get_object_or_404


from store.models import Product, Variation
from .models import Cart, CartItem

# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)  #ürünü al
    product_variation = []
    if request.method == "POST":
        for item in request.POST:
            key = item               #key color  ,   item renk türü (black,white..)
            value = request.POST[key]

            try:  #ürün içindeki varvasyonları(renk,boyut) al
                variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                product_variation.append(variation)
            except:
                pass

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    #cart_item'ın var olup olmadığını kontrol ediyoruz, varsa if ile getir  yoksa else ile oluştur
    is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
    if is_cart_item_exists:
        #filter yaparak her farklı ürün eklediğinde gruplamalı filtre yapıyoruz
        cart_item = CartItem.objects.filter(product=product, cart=cart)
        #1 existing_variations -> db'den
        #2 current variation -> product_variation'dan
        #3 item_id -> db'den
        ex_var_list = []  #boş liste oluştur doldurcaz bunu
        id = []
        for item in cart_item:
            existing_variation = item.variations.all()  #CartItem modeli variations vt
            ex_var_list.append(list(existing_variation))
            id.append(item.id)

        print(ex_var_list)

        if product_variation in ex_var_list:
           #cartitemler varvasyonlar farklıysa grupla
           index = ex_var_list.index(product_variation)
           item_id = id[index]
           item = CartItem.objects.get(product=product, id=item_id)
           item.quantity += 1
           item.save()
#yeni varvasyon oluştur, varvasyonları aynıysa her cartitem eklediğinde aynı cartiteme atsın
        else:
           item = CartItem.objects.create(product=product, quantity=1, cart=cart)
           if len(product_variation) > 0:
               item.variations.clear()
               item.variations.add(*product_variation)
           item.save()
#caritem ekle
    else:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        if len(product_variation) > 0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variation)
        cart_item.save()
    return redirect ("cart")


def remove_cart(request, product_id, cart_item_id):  #stok eksiltme ve 0 ise ürünü kartdan silme
    cart      = Cart.objects.get(cart_id=_cart_id(request))
    product   = get_object_or_404(Product, id=product_id)
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect("cart")

def remove_cart_item(request, product_id, cart_item_id):  #ürünü kartdan silme
    cart      = Cart.objects.get(cart_id=_cart_id(request))
    product   = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect("cart")


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax
    except ObjectNotExist:
        pass #nesne yoksa yoksay

    context = {
        "total"      : total,
        "quantity"   : quantity,
        "cart_items" : cart_items,
        "tax"        : tax,
        "grand_total": grand_total,
    }
    return render(request, "store/cart.html", context)
