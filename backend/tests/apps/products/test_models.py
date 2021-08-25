import pytest

from apps.products.models import Product, ProductRowData

pytestmark = pytest.mark.django_db


def test_create_product_row_data():
    product_row_data = ProductRowData(name="test name", row_data={})
    product_row_data.save()
    assert ProductRowData.objects.count() >= 1


def test_create_product():
    product = Product(name="test name")
    product.save()
    assert Product.objects.count() >= 1
