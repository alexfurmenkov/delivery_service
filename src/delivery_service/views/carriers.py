from decimal import Decimal
from typing import List

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from delivery_service.models import DbCarrierModel, DbZoneModel
from delivery_service.serializers.model_serializers import DbCarrierModelSerializer
from delivery_service.serializers.request_serializers import (
    CreateNewCarrierSerializer,
    UpdateCarrierSerializer,
    SearchCarrierSerializer
)
from delivery_service.tools.decorators import request_validation, ensure_existing_record
from delivery_service.tools.responses import (
    ResponseBadRequest,
    ResponseCreated,
    ResponseSuccess,
    ResponseNotFound
)


class CarriersView(ViewSet):
    """
    This class handles HTTP requests on "/carriers/" endpoints
    """
    db_model_class = DbCarrierModel
    serializer_class = DbCarrierModelSerializer

    @request_validation(CreateNewCarrierSerializer)
    def create(self, request: Request) -> Response:
        """
        Endpoint that creates a new zone.
        """
        # ensure that there is no carrier with the same nickname
        nickname: str = request.data.pop('nickname')
        if self.db_model_class.objects.filter(nickname=nickname).exists():
            return ResponseBadRequest(message='Carrier with given nickname already exists.')

        # create new carrier
        carrier_zone: DbZoneModel = DbZoneModel.objects.get(id=request.data.pop('zone_id'))
        new_carrier: DbCarrierModel = self.db_model_class.objects.create(
            zone=carrier_zone,
            nickname=nickname,
            **request.data
        )
        return ResponseCreated(
            message='New carrier has been created successfully.',
            created_resource_id=new_carrier.id
        )

    def list(self, request: Request) -> Response:
        """
        Endpoint that lists all carriers.
        """
        carriers: List[DbCarrierModel] = self.db_model_class.objects.all()
        return ResponseSuccess(
            message='Carriers have been listed successfully.',
            response_data={'carriers': self.serializer_class(carriers, many=True).data}
        )

    @ensure_existing_record(db_model_class)
    def retrieve(self, request: Request, pk=None) -> Response:
        """
        Endpoint that gets a carriers by id.
        """
        carrier: DbCarrierModel = self.db_model_class.objects.get(id=pk)
        return ResponseSuccess(
            message='Carrier has been retrieved successfully.',
            response_data={'carrier': self.serializer_class(carrier).data}
        )

    @request_validation(SearchCarrierSerializer)
    @action(detail=False, methods=['get'])
    def search(self, request: Request) -> Response:
        """
        The endpoint searches carriers that serve in the zone with given coordinates.
        Accepts latitude and longitude in query params and returns carriers.
        One zone can be serviced by several carriers at the same time,
        so the endpoint returns a list of carriers.
        :param request: HTTP request
        :return: Response object
        """
        latitude: Decimal = Decimal(request.query_params['latitude'])
        longitude: Decimal = Decimal(request.query_params['longitude'])

        # ensure that requested zone exists
        if not DbZoneModel.objects.filter(latitude=latitude, longitude=longitude).exists():
            return ResponseNotFound('Carriers are not found.')

        # find carriers assigned to requested zone
        requested_zone: DbZoneModel = DbZoneModel.objects.get(latitude=latitude, longitude=longitude)
        carriers: List[DbCarrierModel] = DbCarrierModel.objects.filter(zone=requested_zone)
        return ResponseSuccess(
            message='Carriers have been found successfully.',
            response_data={'carriers': self.serializer_class(carriers, many=True).data}
        )

    @request_validation(UpdateCarrierSerializer)
    @ensure_existing_record(db_model_class)
    def update(self, request: Request, pk=None) -> Response:
        """
        Endpoint that updates details of a carrier with the given id.
        """
        # update the carrier
        carrier_to_update: DbCarrierModel = self.db_model_class.objects.get(id=pk)
        carrier_to_update.update_db_record(request.data)

        # return successful response
        return ResponseSuccess(message=f'Carrier with id {pk} has been updated successfully.')

    @ensure_existing_record(db_model_class)
    def destroy(self, request: Request, pk=None) -> Response:
        """
        Endpoint that deletes a carrier.
        """
        # delete the carrier
        carrier_to_delete: DbCarrierModel = self.db_model_class.objects.get(id=pk)
        carrier_to_delete.delete()

        # return successful response
        return ResponseSuccess(message=f'Carrier with id {pk} has been deleted successfully.')
