from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


from apps.users.api.serializers.visitor import VisitorSerializer
from apps.users.models.visitor import Visitor


class VisitorViewSet(viewsets.ModelViewSet):
    """ Visitor view set."""

    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

    def list(self, request):
        visitors = self.get_queryset()
        return render(request, 'visitor/list.html', {'visitors': visitors})

    def retrieve(self, request, pk=None):
        visitor = self.get_object()
        return render(request, 'visitor/detail.html', {'visitor': visitor})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            visitors = self.get_queryset()
            return render(request, 'visitor/list.html', {'visitors': visitors})
        return render(request, 'visitor/create.html', {'serializer': serializer})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            visitors = self.get_queryset()
            return render(request, 'visitor/list.html', {'visitors': visitors})
        return render(request, 'visitor/update.html', {'serializer': serializer})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response({'message': 'Visitor deleted successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'Visitor not found'}, status=status.HTTP_404_NOT_FOUND)
