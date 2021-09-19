from django.urls import reverse


def test_view_test_selenium(client):
    url = reverse("view-test-selenium")
    response = client.get(url)
    assert response.status_code == 200
