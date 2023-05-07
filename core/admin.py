from django.contrib import admin
from .models import Post, Link, UserPost, File


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('url_title', 'title',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(UserPost)
admin.site.register(File)
