from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer, ReviewSerializer, TagSerializer, ProductCreateValidateSerializer
from .models import Product, Review, Tag


@api_view(['GET'])
def get_product(request):
    product = Product.objects.all()
    data = ProductSerializer(product, many=True).data
    return Response(data=data)


@api_view(['GET', 'PUT', 'DELETE'])
def get_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Product not found!'})
    if request.method == 'GET':
        data = ProductSerializer(product).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = ProductCreateValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'message': 'error', 'errors': serializer.errors})
        product.title = request.data['title']
        product.description = request.data['description']
        product.price = request.data['price']
        product.category_pk = request.data['category']
        product.tags.set(request.data['tags'])
        product.save()
        return Response(data={'massage': 'Product updated!'})
    else:
        product.delete()
        return Response()


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


