from django.contrib import admin
from .models import Author, Category, Book, UserProfile


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    search_fields = ('title', 'author__name',)
    list_filter = ('author', 'categories',)
    raw_id_fields = ('author',)
    filter_horizontal = ('categories',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)
    filter_horizontal = ('favorite_books',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(UserProfile, UserProfileAdmin)