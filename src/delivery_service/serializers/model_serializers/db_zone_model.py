from rest_framework.serializers import ModelSerializer

from delivery_service.models import DbZoneModel


class DbZoneModelSerializer(ModelSerializer):
    """
    Serializer for DbZoneModel class.
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
