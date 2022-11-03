from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', include ('about.urls')),
    path('blog/', include ('blog.urls')),
    path('sosmed/', include ('home.urls')),
]
