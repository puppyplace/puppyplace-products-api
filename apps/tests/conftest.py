import pytest

from rest_framework.test import APIClient
from apps.tests.factories import ProductFactory

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def products():
    return ProductFactory.create_batch(2)
