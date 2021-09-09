"""
The module describes all DB models of the project.
A model is a class that represents a DB table and encapsulates business logic.

Base model is not added to __all__ because it is abstract
and should not be instanced.
"""
from .db_zone_model import DbZoneModel
from .db_carrier_model import DbCarrierModel


__all__ = [
    'DbZoneModel',
    'DbCarrierModel',
]
