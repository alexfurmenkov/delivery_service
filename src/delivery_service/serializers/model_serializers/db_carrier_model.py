from rest_framework.serializers import ModelSerializer

from delivery_service.models import DbCarrierModel


class DbCarrierModelSerializer(ModelSerializer):
    """
    Serializer for DbCarrierModel class.
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
