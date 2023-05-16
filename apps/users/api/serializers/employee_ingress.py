from rest_framework import serializers

from apps.users.models.employee_ingress import EmployeeIngress


class EmployeeIngressSerializer(serializers.ModelSerializer):
    """ EmployeeIngress serializer

    Args:
        serializers (ModelSerializer): Model serializer
    """

    class Meta:
        """ Metaclass for EmployeeIngressSerializer class """
        model = EmployeeIngress
        fields = '__all__'
