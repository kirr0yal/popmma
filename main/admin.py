from django.contrib import admin

from main.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'title', 'created_at', 'photo', 'is_published')
    list_display_links = ('id', 'tag', 'title', 'photo')
    search_fields = ('tag', 'title', 'subtitle', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
