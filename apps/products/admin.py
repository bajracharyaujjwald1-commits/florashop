
from django.contrib import admin
from apps.products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Field names use the lower_case 'category' convention matching recommended fixes
    list_display = ("id", "name", "Category", "price","image","description", "is_available", "created_at")
    list_filter = ("Category", "is_available", "created_at")
    search_fields = ("name",)
    list_editable = ("price", "is_available")
    ordering = ("-created_at",)