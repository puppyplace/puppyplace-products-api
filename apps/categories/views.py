from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.categories.models import Category
from apps.categories.serializers import CategoryDetailSerializer, CategorySerializer


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
