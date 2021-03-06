from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from .views import (
                TourListView,
                TourDetailView,
                TourCreateView,
                TourUpdateView,
                )

urlpatterns = [




    url(r'^$', TourListView.as_view(), name='list'),


    #url(r'^test/$', TemplateView.as_view(template_name='/index.html'), name='test_index'),


    url(r'^add/$', TourCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TourDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', TourDetailView.as_view(), name='detail_slug'),
    url(r'^(?P<pk>\d+)/edit/$', TourUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/edit/$', TourUpdateView.as_view(), name='update_slug'),







]
