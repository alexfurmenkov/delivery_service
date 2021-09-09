"""
Serializer for GET HTTP request on URL "/carriers/search/"
"""
from rest_framework.fields import DecimalField

from ..base_request_serializer import BaseRequestSerializer


class SearchCarrierSerializer(BaseRequestSerializer):
    """
    The class defines the fields that the request has to contain
    """

    longitude = DecimalField(max_digits=8, decimal_places=4, label='longitude')
    latitude = DecimalField(max_digits=8, decimal_places=4, label='latitude')
