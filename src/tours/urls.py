from django.conf.urls import include, url
from django.contrib import admin

from .views import (
                TourListView,
                TourDetailView,
                TourCreateView,
                TourUpdateView,
                )

urlpatterns = [

    url(r'^$', TourListView.as_view(), name='tour_list_view'),
    url(r'^add/$', TourCreateView.as_view(), name='tour_create_view'),
    url(r'^(?P<pk>\d+)/$', TourDetailView.as_view(), name='tour_detail_view'),
    url(r'^(?P<slug>[\w-]+)/$', TourDetailView.as_view(), name='tour_detail_slug_view'),
    url(r'^(?P<pk>\d+)/edit/$', TourUpdateView.as_view(), name='tour_update_view'),
    url(r'^(?P<slug>[\w-]+)/edit/$', TourUpdateView.as_view(), name='tour_update_slug_view'),




]
