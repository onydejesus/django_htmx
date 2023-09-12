from django.contrib import admin
from .models import Author, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'number_of_pages')


class BookInLineAdmin(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInLineAdmin]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)