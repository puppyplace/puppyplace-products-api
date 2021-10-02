import pytest

from apps.tests.factories import CategoryFactory


@pytest.fixture
def categories():
    return CategoryFactory.create_batch(2)
