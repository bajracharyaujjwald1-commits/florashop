from django.db import models

# Create your models here.
class Category(models.Model):
    """
    florals, plants or gifts
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "Product_Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    """Product name"""

    Category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Prices in NPR"
    )
    description = models.CharField(max_length=500, null = True, blank= True)
    image =models.ImageField(upload_to="products/", null = True, blank= True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

