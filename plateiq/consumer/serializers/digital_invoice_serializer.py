from rest_framework import serializers

from plateiq.consumer.serializers.invoice_item_serializer import InvoiceItemSerializer
from plateiq.core.models.invoice import DigitalInvoice
from plateiq.core.serializers.common_serializer import AddressSerializer


class DigitalInvoiceDetailSerializer(serializers.ModelSerializer):
    vendor_address = AddressSerializer(required=False)
    buyer_address = AddressSerializer(required=False)
    invoice_items = InvoiceItemSerializer(many=True, read_only=True)

    class Meta:
        model = DigitalInvoice
        fields = (
            'code', 'raw_invoice_id', 'invoice_number', 'invoice_date', 'due_date', 'vendor_name', 'vendor_address',
            'buyer_name', 'buyer_address', 'sub_total', 'tax_percentage', 'tax_applicable', 'discount_percentage',
            'discount_applicable', 'amount_payable', 'is_paid', 'created_on', 'updated_on', 'invoice_items')
        extra_kwargs = {'code': {'read_only': True, 'required': False}}

    def to_representation(self, instance):
        representation = super(DigitalInvoiceDetailSerializer, self).to_representation(instance)
        representation['invoice_items'] = InvoiceItemSerializer(instance.invoiceitem_set.all(), many=True).data
        return representation
