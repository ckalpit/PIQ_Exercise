from rest_framework import viewsets

from plateiq.core.models.invoice import InvoiceItem
from plateiq.p_admin.serializers import InvoiceItemSerializer


class InvoiceItemView(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
