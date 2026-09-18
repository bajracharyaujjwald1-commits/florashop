from django.urls import path

from apps.products.views import ProductCreateView, ProductDeleteView, ProductListView, ProductUpdateView


urlpatterns = [
    path("list/", ProductListView.as_view(), name = "product_list"),
    path("create/", ProductCreateView.as_view(), name = "product_create"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name = "product_update"),            
    path("delete/<int:pk>", ProductDeleteView.as_view(), name = "product_delete"),
]