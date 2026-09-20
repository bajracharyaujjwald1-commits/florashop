from decimal import Decimal

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from apps.products.models import Product
from django.shortcuts import render
import uuid
from django.shortcuts import get_object_or_404, redirect
from apps.purchase.models import Purchase, PaymentStatus


def purchase_view(request):
    # ID 1 = Dried and Fresh Florals
    florals = Product.objects.filter(Category_id=1, is_available=True)

    # ID 2 = Plants and Living greenery
    plants = Product.objects.filter(Category_id=2, is_available=True)

    # ID 3 = Gifts and Home Goods
    gifts = Product.objects.filter(Category_id=3, is_available=True)

    context = {
        "florals": florals,
        "plants": plants,
        "gifts": gifts,
    }
    return render(request, "purchase/products.html", context)

@login_required
def create_purchase_view(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    sub_total = product.price
    discount = Decimal(0.00)
    total = sub_total - discount
    if request.method == "POST":
        purchase_no = f"PUR-{uuid.uuid4().hex[:8].upper()}"
        invoice_no = f"INV-{uuid.uuid4().hex[:8].upper()}"

        purchase = Purchase.objects.create(
            purchase_number = purchase_no,
            invoice_number = invoice_no,
            purchase_date = timezone.now().date(),
            sub_total = sub_total,
            discount = discount,
            total = total,
            is_purchase_verified = False,
            payment_status = PaymentStatus.PENDING,


        )
        return redirect("purchase:purchase_detail", purchase_id = purchase.id)

    context = {
        "product": product,
        "sub_total": sub_total,
        "discount": discount,
        "total": total,
    }
    return render(request, "purchase/confirm_purchase.html", context)

@login_required
def purchase_detail_view(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)
    return render(
        request, "purchase/purchase_detail.html",{"purchase":purchase}
    )
