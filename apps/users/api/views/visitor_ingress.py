from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.users.api.serializers.visitor_ingress import VisitorIngressSerializer
from apps.users.models.visitor_ingress import VisitorIngress


class VisitorIngressViewSet(viewsets.ModelViewSet):
    """ VisitorIngress view set."""

    queryset = VisitorIngress.objects.all()
    serializer_class = VisitorIngressSerializer

    def update(self, request, *args, **kwargs):
        """
        Update an existing VisitorIngress instance.

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
            return Response({'message': 'VisitorIngress updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

