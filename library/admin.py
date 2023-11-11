from django.contrib import admin
from .models import *
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'second_name']
    list_filter = ['name']

class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['title']
    prepopulated_fields = {"slug": ("title",)}

class RatingAdmin(admin.ModelAdmin):
    list_display = ['star', 'book', 'ip']
    list_filter = ['star']

class RatingStarAdmin(admin.ModelAdmin):
    list_display = ['value']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(RatingStar, RatingStarAdmin)