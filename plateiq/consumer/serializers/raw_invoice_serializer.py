from rest_framework import serializers

from plateiq.core.models.invoice import RawInvoice


class RawInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawInvoice
        fields = '__all__'
