from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'date', 'description']
    list_display_links = ['title']


admin.site.register(Post, PostAdmin)
