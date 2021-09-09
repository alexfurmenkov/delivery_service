"""
This class represents a carrier DB record.
"""
from django.db.models import CharField, IntegerField, ForeignKey, CASCADE

from .base_db_model import BaseDbModel
from .db_zone_model import DbZoneModel


class DbCarrierModel(BaseDbModel):
    """
    This class describes the implementation of the DB record:
    its attributes, methods and table name.
    """

    class Meta:
        db_table = 'carriers'

    zone = ForeignKey(to=DbZoneModel, on_delete=CASCADE, name='zone')
    nickname = CharField(max_length=1000, unique=True, name='nickname')
    first_name = CharField(max_length=1000, name='first_name')
    last_name = CharField(max_length=1000, name='last_name')
    gender = CharField(max_length=1000, name='gender')
    age = IntegerField(name='age')

    @property
    def _update_allowed_fields(self) -> list:
        return [
            'zone',
            'first_name',
            'last_name',
            'gender',
            'age',
        ]

    def update_db_record(self, update_body: dict):
        """
        Extends the method of parent class.
        Reason - Need to get zone record object from the DB if it is being updated.
        :param update_body: Dict with keys to be updated
        :return: None
        """
        zone_id: str = update_body.get('zone', None)
        if zone_id:
            update_body['zone'] = DbZoneModel.objects.get(id=zone_id)
        super().update_db_record(update_body)
