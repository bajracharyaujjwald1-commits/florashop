from django.contrib import admin
from apps.payment.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    # Columns displayed in the list table
    list_display = (
        "id",
        "purchase",
        "payment_method",
        "status",
        "amount",
        "pidx",
        "created_at",
    )

    # Sidebar filters
    list_filter = (
        "payment_method",
        "status",
        "created_at",
    )

    # Search fields (searches through purchase number via relational lookup as well)
    search_fields = (
        "pidx",
        "transaction_id",
        "purchase__purchase_number",
        "purchase__invoice_number",
    )

    # Read-only fields to prevent manual tampering with transaction logs
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    # Group fields into structured sections in the detail view
    fieldsets = (
        (
            "Order Information",
            {
                "fields": ("purchase", "amount"),
            },
        ),
        (
            "Payment Gateway Details",
            {
                "fields": (
                    "payment_method",
                    "status",
                    "pidx",
                    "transaction_id",
                ),
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
            },
        ),
    )