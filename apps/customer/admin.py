from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "get_email")
    list_display_links = ("id", "username")
    search_fields = (
        "username__username",
        "username__email",
    )
    raw_id_fields = ("username",)

    @admin.display(description="Email")
    def get_email(self, obj):
        return obj.username.email

    