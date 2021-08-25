from rest_framework import mixins, viewsets

from apps.products.models import ProductRawData

from .serializers import ProductRawDataSerializer


class ProductRawDataViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ProductRawData.objects.all()
    serializer_class = ProductRawDataSerializer
