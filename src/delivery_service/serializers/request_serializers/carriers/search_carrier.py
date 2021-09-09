from rest_framework.fields import DecimalField
from rest_framework.serializers import Serializer


class SearchCarrierSerializer(Serializer):
    """
    Serializer for GET HTTP request on URL "/carriers/search/"
    """

    longitude = DecimalField(max_digits=8, decimal_places=4, label='longitude')
    latitude = DecimalField(max_digits=8, decimal_places=4, label='latitude')
