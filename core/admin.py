from django.contrib import admin
from .models import Book,IssuedBook

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['name', 'category', 'author', 'isbn']
admin.site.register(Book, BookAdmin)

class IssuedBookAdmin(admin.ModelAdmin):
    model = IssuedBook
    list_display = ['student', 'book', 'expirydate']
    
admin.site.register(IssuedBook, IssuedBookAdmin)