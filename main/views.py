from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import CategorySerializer, TagSerializer, ProductSerializer, ReviewSerializer
from .models import Category, Tag, Product, Review

@api_view(['GET'])
def get_product(request):
    product = Product.objects.all()
    data = ProductSerializer(product, many=True).data
    return Response(data=data)

@api_view(['GET'])
def get_review(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Movie not found!'})
    data = ReviewSerializer(review).data
    return Response(data=data)












