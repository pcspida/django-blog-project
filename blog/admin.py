from blog.models import *
from django.contrib import admin
from django.contrib.auth.models import User

class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created','updated')
    search_fields= ('title','body')
    list_filter = ('created',)
    ordering=('title',)
   # inlines=[CommentInline,]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','author','some_body','created','updated')
    list_filter = ('created','author')
    


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)


