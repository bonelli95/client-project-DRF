from rest_framework import viewsets, filters
from clients.serializers import ClientSerializer
from clients.models import Client
from django_filters.rest_framework import DjangoFilterBackend

class ClientsViewSet(viewsets.ModelViewSet):
    """Listing customers"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'tin']
    filterset_fields = ['active']
