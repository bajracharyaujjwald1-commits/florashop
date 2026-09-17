from rest_framework import serializers
from apps.customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):

    username = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Customer
        fields = "__all__"