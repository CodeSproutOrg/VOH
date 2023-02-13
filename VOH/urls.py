from django.contrib import admin
from django.urls import path
from core import views
from core.views import pageNotFound

handler404 = pageNotFound

urlpatterns = [
    path('', views.index, name='main'),
    path('blog', views.blog, name='blog'),
    path('stories', views.stories, name='stories'),
    path('resources', views.resources, name='resources'),
    path('resources/<str:file_name>/', views.download_file, name='download_file'),
    path('test', views.process_alienation_test, name='process_alienation_test'),
    path('admin/', admin.site.urls),
]
