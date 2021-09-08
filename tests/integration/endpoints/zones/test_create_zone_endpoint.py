from decimal import Decimal

from django.test import TestCase
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from delivery_service.models import DbZoneModel
from tests.test_utils.test_constants import DEFAULT_CONTENT_TYPE
from tests.test_utils.test_records_pks import TEST_ZONE_PK


class TestCreateZoneEndpoint(TestCase):
    """
    This class contains tests that check POST "/zones" endpoint.
    """
    fixtures = ['test_zone.json', ]

    def setUp(self) -> None:
        self.request_path: str = '/zones/'
        self.existing_zone = DbZoneModel.objects.get(pk=TEST_ZONE_PK)

    def test_create_new_zone(self):
        """
        The test checks the happy scenario of creating a user.
        Expected behavior is 201 HTTP response with success message and zone_id.
        """
        request_data: dict = {
            'longitude': Decimal('25.4857'),
            'latitude': Decimal('52.4587'),
            'name': 'zone name'
        }
        response: Response = self.client.post(
            path=self.request_path,
            data=request_data,
            content_type=DEFAULT_CONTENT_TYPE
        )
        assert response.status_code == HTTP_201_CREATED
        assert response.data['status'] == 'success'
        assert response.data['message'] == 'New zone has been created successfully.'

        created_zone: DbZoneModel = DbZoneModel.objects.get(id=response.data['id'])
        assert created_zone.longitude == request_data['longitude']
        assert created_zone.latitude == request_data['latitude']
        assert created_zone.name == request_data['name']

    def test_create_new_zone_existing_zone(self):
        """
        Tests the case when a zone exists. Expected behavior is
        a response with 400 HTTP status and error message.
        """
        request_data: dict = {
            'longitude': self.existing_zone.longitude,
            'latitude': self.existing_zone.latitude,
            'name': self.existing_zone.name
        }
        response: Response = self.client.post(
            path=self.request_path,
            data=request_data,
            content_type=DEFAULT_CONTENT_TYPE
        )
        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data == {
            'status': 'error',
            'message': 'Zone with given coordinates already exists.'
        }

    def test_create_new_no_mandatory_fields(self):
        """
        Tests the case when request body is missing coordinates.
        Expected behavior is a response with 400 HTTP status and error message.
        """
        request_data: dict = {
            'name': 'test name',
        }
        response: Response = self.client.post(
            path=self.request_path,
            data=request_data,
            content_type=DEFAULT_CONTENT_TYPE
        )
        assert response.status_code == 400
        assert response.data == {
            'status': 'error',
            'message': 'Request body is invalid.',
            'invalid_keys': ['longitude', 'latitude', ]
        }

    def test_create_new_zone_invalid_coordinates(self):
        """
        Tests the case when a zone exists. Expected behavior is
        a response with 400 HTTP status and error message.
        """
        request_data: dict = {
            'longitude': 'allalala',
            'latitude': 'sdjufdno3rnfjnrj'
        }
        response: Response = self.client.post(
            path=self.request_path,
            data=request_data,
            content_type=DEFAULT_CONTENT_TYPE
        )
        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data == {
            'status': 'error',
            'message': 'Request body is invalid.',
            'invalid_keys': ['longitude', 'latitude', ]
        }
