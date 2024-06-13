from django.urls import path
from .views import product_list  # Ensure you import the view you want to use

urlpatterns = [
    path('product_list/', product_list, name='product_list'),  # Define the URL pattern for the view
]
