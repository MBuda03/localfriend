from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^detail/$', 'tours.views.detail_view', name='detail_view'),
    url(r'^list/$', 'tours.views.list_view', name='list_view'),
]
