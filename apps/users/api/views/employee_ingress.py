from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.users.api.serializers.employee_ingress import EmployeeIngressSerializer
from apps.users.models.employee_ingress import EmployeeIngress


class EmployeeIngressViewSet(viewsets.ModelViewSet):
    """ EmployeeIngress view set."""

    queryset = EmployeeIngress.objects.all()
    serializer_class = EmployeeIngressSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'EmployeeIngress created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({'message': 'EmployeeIngress updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return Response({'message': 'Deleting EmployeeIngress is not allowed'},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)