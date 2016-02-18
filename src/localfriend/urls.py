from django.conf.urls import include, url
from django.contrib import admin

from tours.views import (
                TourListView,
                TourDetailView,
                TourCreateView,
                TourUpdateView,
                )


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tours/',include("tours.urls", namespace='tours') ),

]


"""
    url(r'^create/$', 'tours.views.create_view', name='create_view'),
    url(r'^detail/(?P<object_id>\d+)/edit/$', 'tours.views.update_view', name='detail_view'),

    url(r'^detail/(?P<object_id>\d+)/$', 'tours.views.detail_view', name='detail_view'),
    url(r'^detail/(?P<slug>[\w-]+)/$', 'tours.views.detail_slug_view', name='detail_slug_view'),
    url(r'^list/$', 'tours.views.list_view', name='list_view'),
"""
