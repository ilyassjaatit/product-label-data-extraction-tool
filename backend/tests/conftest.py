import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from tests.factories import UserFactory

# Register factories to pytest global namespace.
# They can be access as normal fixtures using user_factory or job_factory.
register(UserFactory)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def api_client_authenticate(db, user_factory, api_client):
    def _api_client(user=None):
        """Allows pass custom user object."""
        if user is None:
            user = user_factory()
        api_client.force_authenticate(user=user)
        return api_client

    yield _api_client
    api_client.force_authenticate(user=None)
