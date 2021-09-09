from rest_framework.serializers import Serializer, CharField, IntegerField


class CreateNewCarrierSerializer(Serializer):
    """
    Serializer for POST HTTP request on URL "/carriers/"
    """

    zone_id = CharField(required=True, label='zone_id', max_length=1000)
    nickname = CharField(required=True, label='nickname', max_length=1000)
    first_name = CharField(required=True, label='first_name', max_length=1000)
    last_name = CharField(required=True, label='last_name', max_length=1000)
    gender = CharField(required=True, label='gender', max_length=1000)
    age = IntegerField(required=True, label='age')
