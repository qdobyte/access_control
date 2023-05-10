from rest_framework import serializers
from apps.users.models.visitor import Visitor


class VisitorSerializer(serializers.ModelSerializer):
    """ Visitor serializer """

    class Meta:
        """ Metaclass for VisitorSerializer class """
        model = Visitor
        fields = '__all__'
