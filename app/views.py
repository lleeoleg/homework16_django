from django.shortcuts import render, get_list_or_404, redirect
from .models import Product

def success(request):
    return render(request, 'success.html')

def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        
        if name and price and description:
            Product.objects.create(name=name, price=price, description=description)
            return redirect('/success/')
        else:
            return get_list_or_404(Product)
    
    return render(request, 'index.html')

