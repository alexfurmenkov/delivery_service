"""
The module contains base request serializer.
"""
from rest_framework.serializers import Serializer


class BaseRequestSerializer(Serializer):
    """
    This class inherits from DRF Serializer class and implements abstract methods.
    Interface of DRF Serializer class requires the child
    to implement create() and update() even if
    the child is not intended to create DB records.
    It is a drawback of DRF Serializer class interface and
    violates the Interface Segregation Principle.

    Custom request serializers of this project do not
    create new DB records, so create() and update() are overwritten
    in order to avoid ABC errors but do not actually contain any implementation.
    """

    def update(self, instance, validated_data):
        """
        Request serializers of this project do not update DB records
        :param instance: instance to update
        :param validated_data: validated data
        :return: None
        """

    def create(self, validated_data):
        """
        Request serializers of this project do not create DB records
        :param validated_data: validated data
        :return: None
        """
