from django.urls import reverse

import pytest
from rest_framework import status

PRODUCT_RAW_DATA_ENDPOINT = "/api/product-raw-data/"

pytestmark = pytest.mark.django_db


def test_product_raw_data_list_not_authorized(api_client):
    response = api_client.get(reverse("api:productrawdata-list"))
    assert reverse("api:productrawdata-list") == PRODUCT_RAW_DATA_ENDPOINT
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_product_raw_data_list_authorized(api_client_authenticate):
    response = api_client_authenticate().get(reverse("api:productrawdata-list"))
    assert reverse("api:productrawdata-list") == PRODUCT_RAW_DATA_ENDPOINT
    assert response.status_code == status.HTTP_200_OK
