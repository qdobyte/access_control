from datetime import datetime, time

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.users.api.serializers.employee_ingress import EmployeeIngressSerializer
from apps.users.models.employee_ingress import EmployeeIngress


class EmployeeIngressViewSet(viewsets.ModelViewSet):
    """ EmployeeIngress view set."""

    queryset = EmployeeIngress.objects.all()
    serializer_class = EmployeeIngressSerializer

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
        LIMIT_TIME = time(hour=16)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial, many=False)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Check if egress_time is being set and if employee is leaving before 16:00
        egress_time = request.data.get('egress_time')
        if egress_time:
            egress_time = datetime.strptime(egress_time, '%Y-%m-%d %H:%M:%S.%f')
            if egress_time.time() < LIMIT_TIME:
                # Ask for reason of leaving
                reason = request.data.get('reason_for_leaving')
                if reason not in ['CITA', 'CALAMIDAD', 'DILIGENCIA']:
                    return Response({
                        'message': 'Invalid reason for leaving. Allowed values are "Cita médica", '
                                   '"calamidad", or "diligencia personal".'
                    }, status=status.HTTP_400_BAD_REQUEST)
            request.data['is_inside'] = False

        if serializer.validated_data:
            self.perform_update(serializer)
            return Response({'message': 'EmployeeIngress updated successfully'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

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
