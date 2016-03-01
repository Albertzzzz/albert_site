from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.add, name='add'),
    url(r'^(?P<a>[0-9]+)/(?P<b>[0-9]+)/$', views.add2, name='add2')
]
