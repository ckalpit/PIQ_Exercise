import hashlib

from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from plateiq.core.models.invoice import RawInvoice
from plateiq.p_admin.serializers import RawInvoiceSerializer
from plateiq.p_admin.serializers.raw_invoice_serializer import RawInvoiceStatusSerializer


class InvoiceView(viewsets.ModelViewSet):
    queryset = RawInvoice.objects.all()
    serializer_class = RawInvoiceSerializer

    http_method_names = ['get']

    def perform_create(self, serializer):
        if self.request and hasattr(self.request, "data"):
            file_name = self.request.data['file'].name
            hash_object = hashlib.md5(file_name.encode('utf-8'))
            file_hash = hash_object.hexdigest()
            code = 'RI-{0}-{1}'.format(self.request.data['uploaded_by'], file_hash)
            serializer.save(code=code, file_name=file_name)


class UpdateInvoiceStatusView(mixins.UpdateModelMixin, GenericViewSet):
    queryset = RawInvoice.objects.all()
    serializer_class = RawInvoiceStatusSerializer
    http_method_names = ['patch']
