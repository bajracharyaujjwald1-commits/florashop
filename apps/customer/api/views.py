from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import request, status

from apps.customer.api.serializers import CustomerSerializer
from apps.customer.models import Customer

from django.shortcuts import get_object_or_404

class CustomerView(GenericAPIView):
    queryset = Customer
    serializer_class = CustomerSerializer

    def get(self, *args, **kwargs):
        data = Customer.objects.all()
        serializer = self.get_serializer(data, many =True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Customer Created Successfully"
            })
        else:
            return Response(serializer.errors)
