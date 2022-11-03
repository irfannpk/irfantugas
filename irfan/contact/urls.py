from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('blog/', include ('blog.urls')),
    path('sosmed/', include ('home.urls')),
]
