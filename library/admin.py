from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'second_name']
    list_filter = ['name']

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['title']
    prepopulated_fields = {"slug": ("title",)}

@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'rating', 'create_at']
    list_filter = ['create_at']
