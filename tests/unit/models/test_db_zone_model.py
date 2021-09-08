import uuid
from decimal import Decimal

from django.db import IntegrityError
from django.test import TestCase

from delivery_service.models import DbZoneModel
from tests.test_utils.test_records_pks import TEST_ZONE_PK


class TestDbZoneModel(TestCase):
    """
    This class contains tests for the db zone model.
    """

    fixtures = ['test_zone.json', ]

    def setUp(self) -> None:
        self.zone: DbZoneModel = DbZoneModel.objects.get(pk=TEST_ZONE_PK)

    def test_create_new_zone_existing_coordinates(self):
        """
        Test checks that a zone with the same coordinates cannot be created more than once.
        An existing zone is created by the fixture.
        """
        with self.assertRaises(IntegrityError):
            DbZoneModel.objects.create(longitude=self.zone.longitude, latitude=self.zone.latitude, name=self.zone.name)

    def test_update_zone(self):
        """
        Test ensures that only allowed fields of a zone can be updated.
        """
        new_longitude: Decimal = Decimal('20.4912')
        new_latitude: Decimal = Decimal('50.7377')
        new_id: uuid.UUID = uuid.uuid4()

        # check that the attributes of an object have changed
        self.zone.update_db_record({'longitude': new_longitude, 'latitude': new_latitude, 'id': new_id})
        assert self.zone.longitude == new_longitude
        assert self.zone.latitude == new_latitude
        assert self.zone.id != new_id

        # check that the DB record has been updated
        updated_zone: DbZoneModel = DbZoneModel.objects.get(id=self.zone.id)
        assert updated_zone.longitude == new_longitude
        assert updated_zone.latitude == new_latitude
