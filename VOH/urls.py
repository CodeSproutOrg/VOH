from django.contrib import admin
from django.urls import path
from core import views
from core.views import pageNotFound

handler404 = pageNotFound

urlpatterns = [
    path('', views.index, name='main'),
    path('blog', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.blog, name='blog'),
    path('stories', views.stories, name='stories'),
    path('test', views.process_alienation_test, name='process_alienation_test'),

    path('links', views.links_view, name='links'),
    path('videos', views.videos_view, name='videos'),
    path('apps', views.apps_view, name='apps'),
    path('documents', views.documents_view, name='documents_view'),
    path('documents/<str:file_name>/', views.download_file, name='download_file'),

    path('developers', views.developers_view, name='developers'),

    path('admin/', admin.site.urls),
]
