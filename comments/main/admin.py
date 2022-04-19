from django.contrib import admin
from .models import Post, Comment


admin.register(Post)
admin.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post',)
    search_fields = ('id', 'post',)
    list_filter = ('post',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'post',)
    search_fields = ('id', 'parent', 'text',  'post',)
    list_filter = ('parent', 'text',  'post',)
    empty_value_display = '-пусто-'
