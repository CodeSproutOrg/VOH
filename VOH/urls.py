from django.contrib import admin
from django.urls import path
from core import views
from core.views import pageNotFound

handler404 = pageNotFound

urlpatterns = [
    path('', views.index, name='home'),
    path('posts', views.posts, name='posts'),
    path('stories', views.stories, name='stories'),
    path('links', views.links, name='links'),
    path('help-us', views.help_us, name='help-us'),
    path('admin/', admin.site.urls),
]
