"""
This module is an entrypoint for all request serializers.
"""
from .zones import CreateNewZoneSerializer, UpdateZoneSerializer
from .carriers import CreateNewCarrierSerializer, UpdateCarrierSerializer, SearchCarrierSerializer

__all__ = [
    'CreateNewZoneSerializer',
    'UpdateZoneSerializer',
    'CreateNewCarrierSerializer',
    'UpdateCarrierSerializer',
    'SearchCarrierSerializer',
]
