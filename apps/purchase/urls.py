from django.urls import path
from apps.purchase.views import purchase_view


app_name = "purchase"
urlpatterns =[
    path('',purchase_view, name="products"),
]