"""
Serializer for PUT HTTP request on URL "/zones/{zone_id}/"
"""
from rest_framework.fields import DecimalField
from rest_framework.serializers import CharField

from ..base_request_serializer import BaseRequestSerializer


class UpdateZoneSerializer(BaseRequestSerializer):
    """
    The class defines the fields that the request has to contain
    """

    longitude = DecimalField(required=False, max_digits=8, decimal_places=4, label='longitude')
    latitude = DecimalField(required=False, max_digits=8, decimal_places=4, label='latitude')
    name = CharField(required=False, label='name', max_length=1000)
