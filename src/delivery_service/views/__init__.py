"""
The module contains the project views.
A view is responsible for handling HTTP request:
accepts a request and returns a response.
"""
from .zones import ZonesView
from .carriers import CarriersView


__all__ = [
    'ZonesView',
    'CarriersView',
]
