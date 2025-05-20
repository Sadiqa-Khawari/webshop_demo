from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Order
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_details.html', {'product': product})

def purchase_product(request, pk):

    return redirect("purcgase_succeeded")

def purchase_succeeded(request):
    return render(request, 'shop/success.html')