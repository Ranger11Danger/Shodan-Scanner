from django.urls import path
from django.conf.urls import url
from django.views.generic.base import View
from .views import (dashboard_main_view,
                    dashboard_scan_details,
                    dashboard_cve_details,
                    dashboard_scan_view,
                    dashboard_manage_scan_view,
                    dashboard_address_view,
                    dashboard_info_view,
                    geo_view,
                    geo_map_view,
                    shodan_upload_view
                    )

app_name = "dashboard"
urlpatterns = [
    path("dashboard/scans", view=dashboard_main_view, name="index"),
    path("", view=dashboard_info_view, name="info"),
    path("addresses", view=dashboard_address_view, name="address view"),
    path("geo/", view=geo_view, name="geo"),
    path("upload/", view=shodan_upload_view, name="upload"),
    path("geo/map/", view=geo_map_view, name="map"),
    url(r'^scan/(?P<slug>[\w-]+)/manage/$', view=dashboard_manage_scan_view, name="manage scan"),
    url(r'^scan/(?P<slug>[\w-]+)/(?P<cveid>[\w-]+)/$', view=dashboard_cve_details, name="cve details"),
    url(r'^scan/(?P<slug>[\w-]+)/$', view=dashboard_scan_details, name="scan details"),
    url(r'^scan/$', view=dashboard_scan_view, name="scan"),
]
