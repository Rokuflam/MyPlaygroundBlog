from django.contrib import admin
from .models import Author, Tag, Post, Comment


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'date', 'tags')
    list_display = ('title', 'date', 'author')
    
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post')
    