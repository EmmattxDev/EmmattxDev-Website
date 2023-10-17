"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import settings
# from base import views


urlpatterns = [
    # administration 
    path('professor4jesus/admin/', admin.site.urls),

    # my main pages for my website
    path('', include('pages.urls')),
]
    
#     # blog home pages and templates
#     path('base/', include('base.urls')),

#     # blog urls and templates
#     path('blog/', include('blog.urls')),

#     # #contact urls
#     # path('contact/', include('contact.urls')),

#     # search functionality for blog
#     path('search/', include('search.urls')),
#     path('tags/<slug:slug>/', views.tag, name='tag'),

#     # account and authentication
#    path('accounts/', include('authentication.urls')),
   

#    # feedback test urls
#    path('feedback/', include('feedback.urls')),



if settings.DEBUG:
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
