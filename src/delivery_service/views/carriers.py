from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from delivery_service.models import DbCarrierModel, DbZoneModel
from delivery_service.serializers.model_serializers import DbCarrierModelSerializer
from delivery_service.serializers.request_serializers import CreateNewCarrierSerializer
from delivery_service.tools.decorators import request_validation
from delivery_service.tools.responses import ResponseBadRequest, ResponseCreated


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
