"""
Serializer for DbZoneModel class.
"""
from rest_framework.serializers import ModelSerializer

from delivery_service.models import DbZoneModel


class DbZoneModelSerializer(ModelSerializer):
    """
    The serializer defines the fields that have to be serialized.
    """

    class Meta:
        model = DbZoneModel
        fields: list = [
            'id',
            'created_at',
            'updated_at',
            'longitude',
            'latitude',
            'name',
        ]
