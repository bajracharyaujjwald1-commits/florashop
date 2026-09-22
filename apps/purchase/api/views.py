from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from apps.purchase.api.serializer import PurchaseSerializer
from apps.purchase.models import Purchase
from rest_framework.decorators import APIView
from datetime import datetime

class PurchaseView(GenericAPIView):
    queryset = Purchase
    serializer_class = PurchaseSerializer

    def get(self, request, *args, **kwargs):
        data = Purchase.objects.all()
        serializer = self.get_serializer(data,many =True)
        return Response(serializer.data)

    def post(self, request):
        data =request.data
        serializer = self.get_serializer(data, may =True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Purchase has been created successfully"
            })

        return Response(serializer.errors)

class UpdatePurchaseView(GenericAPIView):
    queryset = Purchase
    serializer_class = PurchaseSerializer

    def get(self, request, id):
        data = get_object_or_404(Purchase, id=id)
        serializer=self.get_serializer(data)
        return Response(serializer.data)

    def put(self, request, id):
        data = get_object_or_404(Purchase, id=id)
        serializer=self.get_serializer(data, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Purchase updated successfully"
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self,request,id):
        data = get_object_or_404(Purchase, id=id)
        data.delete()

        return Response({
            "message":"Purchase Deleted Successfully"
        }, status=status.HTTP_204_NO_CONTENT)
