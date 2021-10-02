from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from apps.categories.models import Category
from apps.categories.serializers import (
    CategoryDetailSerializer,
    CategorySerializer,
    ProductPerCategorySerializer,
)
from apps.products.models import Product


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class ProductPerCategoryView(ListAPIView):
    serializer_class = ProductPerCategorySerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)
