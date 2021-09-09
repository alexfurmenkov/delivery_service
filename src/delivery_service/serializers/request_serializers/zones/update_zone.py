from rest_framework.fields import DecimalField
from rest_framework.serializers import Serializer, CharField


class UpdateZoneSerializer(Serializer):
    """
    Serializer for PUT HTTP request on URL "/zones/{zone_id}/"
    """

    longitude = DecimalField(required=False, max_digits=8, decimal_places=4, label='longitude')
    latitude = DecimalField(required=False, max_digits=8, decimal_places=4, label='latitude')
    name = CharField(required=False, label='name', max_length=1000)
