from rest_framework import serializers
from apps.users.models.employee import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """ Employee serializer

    Args:
        serializers (ModelSerializer): Model serializer
    """

    class Meta:
        """ Metaclass for EmployeeSerializer class """
        model = Employee
        fields = '__all__'
