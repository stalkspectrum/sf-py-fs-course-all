from django.contrib import admin

# Register your models here.
from p_library.models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
