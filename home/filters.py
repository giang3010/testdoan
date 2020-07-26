from django import forms
from order.models import Order
import django_filters
from django_filters.widgets import DateRangeWidget
from product.models import Product, Variants

class ExportFilter(django_filters.FilterSet):
    create_at = django_filters.DateFilter(field_name='create_at', label='Chọn Tháng Ban Muốn Thống Kê'),
    create_at_gte = django_filters.DateFilter(field_name='update_date',name='update_date_gte', lookup_type='gte', label='Date minimale'),
    create_at_lte = django_filters.DateFilter(field_name='update_date',name='update_date_lte', lookup_type='lte', label='Date maximale'),
    status = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Order
        fields = {
            'create_at': ['gte', 'lte'],
            'status' :[]
        }

class ExportProductFilter(django_filters.FilterSet):
    quantity = django_filters.NumberFilter(field_name='quantity',lookup_type='lte', label='Số Lượng Tồn'),
    quantity_lte = django_filters.NumberFilter(field_name='quantity',name='quantity_lte',lookup_type='lte', label='Số Lượng Tồn'),
    class Meta:
        model = Variants
        fields = {
            'quantity': ['lte'],
        }


        