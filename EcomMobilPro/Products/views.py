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
    




def brand_mob(request, Brand_name):
    message = None
    brands = product.objects.filter(Brand_name__Brand_name=Brand_name)
    if brands.exists():
        all_brands = brand.objects.all()
        return render(request, 'brand.html', {'brands': brands, 'all_brands': all_brands})
    else:
        all_brands = brand.objects.all()
        message = "This product is not available in this time"
        return render(request, 'brand.html',  {'message':message,'all_brands': all_brands})

    
    
def productDetails(request, pk, Brand_name):
    mobile = product.objects.get( id = pk)
    brands = product.objects.filter(Brand_name__Brand_name=Brand_name)
    brnd= brand.objects.all()
    return render(request, 'product_details.html', {'mobile':mobile, 'brands': brands, 'brnd':brnd})



