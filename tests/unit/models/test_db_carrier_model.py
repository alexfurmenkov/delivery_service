import uuid

from django.db import IntegrityError
from django.test import TestCase

from delivery_service.models import DbCarrierModel, DbZoneModel
from tests.test_utils.test_records_pks import TEST_CARRIER_PK, TEST_ZONE_PK


class TestDbCarrierModel(TestCase):
    """
    This class contains tests for the db carrier model.
    """

    fixtures = ['test_carrier.json', 'test_zone.json', ]

    def setUp(self) -> None:
        self.carrier: DbCarrierModel = DbCarrierModel.objects.get(pk=TEST_CARRIER_PK)
        self.zone: DbZoneModel = DbZoneModel.objects.get(pk=TEST_ZONE_PK)

    def test_create_new_carrier_existing_nickname(self):
        """
        Test checks that a carrier with the same nickname cannot be created more than once.
        """
        with self.assertRaises(IntegrityError):
            DbCarrierModel.objects.create(
                zone=self.zone,
                nickname=self.carrier.nickname,
                first_name=self.carrier.first_name,
                last_name=self.carrier.last_name,
                gender=self.carrier.gender,
                age=self.carrier.age
            )

    def test_update_carrier(self):
        """
        Test ensures that only allowed fields of a carrier can be updated.
        """
        new_first_name: str = 'updated first name'
        new_age: int = 40
        new_id: uuid.UUID = uuid.uuid4()

        # check that the attributes of an object have changed
        self.carrier.update_db_record({'first_name': new_first_name, 'age': new_age})
        assert self.carrier.first_name == new_first_name
        assert self.carrier.age == new_age
        assert self.carrier.id != new_id

        # check that the DB record has been updated
        updated_carrier: DbCarrierModel = DbCarrierModel.objects.get(id=self.carrier.id)
        assert updated_carrier.first_name == new_first_name
        assert updated_carrier.age == new_age
