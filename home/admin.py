from django.contrib import admin

# Register your models here.
from .models import ContactMessage, Subscribe


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone','status','create_at','note')
    list_filter = ('status','create_at')
    readonly_fields = ('name','email', 'phone','message','ip','create_at')

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(ContactMessage,ContactMessageAdmin)
admin.site.register(Subscribe,SubscribeAdmin)