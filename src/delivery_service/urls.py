"""
delivery_service URL Configuration.

In the project, the views are built using the DRF ViewSet class
because its methods like create, list, retrieve etc are
more convenient than Django class based views.
Also, the ViewSet class creates RESTful URLs under the hood
which makes it even more convenient (see DRF docs for reference).
"""
from django.conf.urls import url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

import delivery_service.views as delivery_service_views


router: DefaultRouter = DefaultRouter()
router.register(r'zones', delivery_service_views.ZonesView, basename='zones')
router.register(r'carriers', delivery_service_views.CarriersView, basename='carriers')

schema_view = get_schema_view(
   openapi.Info(title='Delivery Service API', default_version='v1'),
   public=True,
   permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
urlpatterns += router.urls
