"""
This module is an entrypoint for zones request serializers.
"""
from .create_new_zone import CreateNewZoneSerializer
from .update_zone import UpdateZoneSerializer


__all__ = [
    'CreateNewZoneSerializer',
    'UpdateZoneSerializer',
]
