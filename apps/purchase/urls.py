from django.urls import path
from apps.purchase.views import purchase_view, create_purchase_view, purchase_detail_view


app_name = "purchase"
urlpatterns =[
    path('',purchase_view, name="products"),
    path('purchase/create/<int:product_id>',create_purchase_view, name="create_purchase"),
    path('purchase/details/<int:purchase_id>', purchase_detail_view, name = "purchase_detail"),

]