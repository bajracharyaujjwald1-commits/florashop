from rest_framework import serializers
from apps.purchase.models import Purchase, PaymentStatus

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"