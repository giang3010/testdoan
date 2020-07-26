from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
# Create your views here.
from product.models import *
from order.models import *
from user.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
import json as simplejson 

def index(request):
    return HttpResponse("This is my order site")

def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    context = {
        'category' : category,
        'shopcart': shopcart,
        'total': total,

    }
    return render(request,'cart.html',context)


@login_required(login_url='/login')
def orderproduct(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    citys = City.objects.all()

    wards = Ward.objects.all()
    districts = District.objects.all()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        
        if form.is_valid():
            # c = City.objects.get(id=form.cleaned_data['city'])
            # d = District.objects.get(id=form.cleaned_data['district'])
            
            
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.address = form.cleaned_data['address']
            # data.city = c.name
            # data.district = d.name
            data.district = form.cleaned_data['district']
            data.city = form.cleaned_data['city']
            
            data.user_id = current_user.id
            data.total = total
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()

            #chuyen item trong shopcart vao orderproduct
            
            for rs in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity          
                # if rs.product.variant == 'None':
                #     detail.price    = rs.product.price
                # else:
                detail.price = rs.variant.price
                detail.variant_id   = rs.variant_id
                detail.total = rs.amount
                detail.save()
                #giam so luong san pham trong Product
                # if  rs.product.variant=='None':
                #     product = Product.objects.get(id=rs.product_id)
                #     product.amount -= rs.quantity
                #     product.save()
                # else:
                variant = Variants.objects.get(id=rs.variant_id)
                variant.quantity -= rs.quantity
                variant.save()
            #xoa gio hang sau khi da order
            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items'] = 0
            return render(request,'order_completed.html',{
                'ordercode' : ordercode,
                'category' : category,
            })
        else:

            messages.warning(request, 'Đặt hàng thất bại! hãy kiểm tra lại thông tin')
            return HttpResponseRedirect("/order/orderproduct")
    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'shopcart' : shopcart,
        'category' : category,
        'total' : total,
        'profile' : profile,
        'form' : form,
        'citys' : citys,
        'wards' : wards,
        'districts' : districts,
    }
    return render(request,'order_form.html',context)