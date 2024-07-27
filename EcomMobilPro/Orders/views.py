from django.shortcuts import render
from Products.models import brand,product
# Create your views here.

def cart(request):
    brands = brand.objects.all()
    return render(request, 'cart.html', {'brands':brands})


def addCart(request):
    if request.POST:
        user = request.user
        Customer = user.customer_profile
        Product = request.POST.get('pk')
        quantity = request.POST.get('product_id')
        
        
        