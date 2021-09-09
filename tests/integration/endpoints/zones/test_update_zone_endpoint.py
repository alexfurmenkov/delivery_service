import uuid
from decimal import Decimal

from django.test import TestCase
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from delivery_service.models import DbZoneModel
from tests.test_utils.test_constants import DEFAULT_CONTENT_TYPE
from tests.test_utils.test_records_pks import TEST_ZONE_PK


class TestUpdateZoneEndpoint(TestCase):
    """
    This class contains tests that check PUT "/zones" endpoint.
    """
    fixtures: list = ['test_zone.json', ]

    def setUp(self) -> None:
        self.request_path: str = '/zones/'
        self.zone: DbZoneModel = DbZoneModel.objects.get(pk=TEST_ZONE_PK)

    def test_update_zone(self):
        """
        The test checks the happy scenario of updating a zone.
        Expected behavior is 200 HTTP response
        with success message.
        """
        # send request to update a zone
        request_data: dict = {
            'name': 'new zone name',
            'longitude': Decimal('32.9865')
        }
        response: Response = self.client.put(
            path=f'{self.request_path}{self.zone.id}/',
            data=request_data,
            content_type=DEFAULT_CONTENT_TYPE
        )

        # check response format
        assert response.status_code == HTTP_200_OK
        assert response.data == {
            'status': 'success',
            'message': f'Zone with id {self.zone.id} has been updated successfully.'
        }

        # ensure that the zone was updated in the DB
        updated_zone: DbZoneModel = DbZoneModel.objects.get(id=self.zone.id)
        assert updated_zone.name == request_data['name']
        assert updated_zone.longitude == request_data['longitude']

    def test_update_zone_invalid_request_body(self):
        """
        Test the case when the request contains invalid body.
        Expected behavior is a response with
        400 HTTP status and error message.
        """
        # send request to update a zone
        request_data: dict = {
            'name': 'new zone name',
            'longitude': 'of jcvbfndneje a aaaa'
        }
        response: Response = self.client.put(
            path=f'{self.request_path}{self.zone.id}/',
            data=request_data,
            content_type=DEFAULT_CONTENT_TYPE
        )
        assert response.data == {
            'status': 'error',
            'message': 'Request body is invalid.',
            'invalid_keys': ['longitude', ]
        }

    def test_update_zone_not_found(self):
        """
        Test the case when the zone is not found.
        Expected behavior is a response with
        404 HTTP status and error message.
        """
        not_found_zone_id: str = str(uuid.uuid4())
        response: Response = self.client.put(
            path=f'{self.request_path}{not_found_zone_id}/',
            data={},
            content_type=DEFAULT_CONTENT_TYPE
        )
        assert response.data == {
            'status': 'error',
            'message': f'Resource with id {not_found_zone_id} is not found.'
        }
