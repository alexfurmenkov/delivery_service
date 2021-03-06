"""
This module is responsible for handling incoming messages
HTTP requests to "/zones/" endpoints.
"""
from decimal import Decimal
from typing import List

from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from delivery_service.models import DbZoneModel
from delivery_service.serializers.model_serializers import DbZoneModelSerializer
from delivery_service.serializers.request_serializers import (
    CreateNewZoneSerializer,
    UpdateZoneSerializer
)
from delivery_service.tools.decorators import (
    request_validation,
    ensure_existing_record
)
from delivery_service.tools.responses import (
    ResponseBadRequest,
    ResponseCreated,
    ResponseSuccess
)


class ZonesView(ViewSet):
    """
    The class implements CRUD functional for zones endpoints.
    """
    db_model_class = DbZoneModel
    serializer_class = DbZoneModelSerializer

    @swagger_auto_schema(
        request_body=CreateNewZoneSerializer,
        responses={
            '201': 'New zone has been created successfully.',
            '400': 'Zone with given coordinates already exists.',
        }
    )
    @request_validation(CreateNewZoneSerializer)
    def create(self, request: Request) -> Response:
        """
        Endpoint that creates a new zone.
        """
        longitude: Decimal = Decimal(request.data['longitude'])
        latitude: Decimal = Decimal(request.data['latitude'])
        name: str = request.data.get('name')  # name is optional

        # ensure that there is no zone with the same coordinates
        if self.db_model_class.objects.filter(longitude=longitude, latitude=latitude).exists():
            return ResponseBadRequest(message='Zone with given coordinates already exists.')

        # create new zone
        new_zone: DbZoneModel = self.db_model_class.objects.create(
            longitude=longitude,
            latitude=latitude,
            name=name
        )
        return ResponseCreated(
            message='New zone has been created successfully.',
            created_resource_id=new_zone.id
        )

    @swagger_auto_schema(
        responses={
            '200': 'Zones have been listed successfully.',
        }
    )
    def list(self, request: Request) -> Response:
        """
        Endpoint that lists all zones.
        """
        zones: List[DbZoneModel] = self.db_model_class.objects.all()
        return ResponseSuccess(
            message='Zones have been listed successfully.',
            response_data={'zones': self.serializer_class(zones, many=True).data}
        )

    @swagger_auto_schema(
        responses={
            '200': 'Zone has been retrieved successfully.',
            '404': 'Zone with given id is not found.',
        }
    )
    @ensure_existing_record(db_model_class)
    def retrieve(self, request: Request, pk=None) -> Response:
        """
        Endpoint that gets a zone by id.
        """
        zone: DbZoneModel = self.db_model_class.objects.get(id=pk)
        return ResponseSuccess(
            message='Zone has been retrieved successfully.',
            response_data={'zone': self.serializer_class(zone).data}
        )

    @swagger_auto_schema(
        request_body=UpdateZoneSerializer,
        responses={
            '200': 'Zone has been updated successfully.',
            '404': 'Zone with given id is not found.',
        }
    )
    @request_validation(UpdateZoneSerializer)
    @ensure_existing_record(db_model_class)
    def update(self, request: Request, pk=None) -> Response:
        """
        Endpoint that updates a zone with the given id.
        """
        zone_to_update: DbZoneModel = self.db_model_class.objects.get(id=pk)
        zone_to_update.update_db_record(request.data)
        return ResponseSuccess(f'Zone with id {pk} has been updated successfully.')

    @swagger_auto_schema(
        responses={
            '200': 'Zone has been deleted successfully.',
            '404': 'Zone with given id is not found.',
        }
    )
    @ensure_existing_record(db_model_class)
    def destroy(self, request: Request, pk=None) -> Response:
        """
        Endpoint that deletes a zone.
        """
        # delete the carrier
        zone_to_delete: DbZoneModel = self.db_model_class.objects.get(id=pk)
        zone_to_delete.delete()

        # return successful response
        return ResponseSuccess(message=f'Zone with id {pk} has been deleted successfully.')
