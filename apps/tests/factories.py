from uuid import uuid4

import factory

from apps.categories.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    id = factory.LazyFunction(uuid4)
    name = factory.Sequence(lambda n: f'category_{n}')
