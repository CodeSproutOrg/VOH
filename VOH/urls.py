from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='home'),
    path('links', views.links, name='links'),
    path('admin/', admin.site.urls),
]
