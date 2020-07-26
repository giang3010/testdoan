from django.urls import path
from . import views

urlpatterns = [
    path('',views.user, name = 'user'),
    path('update/',views.user_update, name = 'user_update'),
    path('change-password/',views.user_password, name = 'change-password'),
    path('password/',views.user_password, name = 'change-password'),
    path('orders/',views.orders, name = 'orders'),
    path('orderdetail/<int:id>',views.orderdetail, name = 'orderdetail'),
    path('deletefromorder/<int:id>', views.deletefromorder, name = "deletefromorder"),
]