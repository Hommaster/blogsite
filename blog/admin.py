from django.contrib import admin

from .models import Post, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'status', 'publish']
    list_filter = ['status', 'publish', 'author', 'create']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'email', 'text', 'active', 'created']
    list_filter = ['active', 'created', 'update']
    search_fields = ['name', 'post', 'text']
