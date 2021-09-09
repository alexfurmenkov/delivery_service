"""
Serializer for DbCarrierModel class.
"""
from rest_framework.serializers import ModelSerializer

from delivery_service.models import DbCarrierModel


class DbCarrierModelSerializer(ModelSerializer):
    """
    The serializer defines the fields that have to be serialized.
    """

    class Meta:
        model = DbCarrierModel
        fields: list = [
            'id',
            'created_at',
            'updated_at',
            'zone',
            'nickname',
            'first_name',
            'last_name',
            'gender',
            'age',
        ]
