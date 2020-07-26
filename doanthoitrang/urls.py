"""doanthoitrang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from doanthoitrang import settings
from product.admin import event_admin_site
from django.contrib.auth import views as auth_views

from home import views
from order import views as OrderViews
from user import views as UserViews

urlpatterns = [
    path('',include('home.urls'),name = 'base'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('product/',include('product.urls')),

    path('order/',include('order.urls')),

    path('user/',include('user.urls')),
    
    path('shop/', views.shop, name = "shop"),
    path('shop/<int:id>/<slug:slug>',views.shop_products, name='shop_products'),
    path('category/<int:id>/<slug:slug>',views.category_products, name='category_products'),

    path('chart/',views.chart, name='chart'),
    path('chart2/',views.chart_2, name='chart2'),
    path('test/',views.export_users_xls, name='test'),
    path('report/',views.report, name='report'),
    path('report_products/',views.report_products, name='report_products'),

    
    path('trademark/<int:id>',views.trademark, name='trademark'),

    # path('search/',views.product_search, name='product_search'),
    path('search/', views.search, name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),

    # path('search/',views.search, name='search'),
    path('product/<int:id>/<slug:slug>/',views.product_detail, name='product_detail'),
    
    #order
    path('order/orderproduct/', OrderViews.orderproduct, name = "orderproduct"),
    path('shopcart/', OrderViews.shopcart, name = "cart"),
    path('ajaxcolor/',views.ajaxcolor, name='ajaxcolor'),

    #user
    path('login/', UserViews.login, name = "login"),
    path('signup/', UserViews.signup, name = "signup"),
    path('logout/', UserViews.logout, name = "logout"),

    #reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
     name='password_reset_confirm'),
    
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
     name='password_reset_complete'),

    path('admin/', admin.site.urls),
    path('event-admin/', event_admin_site.urls),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
