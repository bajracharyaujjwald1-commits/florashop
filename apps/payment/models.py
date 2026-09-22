from django.db import models
from apps.purchase.models import Purchase



class PaymentMethod(models.TextChoices):
        KHALTI = "KHALTI", "Khalti"


class TransactionStatus(models.TextChoices):
    PENDING = "PENDING", "Pending" 
    COMPLETED = "COMPLETED", "Completed"
    FAILED = "FAILED", "Failed"
    REFUNDED = "REFUNDED", "Refunded"

class Transaction(models.Model):
    purchase = models.OneToOneField(
        Purchase, on_delete=models.CASCADE, related_name="transaction"
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,
        default=PaymentMethod.KHALTI,
    )
    status = models.CharField(
        max_length=20,
        choices=TransactionStatus.choices,
        default=TransactionStatus.PENDING,
    )
    pidx = models.CharField(
        max_length=255, unique=True, null=True, blank=True
    )
    transaction_id = models.CharField(
        max_length=255, null=True, blank=True
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transaction {self.pidx or self.id} - {self.status}"