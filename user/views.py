from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, update_session_auth_hash
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
from product.models import Category
from order.models import *
from user.forms import *
from user.models import *

def _get_queryset(klass):
    if hasattr(klass, '_default_manager'):
        return klass._default_manager.all()
    return klass

def get_object_or_404(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    if not hasattr(queryset, 'get'):
        klass__name = klass.__name__ if isinstance(klass, type) else klass.__class__.__name__
        raise ValueError(
            "First argument to get_object_or_404() must be a Model, Manager, "
            "or QuerySet, not '%s'." % klass__name
        )
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        raise Http404('No %s matches the given query.' % queryset.model._meta.object_name)



@login_required(login_url='/login')
def orderdetail(request,id):
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    category = Category.objects.all()
    order = Order.objects.filter(user_id = current_user.id,id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    context ={
        'category' : category,
        'order' : order,
        'orderitems' : orderitems,
        'total' : total,
    }
    return render(request,'user_orders_detail.html',context)

@login_required(login_url='/login')
def deletefromorder(request, id):
    order = Order.objects.get(id=id )
    order.status = 'Hủy'
    order.save()
    messages.success(request,"Đã hủy đơn")
    return HttpResponseRedirect('/user/orders')

@login_required(login_url='/login')
def orders(request):
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    category = Category.objects.all()
    orders = Order.objects.filter(user_id = current_user.id).exclude(status = 'Hủy')
    context ={
        'category' : category,
        'orders' : orders,
        'total' : total,
    }
    return render(request,'user_orders.html',context)


@login_required(login_url='/login')
def user_password(request):
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    if request.method == "POST":
        form = ChangePassWord(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)           
            messages.success(request,'Thay đổi mật khẩu thành công')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request,'Không thể thay đổi mật khẩu')
            return HttpResponseRedirect('/user/change-password')
    else:
        category = Category.objects.all()
        form = ChangePassWord(request.user)
        return render(request,'user_password.html',{
            'form' : form,
            'category' : category,
            'total' : total,
        })

@login_required(login_url='/login')
def user_update(request):
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    profile = UserProfile.objects.get(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Cập nhật thông tin tài khoản thành công')
            return HttpResponseRedirect('/user')
        else:
            messages.warning(request,'Không thể thay đổi thông tin')
            return HttpResponseRedirect('/user/update/')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance = request.user.userprofile)
        context = {
            'category' : category,
            'user_form' : user_form,
            'profile_form' : profile_form,
            'total' : total,
            'profile' : profile,
        }
        return render(request,'user_update.html',context)


def user(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id = current_user.id)
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    context = {
        'category' : category,
        'profile' : profile,
        'total' : total,
    }
    return render(request,'user.html',context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate( username=username, password=password)
        if user is not None:
            auth.login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id = current_user.id)
            request.session['userimage'] = userprofile.image.url
            # Chuyen toi trang chu
            return HttpResponseRedirect('/')
        else:
            # Quay lai trang dang nhap voi thong bao
            messages.warning(request,"Thông tin tài khoản hoặc mật khẩu không chính xác!")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    context = {
        'category' : category,

    }
    
    return render(request,'login_form.html',context)


def logout(request):
    auth.logout(request)
    return redirect('/')
    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            auth_login(request, user)
            #đưa
        
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/user/user.png"
            data.save()
            messages.success(request, 'Tạo tài khoản thành công')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')
        
    form = SignUpForm()
    category = Category.objects.all()
    context = {
        'category' : category,
        'form': form,

    }
    return  render(request,'register_form.html',context)

