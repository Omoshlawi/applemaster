from .cart import Cart
from .cart_wish import CartWish
from .wish_list import WishList


def wish_cart(request):
    return {'cart_wish': CartWish(request)}
