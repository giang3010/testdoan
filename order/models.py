from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count

# Create your models here.
from django.forms import ModelForm, TextInput

from product.models import *



class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    variant = models.ForeignKey(Variants,on_delete=models.SET_NULL, blank= True,null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        return (self.product.price)

    @property
    def amount(self):
        return (self.quantity * self.product.price)

    @property
    def varamount(self):
        return (self.quantity * self.variant.price)



class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']
        widgets = {
            'quantity' : TextInput(attrs={'class':'input', 'type':'number','value':'1'}),
        }

class Order(models.Model):
    STATUS = (
        ('Mới', 'Mới'),
        ('Đã xác nhận', 'Đã xác nhận'),
        ('Chuẩn bị giao', 'Chuẩn bị giao'),
        ('Đang vận chuyển', 'Đang vận chuyển'),
        ('Hoàn thành', 'Hoàn thành'),
        ('Hủy', 'Hủy'),
    )
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    code = models.CharField(max_length= 5, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length= 12, blank=True)
    address = models.CharField(max_length= 100, blank=True)
    district = models.CharField(max_length= 30, blank=True)
    city = models.CharField(max_length= 30, blank=True)
    # 
    total = models.DecimalField(default = 0,max_digits=100,decimal_places=0)
    shiper = models.CharField(max_length= 50, blank=True)
    note = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS, default='Mới')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.last_name



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','phone','address','district','city',]


class OrderProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variants, on_delete=models.SET_NULL,blank=True, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(default = 0,max_digits=100,decimal_places=0)
    total = models.DecimalField(default = 0,max_digits=100,decimal_places=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title