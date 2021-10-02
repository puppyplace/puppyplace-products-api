from rest_framework import serializers

from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class ProductDetailSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        lookup_url_kwarg = 'id'
