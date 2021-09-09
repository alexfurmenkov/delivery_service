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


router: DefaultRouter = DefaultRouter()
router.register(r'zones', delivery_service_views.ZonesView, basename='zones')
router.register(r'carriers', delivery_service_views.CarriersView, basename='carriers')

urlpatterns: list = router.urls
