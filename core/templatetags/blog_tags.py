from django import template
from django.shortcuts import get_object_or_404

from core.models import Post, VideoLink

register = template.Library()


@register.simple_tag()
def blog_posts():
    posts = Post.objects.all()
    return posts

@register.simple_tag()
def blog_post(post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return post

@register.simple_tag()
def video_posts():
    videos = VideoLink.objects.all()
    return videos

@register.simple_tag()
def video_post(video_slug):
    video = get_object_or_404(VideoLink, slug=video_slug)
    return video