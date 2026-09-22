from django.urls import path, re_path
from apps.payment import views

app_name = "payment"

urlpatterns = [
    path(
        "initiate/<int:purchase_id>/",
        views.initiate_payment,
        name = "initiate_payment",
    ),
    path("callback/", views.payment_callback, name = "payment_callback"),

    re_path(r"^callback/?$", views.payment_callback, name="payment_callback"),
]
