from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'tags', 'reviews']

    def get_tags(self, product):
        return TagSerializer(product.tags.filter(is_active=True), many=True).data


class ProductCreateValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=200)
    description = serializers.CharField()
    price = serializers.IntegerField()
    category = serializers.IntegerField()
    tags = serializers.ListField()

    def validate_title(self, title):
        if Product.objects.filter(title=title):
            raise ValidationError("This cap already exist!")
