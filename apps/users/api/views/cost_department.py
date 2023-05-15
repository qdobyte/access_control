from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.users.api.serializers.cost_department import CostDepartmentSerializer
from apps.users.models.cost_department import CostDepartment


class CostDepartmentViewSet(viewsets.ModelViewSet):
    """ Cost Department view set."""

    queryset = CostDepartment.objects.all()
    serializer_class = CostDepartmentSerializer




