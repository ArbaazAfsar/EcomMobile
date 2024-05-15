from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import brand,product

# Create your views here.

def index(request):
    brands = brand.objects.all()
    mobiles = product.objects.all()
    return render(request, 'index.html', {'brands':brands, 'mobiles': mobiles})

def productsLists(request):
    brands = brand.objects.all()
    mobiles = product.objects.all()
    return render(request, 'productsList.html', {'brands':brands,  'mobiles': mobiles})

def base(request):
    brands = brand.objects.all()
    return render(request, 'base.html', {'brands':brands} )
    


def BrandMob(request, Brand_name):
    error= None
    try:
        brands = product.objects.filter(Brand_name__Brand_name=Brand_name)
        brnd = brand.objects.all()
        
        return render(request, 'brand.html', {'brands': brands, 'brnd':brnd})
        
    except product.DoesNotExist:
        error = {'error':"Brand not found"}
        return render(request,'brand.html', error )



