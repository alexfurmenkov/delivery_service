import uuid

from django.test import TestCase
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from delivery_service.models import DbCarrierModel, DbZoneModel
from delivery_service.serializers.model_serializers import DbCarrierModelSerializer
from tests.test_utils.test_records_pks import TEST_CARRIER_PK, TEST_ZONE_PK


class TestGetCarriersEndpoints(TestCase):
    """
    This class contains tests that check GET "/carriers/..." endpoints.
    """
    fixtures: list = ['test_zone.json', 'test_carrier.json', ]

    def setUp(self) -> None:
        self.request_path: str = '/carriers/'
        self.carrier: DbCarrierModel = DbCarrierModel.objects.get(pk=TEST_CARRIER_PK)
        self.zone: DbZoneModel = DbZoneModel.objects.get(pk=TEST_ZONE_PK)

    def test_list_carriers(self):
        """
        Tests the happy scenario of listing carriers.
        Expected behavior is a 200 HTTP response
        with success message and list of carriers.
        """
        response: Response = self.client.get(self.request_path)
        assert response.status_code == HTTP_200_OK
        assert response.data == {
            'status': 'success',
            'message': 'Carriers have been listed successfully.',
            'carriers': [DbCarrierModelSerializer(self.carrier).data, ],
        }

    def test_search_carriers(self):
        """
        This test checks that /carriers/search/
        endpoint finds the right carriers.
        Expected behavior is a 200 HTTP response
        with success message and list of carriers.
        """
        response: Response = self.client.get(
            f'{self.request_path}search/',
            {'latitude': self.zone.latitude, 'longitude': self.zone.longitude, }
        )
        assert response.status_code == HTTP_200_OK
        assert response.data == {
            'status': 'success',
            'message': 'Carriers have been found successfully.',
            'carriers': [DbCarrierModelSerializer(self.carrier).data, ],
        }

    def test_search_carriers_not_found(self):
        """
        This test checks that /carriers/search/
        endpoint finds the right carriers.
        Expected behavior is a 200 HTTP response
        with success message and list of carriers.
        """
        response: Response = self.client.get(
            f'{self.request_path}search/',
            {'latitude': '33.2222', 'longitude': '74.7482', }
        )
        assert response.status_code == HTTP_404_NOT_FOUND
        assert response.data == {
            'status': 'error',
            'message': 'Carriers are not found.',
        }

    def test_get_carrier_by_id(self):
        """
        Tests the happy scenario of getting a carrier by id.
        Expected behavior is a 200 HTTP response
        with success message and a single carrier.
        """
        response: Response = self.client.get(f'{self.request_path}{self.carrier.id}/')
        assert response.status_code == HTTP_200_OK
        assert response.data == {
            'status': 'success',
            'message': 'Carrier has been retrieved successfully.',
            'carrier': DbCarrierModelSerializer(self.carrier).data,
        }

    def test_get_carrier_by_id_not_found(self):
        """
        Tests case when requested carrier is not found.
        Expected behavior is response with 404 status and error message.
        """
        not_found_carrier_id: str = str(uuid.uuid4())
        response: Response = self.client.get(f'{self.request_path}{not_found_carrier_id}/')
        assert response.status_code == HTTP_404_NOT_FOUND
        assert response.data == {
            'status': 'error',
            'message': f'Resource with id {not_found_carrier_id} is not found.',
        }
