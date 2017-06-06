from django.conf.urls import url
from . import views

urlpatterns=[
    # /Hostels/
    url(r'^$',views.index,name=''),

    # /Hostels/71/
    url(r'^(?P<hostels_id>[0-9]+)/$',views.detail, name='detail'),


]
