from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('debug_toolbar.urls')),
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
