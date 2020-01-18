from rest_framework import serializers

from plateiq.core.models.invoice import DigitalInvoice, InvoiceItem
from plateiq.core.serializers.common_serializer import AddressSerializer
from plateiq.p_admin.serializers.invoice_item_serializer import InvoiceItemSerializer


class DigitalInvoiceSerializer(serializers.ModelSerializer):
    vendor_address = AddressSerializer()
    buyer_address = AddressSerializer()

    class Meta:
        model = DigitalInvoice
        fields = (
            'code', 'raw_invoice_id', 'invoice_number', 'invoice_date', 'due_date', 'vendor_name', 'vendor_address',
            'buyer_name', 'buyer_address', 'sub_total', 'tax_percentage', 'tax_applicable', 'discount_percentage',
            'discount_applicable', 'amount_payable', 'is_paid', 'created_on', 'updated_on')


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

    def create(self, validated_data):
        vendor_address = validated_data.pop('vendor_address', None)
        buyer_address = validated_data.pop('buyer_address', None)
        invoice_items = validated_data.pop('invoice_items', None)

        if vendor_address:
            vendor_address_serializer = self.fields['vendor_address']
            vendor_address = vendor_address_serializer.create(vendor_address)
            validated_data['vendor_address'] = vendor_address

        if buyer_address:
            buyer_address_serializer = self.fields['buyer_address']
            buyer_address = buyer_address_serializer.create(buyer_address)
            validated_data['buyer_address'] = buyer_address

        digital_invoice = DigitalInvoice.objects.create(**validated_data)
        if invoice_items:
            self._add_invoice_items(digital_invoice, invoice_items)

        return digital_invoice

    def update(self, instance, validated_data):
        vendor_address_data = validated_data.pop('vendor_address', None)
        buyer_address_data = validated_data.pop('buyer_address', None)
        invoice_items = self.initial_data.get('invoice_items', [])

        for item in invoice_items:
            item_id = item.get('id', None)
            if item_id:
                inv_item = InvoiceItem.objects.get(id=item_id, digital_invoice_id=instance)
                inv_item.description = item.get('description', inv_item.description)
                inv_item.quantity = item.get('quantity', inv_item.quantity)
                inv_item.unit_price = item.get('unit_price', inv_item.unit_price)
                inv_item.total_price = item.get('total_price', inv_item.total_price)
                inv_item.save()
            else:
                InvoiceItem.objects.create(digital_invoice_id=instance, **item)

        buyer_address = instance.buyer_address
        if buyer_address_data:
            if buyer_address:
                buyer_address.street_address = buyer_address_data.get('street_address', buyer_address.street_address)
                buyer_address.city = buyer_address_data.get('city', buyer_address.city)
                buyer_address.state = buyer_address_data.get('state', buyer_address.state)
                buyer_address.postal_code = buyer_address_data.get('postal_code', buyer_address.postal_code)
                buyer_address.save()
                instance.buyer_address = buyer_address
            else:
                buyer_address_serializer = self.fields['buyer_address']
                buyer_address = buyer_address_serializer.create(buyer_address_data)
                instance.buyer_address = buyer_address

        vendor_address = instance.vendor_address
        if vendor_address_data:
            if vendor_address:
                vendor_address.street_address = vendor_address_data.get('street_address', vendor_address.street_address)
                vendor_address.city = vendor_address_data.get('city', vendor_address.city)
                vendor_address.state = vendor_address_data.get('state', vendor_address.state)
                vendor_address.postal_code = vendor_address_data.get('postal_code', vendor_address.postal_code)
                vendor_address.save()
                instance.vendor_address = vendor_address
            else:
                vendor_address_serializer = self.fields['vendor_address']
                vendor_address = vendor_address_serializer.create(vendor_address_data)
                instance.vendor_address = vendor_address

        # Digital Invoice Fields
        instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
        instance.invoice_date = validated_data.get('invoice_date', instance.invoice_date)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.vendor_name = validated_data.get('vendor_name', instance.vendor_name)
        instance.buyer_name = validated_data.get('buyer_name', instance.buyer_name)
        instance.sub_total = validated_data.get('sub_total', instance.sub_total)
        instance.tax_percentage = validated_data.get('tax_percentage', instance.tax_percentage)
        instance.tax_applicable = validated_data.get('tax_applicable', instance.tax_applicable)
        instance.discount_percentage = validated_data.get('discount_percentage', instance.discount_percentage)
        instance.discount_applicable = validated_data.get('discount_applicable', instance.discount_applicable)
        instance.amount_payable = validated_data.get('amount_payable', instance.amount_payable)
        instance.is_paid = validated_data.get('is_paid', instance.is_paid)

        instance.save()

        return instance

    def _add_invoice_items(self, digital_invoice, invoice_items):
        if invoice_items and isinstance(invoice_items, list):
            for invoice_item in invoice_items:
                invoice_item['digital_invoice_id'] = digital_invoice
            invoice_item_serializer = self.fields['invoice_items']
            invoice_item_serializer.create(invoice_items)
