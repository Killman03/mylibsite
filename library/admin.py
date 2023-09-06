from django.contrib import admin
from .models import Author, Books
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'second_name']
    list_filter = ['name']

admin.site.register(Author)
admin.site.register(Books)