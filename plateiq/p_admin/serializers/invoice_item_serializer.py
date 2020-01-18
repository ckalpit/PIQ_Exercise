from rest_framework import serializers

from plateiq.core.models.invoice import InvoiceItem, DigitalInvoice


class InvoiceItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    digital_invoice_id = serializers.PrimaryKeyRelatedField(queryset=DigitalInvoice.objects.all())

    class Meta:
        model = InvoiceItem
        fields = '__all__'
