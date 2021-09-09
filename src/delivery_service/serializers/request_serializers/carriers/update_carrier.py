from rest_framework.serializers import Serializer, CharField, IntegerField


class UpdateCarrierSerializer(Serializer):
    """
    Serializer for PUT HTTP request on URL "/carriers/"
    """

    zone = CharField(required=False, label='zone', max_length=1000)
    first_name = CharField(required=False, label='first_name', max_length=1000)
    last_name = CharField(required=False, label='last_name', max_length=1000)
    gender = CharField(required=False, label='gender', max_length=1000)
    age = IntegerField(required=False, label='age')
