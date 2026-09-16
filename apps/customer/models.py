from django.conf import settings
from django.db import models


class Customer(models.Model):
    username = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="customer_profile",
    )
    email = models.CharField(max_length=50, verbose_name="email", null=True)

    def __str__(self):
        return str(self.username)

    class Meta:
        db_table = "customer"