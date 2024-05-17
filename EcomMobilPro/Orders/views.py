from django.shortcuts import render
from Products.models import brand,product
# Create your views here.

def cart(request):
    brands = brand.objects.all()
    return render(request, 'cart.html', {'brands':brands})