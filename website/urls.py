from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/', include('bookshare.urls')),
    url(r'^search/$', views.search),
]
