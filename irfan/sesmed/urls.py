from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', include ('about.urls')),
    path('blog/', include ('blog.urls')),
]
