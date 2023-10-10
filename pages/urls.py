from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from backend import settings

app_name = 'pages'

urlpatterns = [
    path('', views.home, name="home"),

    #about page
    path('about/', views.about, name='about'),
    
    # portfolio details pages
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio/details/<slug:slug>/', views.portfolio_details, name="portfolio_details"),

    #contact page
    path('contact/', views.contact, name="contact"),

    #favicon urls
    path('favicon.io', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
]


if settings.DEBUG:
    urlpatterns += static(settings.development.STATIC_URL, document_root=settings.development.STATICFILES_DIRS)
    urlpatterns += static(settings.development.MEDIA_URL, document_root=settings.development.MEDIA_ROOT)