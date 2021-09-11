from rest_framework import serializers

from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()

    class Meta:
        model = Product
        fields = ['id', 'name']
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class ProductDetailSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']
        lookup_url_kwarg = 'id'
