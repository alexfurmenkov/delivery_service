import uuid

from django.core.exceptions import ValidationError
from django.test import TestCase


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
        with self.assertRaises(ValidationError):
            DbCarrierModel.objects.create(
                nickname=self.carrier.nickname,
                name=self.carrier.name,
                surname=self.carrier.surname,
                age=self.carrier.age,
                zone=self.zone
            )

    def test_update_carrier(self):
        """
        Test ensures that only allowed fields of a carrier can be updated.
        """
        new_nickname: str = 'test_nickname'
        new_age: int = 40
        new_id: uuid.UUID = uuid.uuid4()

        # check that the attributes of an object have changed
        self.carrier.update_db_record({'nickname': new_nickname, 'age': new_age})
        assert self.carrier.nickname == new_nickname
        assert self.carrier.age == new_age
        assert self.carrier.id != new_id

        # check that the DB record has been updated
        updated_carrier: DbCarrierModel = DbCarrierModel.objects.get(id=self.carrier.id)
        assert updated_carrier.nickname == new_nickname
        assert updated_carrier.age == new_age
