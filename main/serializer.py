from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Tag, Product, Review


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
        fields = ['id', 'title', 'description', 'price', 'tags', 'reviews']

    def get_tags(self, product):
        return TagSerializer(product.tags.filter(is_active=True), many=True).data


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=5, max_length=25)
    description = serializers.CharField()
    price = serializers.IntegerField()
    tags = serializers.ListField()

    def validate_title(self, title):
        if Product.objects.filter(title=title):
            raise ValidationError("This product already exist!")

