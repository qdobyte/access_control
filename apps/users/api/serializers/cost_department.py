from rest_framework import serializers
from apps.users.models.cost_department import CostDepartment


class CostDepartmentSerializer(serializers.ModelSerializer):
    """ CostDepartment serializer

    Args:
        serializers (ModelSerializer): Model serializer
    """

    class Meta:
        """ Metaclass for CostDepartmentSerializer class """
        model = CostDepartment
        fields = '__all__'
