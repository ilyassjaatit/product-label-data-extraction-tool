import pytest

from apps.products.models import Product, ProductRawData

pytestmark = pytest.mark.django_db


def test_create_product_row_data():
    product_row_data = ProductRawData(name="test name", raw_data={})
    product_row_data.save()
    assert ProductRawData.objects.count() >= 1


def test_create_product():
    product = Product(name="test name")
    product.save()
    assert Product.objects.count() >= 1
