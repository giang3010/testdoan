from django.contrib import admin
from .models import *
from mptt.admin import DraggableMPTTAdmin
from django.contrib.admin import AdminSite
import admin_thumbnails
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent','status','create_at')
    list_filter = ('parent','status','create_at')

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        
        qs = Category.objects.add_related_count(
                 qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

@admin_thumbnails.thumbnail('image')
class ProductImageInLine(admin.TabularInline):
    model = Images
    readonly_fields=('id',)
    extra = 1

class ProductVariantsInLine(admin.TabularInline):
    model = Variants
    readonly_fields=('image_tag',)
    extra = 1
    show_change_link = True

def make_status_true(modeladmin, request, queryset):
    queryset.update(status='True')

def make_status_false(modeladmin, request, queryset):
    queryset.update(status='False')

make_status_true.short_description = 'Update status to True'
make_status_false.short_description = 'Update status to False'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment','product', 'status','create_at']
    list_filter = ['status','rate']
    readonly_fields = ('comment','user','product','rate')
    actions = [make_status_true,make_status_false]

@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'title','image_thumbnail')

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount','price','create_at','image_tag']
    list_filter = ['status','create_at','category',]
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInLine,ProductVariantsInLine]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title',]




class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'code','color_tag')

class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

class VariantsAdmin(admin.ModelAdmin):
    list_display = ('title', 'product','color','size','price','quantity','image_tag')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','create_at','timeend' )




admin.site.register(Comment,CommentAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Variants,VariantsAdmin)
admin.site.register(Category,CategoryAdmin2)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(TradeMark)






class EventAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"

event_admin_site = EventAdminSite(name='event_admin')


event_admin_site.register(Category,CategoryAdmin2)
event_admin_site.register(Product,ProductAdmin)
event_admin_site.register(Images,ImagesAdmin)
event_admin_site.register(News)

