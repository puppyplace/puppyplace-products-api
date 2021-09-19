from uuid import uuid4
import datetime
import factory
import factory.fuzzy

from apps.categories.models import Category
from apps.products.models import Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    id = factory.LazyFunction(uuid4)
    name = factory.Sequence(lambda n: f'category_{n}')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    id = factory.LazyFunction(uuid4)
    description = factory.Sequence(lambda n: f'product_{n}')
    title = factory.Sequence(lambda n: f'product_title_{n}')
    avatar_url = factory.Sequence(lambda n: f'avatar_url_{n}')
    partner = factory.LazyFunction(uuid4)
    created_at = factory.LazyFunction(datetime.datetime.now)
    stock = factory.fuzzy.FuzzyInteger(1)
    price = factory.fuzzy.FuzzyFloat(42.7)
    category = factory.SubFactory(CategoryFactory)
