import pytest
from rest_framework import status
from rest_framework.test import APIClient

from apps.products.models import Product
from apps.tests.factories import ProductFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def products():
    return ProductFactory.create_batch(2)


class TestProductView:
    url = '/api/v1/products/'

    def test_create_product_succefully(self, client):
        data = {"title":"Produto Demo sem categoria",
                "description":"Produto Demo criado para demonstração",
                "avatar_url":"https:asdvgh.fgfds.com/asd-asdasf.jpg",
                "stock": 1,
                "price": 12.00}

        response = client.post(self.url, data)
        assert response.status_code == status.HTTP_201_CREATED

        response_json = response.json()
        assert response_json['title'] == data['title']
        assert response_json['description'] == data['description']
        assert response_json['avatar_url'] == data['avatar_url']
        assert response_json['stock'] == data['stock']
        assert response_json['price'] == data['price']


    def test_create_product_with_wrong_payload(self, client):
        data = {'title':'Produto para teste'}

        response = client.post(self.url, data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        response_json = response.json()
        assert response_json == {'avatar_url': ['This field is required.'], 
                                 'description': ['This field is required.'],
                                 'price': ['This field is required.'],
                                 'stock': ['This field is required.']}


    def test_list_products_succefully(self, client, products):
        response = client.get(self.url)

        assert response.status_code == status.HTTP_200_OK

        response_json = response.json()
        assert len(response_json) == 2
        assert response_json[0]['id'] == str(products[0].id)
        assert response_json[0]['title'] == products[0].title
        assert response_json[0]['description'] == products[0].description 
        assert response_json[0]['avatar_url'] == products[0].avatar_url 


class TestProductDetailView:
    url = '/api/v1/products/{}'

    def test_get_product_detail_succefully(self, client, products):
        product = products[0]

        response = client.get(self.url.format(product.id))
        assert response.status_code == status.HTTP_200_OK

        response_json = response.json()
        assert response_json['id'] == str(product.id)
        assert response_json['title'] == product.title
        assert response_json['description'] == product.description

    def test_update_product_succefully(self, client, products):
        product = products[0]
        new_product_title = 'new product name'
        response = client.patch(
            self.url.format(product.id), data={'title': new_product_title}
        )
        assert response.status_code == status.HTTP_200_OK

        response_json = response.json()
        assert response_json['title'] == new_product_title    

    def test_delete_product_succefully(self, client, products):
        assert Product.objects.count() == 2

        product = products[0]
        response = client.delete(self.url.format(product.id))

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Product.objects.count() == 1

    @pytest.mark.parametrize(
        'action',
        ['get', 'patch', 'delete'],
        ids=['get_product', 'patch_product', 'delete_product'],
    )
    def test_product_with_not_found_id(self, action, client):
        client_request = getattr(client, action)
        response = client_request(
            self.url.format(123), data={'name': 'new product name'}
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND        