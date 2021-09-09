"""
Serializer for POST HTTP request on URL "/carriers/"
"""
from rest_framework.serializers import CharField, IntegerField

from ..base_request_serializer import BaseRequestSerializer


class CreateNewCarrierSerializer(BaseRequestSerializer):
    """
    The class defines the fields that the request has to contain
    """

    zone_id = CharField(required=True, label='zone_id', max_length=1000)
    nickname = CharField(required=True, label='nickname', max_length=1000)
    first_name = CharField(required=True, label='first_name', max_length=1000)
    last_name = CharField(required=True, label='last_name', max_length=1000)
    gender = CharField(required=True, label='gender', max_length=1000)
    age = IntegerField(required=True, label='age')
