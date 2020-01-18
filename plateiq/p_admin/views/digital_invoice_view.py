from rest_framework import viewsets, status
from rest_framework.response import Response

from plateiq.core.models.invoice import DigitalInvoice
from plateiq.p_admin.serializers import DigitalInvoiceSerializer, DigitalInvoiceDetailSerializer


class DigitalInvoiceView(viewsets.ModelViewSet):
    queryset = DigitalInvoice.objects.all()
    serializer_class = DigitalInvoiceSerializer

    http_method_names = ['get']


class DigitalInvoiceDetailView(viewsets.ModelViewSet):
    serializer_class = DigitalInvoiceDetailSerializer

    def get_queryset(self):
        queryset = DigitalInvoice.objects.all()
        raw_invoice_id = self.request.query_params.get('inv_id', None)
        if raw_invoice_id is not None:
            queryset = queryset.filter(raw_invoice_id=raw_invoice_id)
        return queryset

    def create(self, request, *args, **kwargs):
        if self.request and hasattr(self.request, "data"):
            digital_invoice_data = self._add_digital_invoice()
            headers = self.get_success_headers(digital_invoice_data)
            return Response(digital_invoice_data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def _add_digital_invoice(self):
        raw_invoice_id = self.request.data.get('raw_invoice_id')
        code = 'DI-{0}'.format(raw_invoice_id)
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(code=code)
        return serializer.data
