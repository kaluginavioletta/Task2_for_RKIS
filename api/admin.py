from django.contrib import admin

from .models import Author, Book, Cover, Genre, Category

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Cover)
admin.site.register(Genre)
admin.site.register(Category)
