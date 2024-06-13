from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Corrected method to query all products
    context = {
        'products': products  # Added context dictionary
    }
    return render(request, "plp_ecommerce/product_list.html" , context)  # Render template with context
