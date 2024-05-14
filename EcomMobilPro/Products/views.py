from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import brand,product

# Create your views here.

def index(request):
    brands = brand.objects.all()
    mobiles = product.objects.all()
    return render(request, 'index.html', {'brands':brands, 'mobiles': mobiles})

def productsLists(request):
    mobiles = product.objects.all()
    return render(request, 'productsList.html', { 'mobiles': mobiles})

def BrandMob(request, Brand_name):
    pass
    



