from rest_framework import serializers
from apps.users.models.cost_center import CostCenter


class CostCenterSerializer(serializers.ModelSerializer):
    """ CostCenter serializer

    Args:
        serializers (ModelSerializer): Model serializer
    """

    class Meta:
        """ Metaclass for CostCenterSerializer class """
        model = CostCenter
        fields = '__all__'
