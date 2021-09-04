from rest_framework import serializers

from apps.categories.models import Category


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
