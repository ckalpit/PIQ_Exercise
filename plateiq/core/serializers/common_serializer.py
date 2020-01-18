from rest_framework import serializers

from plateiq.core.models.common import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
