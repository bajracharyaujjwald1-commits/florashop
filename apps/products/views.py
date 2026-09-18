from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from apps.products.forms import ProductForm
from apps.products.models import Product, Category
from django.views.generic import CreateView, UpdateView, DeleteView

class ProductListView(View):

    def get(self, request):
        categories = Category.objects.all()
        products = Product.objects.all()
        context = {
            "products":products
        }
        return render(request, "products/list.html", context)
    
class ProductCreateView(CreateView):
        model = Product
        form_class = ProductForm
        template_name = "products/create.html"
        success_url = reverse_lazy("product_list")

class ProductUpdateView(UpdateView):
        model = Product
        form_class = ProductForm
        template_name = "products/create.html"
        success_url = reverse_lazy("product_list")

class ProductDeleteView(DeleteView):
        model = Product
        template_name = "products/delete.html"
        success_url = reverse_lazy("product_list")

