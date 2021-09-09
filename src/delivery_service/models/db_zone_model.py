"""
This class represents a zone DB record.
"""
from django.db.models import DecimalField, CharField

from .base_db_model import BaseDbModel


class DbZoneModel(BaseDbModel):
    """
    This class describes the implementation of the DB record:
    its attributes, methods and table name.
    """

    class Meta:
        db_table = 'zones'
        unique_together = ('longitude', 'latitude', )

    longitude = DecimalField(max_digits=8, decimal_places=4, name='longitude')
    latitude = DecimalField(max_digits=8, decimal_places=4, name='latitude')
    name = CharField(max_length=1000, blank=True, default='', name='name')

    @property
    def _update_allowed_fields(self) -> list:
        return [
            'name',
            'longitude',
            'latitude',
        ]
