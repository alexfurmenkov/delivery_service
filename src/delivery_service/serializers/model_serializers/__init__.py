"""
This module is an entrypoint for DB model serializers.
"""
from .db_zone_model import DbZoneModelSerializer
from .db_carrier_model import DbCarrierModelSerializer


__all__ = [
    'DbZoneModelSerializer',
    'DbCarrierModelSerializer',
]
