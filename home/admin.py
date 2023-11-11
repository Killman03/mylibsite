from django.contrib import admin

from .models import Setting, ContactMessage, Events


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'update_at', 'status']
    list_filter = ['title']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'update_at', 'status']
    list_filter = ['status']
    readonly_fields = ('name', 'update_at', 'subject', 'your_email', 'your_message', 'ip')

class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'update_at', 'status']
    list_filter = ['status']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Setting, SettingAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Events, EventsAdmin)

# Register your models here.
