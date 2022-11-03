from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('contact/', include ('contact.urls')),
    path('sosmed/', include ('home.urls')),
]
