from django import template
from django.urls import reverse

from doanthoitrang import settings
from order.models import ShopCart
from product.models import *

register = template.Library()

@register.simple_tag
def shopcartcount(userid):
    count = ShopCart.objects.filter(user_id=userid).count()
    return count

@register.simple_tag
def shopcarttotal(userid):
    shopcart = ShopCart.objects.filter(user_id = userid)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    return total

@register.simple_tag
def categorytag(self):
    category = Category.objects.all()
    return category
    
@register.simple_tag
def trademarktag(self):
    trademark = TradeMark.objects.all()
    return trademark    
    
    