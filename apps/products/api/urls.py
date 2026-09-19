from django.urls import path
from apps.products.api.views import ProductView, UpdateProductView

urlpatterns = [
    path('',ProductView.as_view()),
    path('<int:id>', UpdateProductView.as_view())
]