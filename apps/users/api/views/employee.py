from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.users.api.serializers.employee import EmployeeSerializer
from apps.users.models.employee import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    """ Employee view set."""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Employee created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({'message': 'Employee updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response({'message': 'Employee deleted successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)