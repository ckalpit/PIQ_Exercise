from rest_framework import viewsets

from plateiq.core.models.common import Address
from plateiq.core.serializers.common_serializer import AddressSerializer


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
