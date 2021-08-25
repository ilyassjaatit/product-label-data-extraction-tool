from rest_framework import serializers

from apps.products.models import ProductRawData


class ProductRawDataSerializer(serializers.ModelSerializer):
    """User Serializer"""

    class Meta:
        model = ProductRawData
        fields = ["id", "name", "raw_data"]
