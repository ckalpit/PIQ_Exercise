from rest_framework import serializers

from plateiq.core.models.invoice import RawInvoice


class RawInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawInvoice
        fields = '__all__'


class RawInvoiceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawInvoice
        fields = ('id', 'code', 'status')
