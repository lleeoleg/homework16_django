from django.urls import path
from .views import create_product, success

urlpatterns = [
    path('create-product/', create_product),
    path('success/', success)
]
