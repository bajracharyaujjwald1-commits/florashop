from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.products.api.serializers import ProductSerializers
from django.shortcuts import get_object_or_404

from apps.products.models import Product
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from apps.products.api.serivice import Access_grant

class ProductView(GenericAPIView):
    queryset = Product
    serializer_class = ProductSerializers
    permission_classes = [Access_grant]

    def get(self, request, *args, **kwargs):
        data = Product.objects.all()
        serializer = self.get_serializer(data, many = True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Product created Successfully"
            })
        else:
            return Response(serializer.errors)

class UpdateProductView(GenericAPIView):
    queryset = Product
    serializer_class = ProductSerializers

    def get(self, request, id):
        data = get_object_or_404(Product, id=id)
        serializer = self.get_serializer(data)
        return Response(serializer.data)

    def put(self, request,id):
        data = get_object_or_404(Product, id = id)
        serializer = self.get_serializer(data, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Product Updated Successfully"
            })
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        data = get_object_or_404(Product, id= id)
        data.delete()
        return Response({
            "message":"Product deleted Successfully"
        }, status.HTTP_204_NO_CONTENT)