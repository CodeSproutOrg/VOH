from django import template
from django.shortcuts import get_object_or_404

from core.models import Post

register = template.Library()


@register.simple_tag()
def blog_posts():
    posts = Post.objects.all()
    return posts


@register.simple_tag()
def blog_post(post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return post
