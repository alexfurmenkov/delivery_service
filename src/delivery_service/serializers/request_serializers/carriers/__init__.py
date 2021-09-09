"""
This module is an entrypoint for carriers request serializers.
"""
from .create_new_carrier import CreateNewCarrierSerializer
from .update_carrier import UpdateCarrierSerializer
from .search_carrier import SearchCarrierSerializer


__all__ = [
    'CreateNewCarrierSerializer',
    'UpdateCarrierSerializer',
    'SearchCarrierSerializer',
]
