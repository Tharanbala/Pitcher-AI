from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Product
from .serializers import ProductSerializer
from .utils import getPerplex
# Create your views here.

class ProductSearch(APIView):

    # # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    #get product details from db
    def get(self, request, *args, **kwargs):

        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #add product in db
    def post(self, request, *args, **kwargs):
        result = getPerplex(request.data.get('name'))
        print(result)
        data = {
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'dimensions': request.data.get('dimensions'),
            'pros': request.data.get('pros'),
            'cons': request.data.get('cons'),
            'reviews': request.data.get('reviews'),
            'stars': request.data.get('stars')
        }

        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)