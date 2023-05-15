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

    def create(self, request):
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'visitor/list.html', {'visitors': serializer.data})
        else:
            return render(request, 'visitor/create.html', {'serializer': serializer.data})
