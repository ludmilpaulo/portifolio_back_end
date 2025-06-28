from django.contrib import admin
from django.urls import include, path

from information.views import homePage, my_info, projectDetail, projectsPage, search

urlpatterns = [
    path('my_info/', my_info),
    path('', homePage, name='homePage'),
    path('projects/', projectsPage, name='projectsPage'),
    path('projects/<str:slug>/', projectDetail, name='projectDetail'),
    path('search/', search, name='search'),
    path('testimonials/', include('testimonials.urls')),

  #  path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),

  #  path('blog/', include('blog.urls', namespace='blog')),
]
