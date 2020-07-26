from django.contrib import admin
from user.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'phone','address','city','image_tag')


class WardInLine(admin.TabularInline):
    model = Ward
    readonly_fields=('id',)
    extra = 1


class DistrictInLine(admin.TabularInline):
    model = District
    readonly_fields=('id',)
    extra = 1

class WardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    inlines = [WardInLine,]

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    inlines = [DistrictInLine,]

@admin.register(City, District, Ward)
class ViewAdmin(ImportExportModelAdmin):
    pass

admin.site.register(UserProfile,UserProfileAdmin)

# admin.site.register(City,CityAdmin)
# admin.site.register(District,DistrictAdmin)
# admin.site.register(Ward,WardAdmin)