from rest_framework import viewsets

from plateiq.consumer.serializers import DigitalInvoiceDetailSerializer
from plateiq.core.models.invoice import DigitalInvoice


class DigitalInvoiceView(viewsets.ModelViewSet):
    serializer_class = DigitalInvoiceDetailSerializer

    http_method_names = ['get']

    def get_queryset(self):
        queryset = DigitalInvoice.objects.all()
        raw_invoice_id = self.request.query_params.get('inv_id', None)
        if raw_invoice_id is not None:
            queryset = queryset.filter(raw_invoice_id=raw_invoice_id)
        return queryset
