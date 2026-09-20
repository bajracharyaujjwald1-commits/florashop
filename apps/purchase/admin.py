from django.contrib import admin
from django.utils.html import format_html
from apps.purchase.models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    # Columns displayed in the list view
    list_display = (
        "purchase_number",
        "invoice_number",
        "purchase_date",
        "total",
        "colored_payment_status",
        "is_purchase_verified",
        "created_at",
    )

    # Sidebar filters for quick navigation
    list_filter = (
        "payment_status",
        "is_purchase_verified",
        "purchase_date",
        "created_at",
    )

    # Search fields for quick lookup
    search_fields = ("purchase_number", "invoice_number")

    # Read-only fields in detail view
    readonly_fields = ("created_at",)

    # Clickable link field in table
    list_display_links = ("purchase_number",)

    # Group fields into organized layout sections in admin form
    fieldsets = (
        (
            "Purchase Info",
            {"fields": ("purchase_number", "invoice_number", "purchase_date")},
        ),
        (
            "Financial Details",
            {"fields": ("sub_total", "discount", "total")},
        ),
        (
            "Status & Verification",
            {"fields": ("payment_status", "is_purchase_verified")},
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at",),
                "classes": ("collapse",),
            },
        ),
    )

    # Add custom colored status badges in list table
    @admin.display(description="Payment Status")
    def colored_payment_status(self, obj):
        colors = {
            "pending": "#ffc107",  # Yellow
            "paid": "#28a745",  # Green
            "unpaid": "#dc3545",  # Red
        }
        color = colors.get(obj.payment_status, "#6c757d")
        return format_html(
            '<span style="color: white; background-color: {}; padding: 3px 8px; border-radius: 4px; font-weight: bold; text-transform: uppercase; font-size: 11px;">{}</span>',
            color,
            obj.get_payment_status_display(),
        )