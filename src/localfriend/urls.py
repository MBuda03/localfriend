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
    url(r'^create/$', 'tours.views.create_view', name='create_view'),
    url(r'^detail/(?P<object_id>\d+)/edit/$', 'tours.views.update_view', name='detail_view'),

    url(r'^detail/(?P<object_id>\d+)/$', 'tours.views.detail_view', name='detail_view'),
    url(r'^detail/(?P<slug>[\w-]+)/$', 'tours.views.detail_slug_view', name='detail_slug_view'),
    url(r'^list/$', 'tours.views.list_view', name='list_view'),
    url(r'^tours/$', TourListView.as_view(), name='tour_list_view'),
    url(r'^tours/add/$', TourCreateView.as_view(), name='tour_create_view'),

    url(r'^tours/(?P<pk>\d+)/$', TourDetailView.as_view(), name='tour_detail_view'),
    url(r'^tours/(?P<slug>[\w-]+)/$', TourDetailView.as_view(), name='tour_detail_slug_view'),
    url(r'^tours/(?P<pk>\d+)/edit/$', TourUpdateView.as_view(), name='tour_update_view'),
    url(r'^tours/(?P<slug>[\w-]+)/edit/$', TourUpdateView.as_view(), name='tour_update_slug_view'),




]
