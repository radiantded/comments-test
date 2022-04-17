from django.contrib import admin
from .models import Post, Comment


admin.register(Post)
admin.register(Comment)


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('post',)
#     search_fields = ('post',)
#     list_filter = ('post',)
#     empty_value_display = '-empty-'


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('comment_text', 'post',)
#     search_fields = ('comment_text',  'post',)
#     list_filter = ('comment_text',  'post',)
#     empty_value_display = '-empty-'
