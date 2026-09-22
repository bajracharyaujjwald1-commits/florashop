from django.db import models
from apps.products.models import Product
from django.conf import settings
# Create your models here.


class PaymentStatus(models.TextChoices):
    PENDING = 'pending', 'pending'
    PAID = 'paid', 'paid'
    UNPAID = 'unpaid', 'unpaid'
    CANCELLED = 'cancelled','cancelled'

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    purchase_number = models.CharField(max_length=50, unique=True)
    purchase_date = models.DateField()
    invoice_number = models.CharField(max_length=50, null =True, blank= True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_purchase_verified = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'purchase'

    def __str__(self):
        return self.purchase_number
    