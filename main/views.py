from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer, ReviewSerializer, TagSerializer
from .models import Product, Review, Tag


@api_view(['GET'])
def get_product(request):
    product = Product.objects.all()
    data = ProductSerializer(product, many=True).data
    return Response(data=data)


@api_view(['GET'])
def get_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Product not found!'})
    data = ProductSerializer(product).data
    return Response(data=data)


@api_view(['GET'])
def get_review(request):
    review = Review.objects.all()
    data = ReviewSerializer(review, many=True).data
    return Response(data=data)


@api_view(['GET'])
def get_tags(request):
    tag = Tag.objects.filter(is_active=True)
    data = TagSerializer(tag, many=True).data
    return Response(data=data)
