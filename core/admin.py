from django.contrib import admin
from .models import Post, Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('url_title', 'title',)


admin.site.register(Post)
