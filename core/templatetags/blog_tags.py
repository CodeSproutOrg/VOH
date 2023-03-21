from django import template
from core.models import Post

register = template.Library()


@register.simple_tag()
def blog_posts():
    posts = Post.objects.all()
    return posts


@register.simple_tag()
def blog_post(post_id):
    post = Post.objects.get(id=post_id)
    return post
