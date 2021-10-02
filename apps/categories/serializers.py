from rest_framework import serializers

from apps.categories.models import Category
from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()

    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class CategoryDetailSerializer(CategorySerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        lookup_url_kwarg = 'id'


class ProductPerCategorySerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = '__all__'
