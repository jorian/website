from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^search/$', views.search),
]
