import pytest
from rest_framework import status
from rest_framework.test import APIClient

from apps.categories.models import Category
from apps.tests.factories import CategoryFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def categories():
    return CategoryFactory.create_batch(2)


class TestCategoryView:
    url = '/api/v1/categories/'

    def test_create_category_succefully(self, client):
        data = {'name': 'category_1'}
        response = client.post(self.url, data)

        assert response.status_code == status.HTTP_201_CREATED

        response_json = response.json()
        assert type(response_json['id']) == str
        assert response_json['name'] == data['name']

    def test_create_category_with_wrong_payload(self, client):
        response = client.post(self.url, {'teste': 123})

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        response_json = response.json()
        assert response_json == {'name': ['This field is required.']}

    def test_list_categories_succefully(self, client):
        categories = CategoryFactory.create_batch(2)
        response = client.get(self.url)

        assert response.status_code == status.HTTP_200_OK

        response_json = response.json()
        assert len(response_json) == 2

class TestCategoryDetailView:
    url = '/api/v1/categories/{}'

    def test_get_category_detail_succefully(self, client, categories):
        category = categories[0]

        response = client.get(self.url.format(category.id))
        assert response.status_code == status.HTTP_200_OK

        response_json = response.json()
        assert response_json['id'] == str(category.id)
        assert response_json['name'] == category.name

    def test_update_category_succefully(self, client, categories):
        category = categories[0]
        new_category_name = 'new category name'
        response = client.patch(
            self.url.format(category.id), data={'name': new_category_name}
        )
        assert response.status_code == status.HTTP_200_OK

        response_json = response.json()
        assert response_json['name'] == new_category_name

    def test_delete_category_succefully(self, client, categories):
        assert Category.objects.count() == 2

        category = categories[0]
        response = client.delete(self.url.format(category.id))

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Category.objects.count() == 1

    @pytest.mark.parametrize(
        'action',
        ['get', 'patch', 'delete'],
        ids=['get_category', 'patch_category', 'delete_category'],
    )
    def test_category_with_not_found_id(self, action, client):
        client_request = getattr(client, action)
        response = client_request(
            self.url.format(123), data={'name': 'new category name'}
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND
