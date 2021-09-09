from django.test import TestCase
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from delivery_service.models import DbCarrierModel
from tests.test_utils.test_constants import DEFAULT_CONTENT_TYPE
from tests.test_utils.test_records_pks import TEST_CARRIER_PK, TEST_ZONE_PK


class TestCreateCarrierEndpoint(TestCase):
    """
    This class contains tests that check POST "/carriers" endpoint.
    """
    fixtures: list = ['test_zone.json', 'test_carrier.json', ]

    def setUp(self) -> None:
        self.request_path: str = '/carriers/'
        self.existing_carrier: DbCarrierModel = DbCarrierModel.objects.get(pk=TEST_CARRIER_PK)

    def test_create_new_carrier(self):
        """
        The test checks the happy scenario of creating a carrier.
        Expected behavior is 201 HTTP response
        with success message and zone_id.
        """
        request_data: dict = {
            'zone_id': TEST_ZONE_PK,
            'nickname': 'alex',
            'first_name': 'alexey',
            'last_name': 'furmenkov',
            'gender': 'male',
            'age': 22,
        }
        response: Response = self.client.post(
            path=self.request_path,
            data=request_data,
            content_type=DEFAULT_CONTENT_TYPE
        )
        assert response.status_code == HTTP_201_CREATED
        assert response.data['status'] == 'success'
        assert response.data['message'] == 'New carrier has been created successfully.'

        created_carrier: DbCarrierModel = DbCarrierModel.objects.get(id=response.data['id'])
        assert str(created_carrier.zone.id) == request_data['zone_id']
        assert created_carrier.nickname == request_data['nickname']
        assert created_carrier.first_name == request_data['first_name']
        assert created_carrier.last_name == request_data['last_name']
        assert created_carrier.gender == request_data['gender']
        assert created_carrier.age == request_data['age']

    def test_create_new_carrier_existing_carrier(self):
        """
        Tests the case when a carrier exists.
        Expected behavior is a response
        with 400 HTTP status and error message.
        """
        request_data: dict = {
            'zone_id': TEST_ZONE_PK,
            'nickname': self.existing_carrier.nickname,
            'first_name': 'alexey',
            'last_name': 'furmenkov',
            'gender': 'male',
            'age': 22,
        }
        response: Response = self.client.post(
            path=self.request_path,
            data=request_data,
            content_type=DEFAULT_CONTENT_TYPE
        )
        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data == {
            'status': 'error',
            'message': 'Carrier with given nickname already exists.'
        }

    def test_create_new_carrier_no_mandatory_fields(self):
        """
        Tests the case when request body is missing required fields.
        Expected behavior is a response with
        400 HTTP status and error message.
        """
        request_data: dict = {
            'first_name': 'ivan',
            'last_name': 'james'
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
            'invalid_keys': ['zone_id', 'nickname', 'gender', 'age', ]
        }
