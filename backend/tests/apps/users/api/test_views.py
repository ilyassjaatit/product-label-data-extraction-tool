from django.urls import reverse

import pytest
from rest_framework import status

USERS_ENDPOINT = "/api/users/"

pytestmark = pytest.mark.django_db


def test_user_list_not_authorized(api_client):
    response = api_client.get(reverse("api:user-list"))
    assert reverse("api:user-list") == USERS_ENDPOINT
    assert response.status_code == status.HTTP_403_FORBIDDEN
