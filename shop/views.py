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
    url = "https://www.vismapay.com/pbwapi/auth_payment"
    api_key = ""

    product = get_object_or_404(product, pk=pk)

    payload = {
        "version": "w3.2",
        "api_key": api_key,
        "order_number": "test-order-1415463675",
        "amount": int(product.total_price * 100),
        "currency": "EUR",
        "email": "test.person@example.com",
        "payment_method": {
            "type": "e-payment",
            "return_url": "https://127.0.0.1.8000/purchase_succeeded",
            "notify_url": "https://127.0.0.1.8000/purchase_succeeded",
            "lang": "fi",
            "token_valid_until": "1442403776",
        },
        "authcode": "8DF90FF9582EC87C073ACEE5C6194E9E2280D6028D55...",
        "customer": {  
            "firstname": "Test",
            "lastname": "Person",
            "email": "test.person@example.com",
            "address_street": "Testaddress 1",
            "address_city": "Testlandia",
            "address_zip": "123456"
        },
        "products": [
            {  
            "id": "ab1",
            "title": "Shipping",
            "count": 1,
            "pretax_price": int(product.price * 100),
            "tax": 0,
            "price": int(product.total_price * 100),
            "type": 2
            }
        ]
        }

    return redirect("purcgase_succeeded")

def purchase_succeeded(request):
    return render(request, 'shop/success.html')