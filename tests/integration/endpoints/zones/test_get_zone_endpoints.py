import uuid

from django.test import TestCase
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from delivery_service.models import DbZoneModel
from delivery_service.serializers.model_serializers import DbZoneModelSerializer
from tests.test_utils.test_records_pks import TEST_ZONE_PK


class TestGetZonesEndpoints(TestCase):
    """
    This class contains tests that check GET "/zones/..." endpoints.
    """
    fixtures: list = ['test_zone.json', ]

    def setUp(self) -> None:
        self.request_path: str = '/zones/'
        self.existing_zone: DbZoneModel = DbZoneModel.objects.get(pk=TEST_ZONE_PK)

    def test_list_zones(self):
        """
        Tests the happy scenario of listing zones.
        Expected behavior is a 200 HTTP response
        with success message and list of zones.
        """
        response: Response = self.client.get(self.request_path)
        assert response.status_code == HTTP_200_OK
        assert response.data == {
            'status': 'success',
            'message': 'Zones have been listed successfully.',
            'zones': [DbZoneModelSerializer(self.existing_zone).data]
        }

    def test_get_zone_by_id(self):
        """
        Tests the happy scenario of getting a zone by id.
        Expected behavior is a 200 HTTP response
        with success message and a single zone.
        """
        response: Response = self.client.get(f'{self.request_path}{self.existing_zone.id}/')
        assert response.status_code == HTTP_200_OK
        assert response.data == {
            'status': 'success',
            'message': 'Zone has been retrieved successfully.',
            'zone': DbZoneModelSerializer(self.existing_zone).data
        }

    def test_get_zone_by_id_not_found(self):
        """
        Tests case when requested zone is not found.
        Expected behavior is response with 404 status and error message.
        """
        not_found_zone_id: str = str(uuid.uuid4())
        response: Response = self.client.get(f'{self.request_path}{not_found_zone_id}/')
        assert response.status_code == HTTP_404_NOT_FOUND
        assert response.data == {
            'status': 'error',
            'message': f'Resource with id {not_found_zone_id} is not found.'
        }
