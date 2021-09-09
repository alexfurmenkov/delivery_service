import uuid

from django.test import TestCase
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from delivery_service.models import DbCarrierModel
from tests.test_utils.test_constants import DEFAULT_CONTENT_TYPE
from tests.test_utils.test_records_pks import TEST_CARRIER_PK


class TestDeleteCarrierEndpoint(TestCase):
    """
    This class contains tests that check DELETE "/carriers/{carrier_id}/" endpoint.
    """

    fixtures: list = ['test_zone.json', 'test_carrier.json', ]

    def setUp(self) -> None:
        self.request_path: str = '/carriers/'
        self.carrier: DbCarrierModel = DbCarrierModel.objects.get(pk=TEST_CARRIER_PK)

    def test_delete_carrier(self):
        """
        Tests the happy scenario of deleting a zone.
        Expected behavior is a 200 HTTP response with success message.
        """
        response: Response = self.client.delete(
            path=f'{self.request_path}{self.carrier.id}/',
            content_type=DEFAULT_CONTENT_TYPE
        )
        assert response.status_code == HTTP_200_OK
        assert response.data == {
            'status': 'success',
            'message': f'Carrier with id {self.carrier.id} has been deleted successfully.'
        }

    def test_delete_carrier_not_found(self):
        """
        Tests case when requested carrier is not found.
        Expected behavior is response with 404 status and error message.
        """
        not_found_carrier_id: str = str(uuid.uuid4())
        response: Response = self.client.delete(
            path=f'{self.request_path}{not_found_carrier_id}/',
            content_type=DEFAULT_CONTENT_TYPE
        )
        assert response.status_code == HTTP_404_NOT_FOUND
        assert response.data == {
            'status': 'error',
            'message': f'Resource with id {not_found_carrier_id} is not found.'
        }
