from rest_framework import serializers
from apps.users.models.visitor_ingress import VisitorIngress


class VisitorIngressSerializer(serializers.ModelSerializer):
    """ VisitorIngress serializer"""

    class Meta:
        """ Metaclass for VisitorIngressSerializer class """
        model = VisitorIngress
        fields = '__all__'
