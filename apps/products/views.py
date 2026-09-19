from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from apps.products.forms import ProductForm
from apps.products.models import Product, Category
from django.views.generic import CreateView, UpdateView, DeleteView

class SStaffRequiredMixin(UserPassesTestMixin):
      def test_func(self):
            return (self.request.user.is_authenticated and self.request.user.is_staff
            )
class ProductListView(SStaffRequiredMixin,View):

    def get(self, request):
        categories = Category.objects.all()
        products = Product.objects.all()
        context = {
            "products":products
        }
        return render(request, "products/list.html", context)


class ProductCreateView(SStaffRequiredMixin,CreateView):
        model = Product
        form_class = ProductForm
        template_name = "products/create.html"
        success_url = reverse_lazy("product_list")

class ProductUpdateView(SStaffRequiredMixin,UpdateView):
        model = Product
        form_class = ProductForm
        template_name = "products/create.html"
        success_url = reverse_lazy("product_list")

class ProductDeleteView(SStaffRequiredMixin,DeleteView):
        model = Product
        template_name = "products/delete.html"
        success_url = reverse_lazy("product_list")

