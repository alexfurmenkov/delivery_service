"""
delivery_service URL Configuration.

In the project, the views are built using the DRF ViewSet class
because its methods like create, list, retrieve etc are
more convenient than Django class based views.
Also, the ViewSet class creates RESTful URLs under the hood
which makes it even more convenient (see DRF docs for reference).
"""
from rest_framework.routers import DefaultRouter

import delivery_service.views as delivery_service_views


zones_router: DefaultRouter = DefaultRouter()
zones_router.register(r'zones', delivery_service_views.ZonesView, basename='zones')


urlpatterns: list = zones_router.urls
