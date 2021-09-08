from django.db.models import CharField, IntegerField, ForeignKey, CASCADE

from .base_db_model import BaseDbModel
from .db_zone_model import DbZoneModel


class DbCarrierModel(BaseDbModel):
    """
    This class represents a carrier DB record.
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
