from rest_framework.fields import DecimalField
from rest_framework.serializers import Serializer, CharField


class CreateNewZoneSerializer(Serializer):
    """
    Serializer for POST HTTP request on URL "/zones/"
    """

    longitude = DecimalField(max_digits=8, decimal_places=4, label='longitude')
    latitude = DecimalField(max_digits=8, decimal_places=4, label='latitude')
    name = CharField(required=False, label='name', max_length=1000)
