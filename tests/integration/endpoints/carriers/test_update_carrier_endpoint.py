import uuid
from decimal import Decimal

from django.test import TestCase
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from delivery_service.models import DbCarrierModel, DbZoneModel
from tests.test_utils.test_constants import DEFAULT_CONTENT_TYPE
from tests.test_utils.test_records_pks import TEST_CARRIER_PK


class TestUpdateZoneEndpoint(TestCase):
    """
    This class contains tests that check PUT "/carriers" endpoint.
    """
    fixtures: list = ['test_zone.json', 'test_carrier.json', ]

    def setUp(self) -> None:
        self.request_path: str = '/carriers/'
        self.carrier: DbCarrierModel = DbCarrierModel.objects.get(pk=TEST_CARRIER_PK)

    def test_update_carrier(self):
        """
        The test checks the happy scenario of updating a carrier.
        Expected behavior is 200 HTTP response
        with success message.
        """
        # send request to update a carrier
        new_zone: DbZoneModel = DbZoneModel.objects.create(longitude=Decimal('74.3937'), latitude=Decimal('34.9383'))
        request_data: dict = {
            'nickname': 'new nickname',
            'first_name': 'john',
            'zone': new_zone.id
        }
        response: Response = self.client.put(
            path=f'{self.request_path}{self.carrier.id}/',
            data=request_data,
            content_type=DEFAULT_CONTENT_TYPE
        )

        # check response format
        assert response.status_code == HTTP_200_OK
        assert response.data == {
            'status': 'success',
            'message': f'Carrier with id {self.carrier.id} has been updated successfully.'
        }

        # ensure that the carrier was updated in the DB
        updated_carrier: DbCarrierModel = DbCarrierModel.objects.get(id=self.carrier.id)
        assert updated_carrier.nickname != request_data['nickname']  # nickname can't be updated
        assert updated_carrier.first_name == request_data['first_name']
        assert updated_carrier.zone.id == request_data['zone']

    def test_update_carrier_invalid_request_body(self):
        """
        Test the case when the request contains invalid body.
        Expected behavior is a response with
        400 HTTP status and error message.
        """
        # send request to update a carrier
        request_data: dict = {
            'first_name': {
                'aa': 'bbb'
            }
        }

        # check response format
        response: Response = self.client.put(
            path=f'{self.request_path}{self.carrier.id}/',
            data=request_data,
            content_type=DEFAULT_CONTENT_TYPE
        )
        assert response.data == {
            'status': 'error',
            'message': 'Request body is invalid.',
            'invalid_keys': ['first_name', ]
        }

    def test_update_carrier_not_found(self):
        """
        Test the case when the carrier is not found.
        Expected behavior is a response with
        404 HTTP status and error message.
        """
        not_found_carrier_id: str = str(uuid.uuid4())
        response: Response = self.client.put(
            path=f'{self.request_path}{not_found_carrier_id}/',
            data={},
            content_type=DEFAULT_CONTENT_TYPE
        )
        assert response.data == {
            'status': 'error',
            'message': f'Resource with id {not_found_carrier_id} is not found.'
        }
