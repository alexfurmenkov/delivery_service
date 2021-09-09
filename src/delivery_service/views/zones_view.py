from decimal import Decimal

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from delivery_service.models import DbZoneModel
from delivery_service.serializers.request_serializers import CreateNewZoneSerializer
from delivery_service.tools.decorators import request_validation
from delivery_service.tools.responses import ResponseBadRequest, ResponseCreated


class ZonesView(ViewSet):
    """
    This class handles HTTP requests on "/users" endpoints
    """
    db_model_class = DbZoneModel

    @request_validation(CreateNewZoneSerializer)
    def create(self, request: Request) -> Response:
        """
        Endpoint that creates a new zone.
        """
        longitude: Decimal = Decimal(request.data['longitude'])
        latitude: Decimal = Decimal(request.data['latitude'])
        name: str = request.data.get('name')  # name is optional

        if self.db_model_class.objects.filter(longitude=longitude, latitude=latitude).exists():
            return ResponseBadRequest(message='Zone with given coordinates already exists.')

        new_zone: DbZoneModel = self.db_model_class.objects.create(longitude=longitude, latitude=latitude, name=name)
        return ResponseCreated(
            message='New zone has been created successfully.',
            created_resource_id=new_zone.id
        )
