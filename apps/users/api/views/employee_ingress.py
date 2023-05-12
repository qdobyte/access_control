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
        """
        Create a new EmployeeIngress instance.

        Args:
            request (Request): The incoming request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The response object with a success or error message.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'EmployeeIngress created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Update an existing EmployeeIngress instance.

        Args:
            request (Request): The incoming request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The response object with a success or error message.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            # Check if egress_time is being set
            if 'egress_time' in request.data and request.data['egress_time'] is not None:
                # Update is_inside to False
                request.data['is_inside'] = False
            self.perform_update(serializer)
            return Response({'message': 'EmployeeIngress updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Destroy an existing EmployeeIngress instance.

        Args:
            request (Request): The incoming request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The response object with a message indicating that deleting EmployeeIngress is not allowed.
        """
        return Response({'message': 'Deleting EmployeeIngress is not allowed'},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)
