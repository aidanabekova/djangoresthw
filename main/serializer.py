from rest_framework import serializers
from .models import Category, Tag, Product, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text '.split()


class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    # tags = TagSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'tags', 'reviews']

    def get_tags(self, product):
        return TagSerializer(product.tags.filter(is_active=True), many=True).data
