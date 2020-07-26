from django.urls import path
from . import views

urlpatterns = [
    path('',views.base, name = 'base'),
    path('blank/', views.blank, name = "blank"),
    path('contact/',views.contact, name = 'contact'),
    path('sub/',views.email_list_signup, name = 'sub'),
    # path('unsub/',views.unsubscribe, name = 'unsub'),
    path('order/addtoshopcart/<int:id>', views.addtoshopcart, name = "addtoshopcart"),
    path('order/deletefromcart/<int:id>', views.deletefromcart, name = "deletefromcart"),
    path('order/delete_single_item_from_cart/<int:id>', views.delete_single_item_from_cart, name = "delete_single_item_from_cart"),
    path('order/add_single_item_from_cart/<int:id>', views.add_single_item_from_cart, name = "add_single_item_from_cart"),
    
    
]