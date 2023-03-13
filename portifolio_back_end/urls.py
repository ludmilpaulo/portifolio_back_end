from django.contrib import admin
from django.urls import path

from information.views import my_info

urlpatterns = [
    path('my_info/', my_info),
    path('admin/', admin.site.urls),
]
