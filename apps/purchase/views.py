from django.shortcuts import render




# Create your views here.

def purchase_view(request):
    return render(request,"purchase/products.html")