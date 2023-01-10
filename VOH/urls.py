from django.contrib import admin
from django.urls import path
from core import views
from core.views import pageNotFound

handler404 = pageNotFound

urlpatterns = [
    path('', views.index, name='main'),
    path('posts', views.posts, name='posts'),
    path('stories', views.stories, name='stories'),
    path('stories_add', views.stories_add, name='stories_add'),
    path('links', views.links, name='links'),
    path('help-us', views.help_us, name='help-us'),
    path('admin/', admin.site.urls),
]
