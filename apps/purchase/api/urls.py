from django.urls import path
from apps.purchase.api.views import PurchaseView,UpdatePurchaseView

urlpatterns = [
    path('',PurchaseView.as_view(), name="purchaseview"),
    path('<int:id>',UpdatePurchaseView.as_view(), name="update_purchaseview")
]