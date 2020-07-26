from django.contrib import admin

# Register your models here.
from order.models import *


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ('product', 'user','quantity','price','amount')
    list_filter = ('user',)

class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product','quantity','price','total')
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('code','first_name','last_name','phone','address','district','city','total','status',)
    list_filter = ('status','user',)
    readonly_fields = ('user','phone','address','district','city','last_name','total','first_name',)
    can_delete = False
    inlines = [OrderProductline]
    search_fields = ['code',]

    
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product','quantity','price','total')
    list_filter = ('user',)

admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)