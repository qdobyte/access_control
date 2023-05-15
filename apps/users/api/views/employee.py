from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, status

from apps.users.api.serializers.employee import EmployeeSerializer
from apps.users.models.employee import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    """ Employee view set."""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request):
        employees = self.get_queryset()
        return render(request, 'employee/list.html', {'employees': employees})

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'employee/list.html', {'employees': serializer.data})
        else:
            return render(request, 'employee/create.html', {'serializer': serializer.data})
