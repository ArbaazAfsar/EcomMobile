from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import brand,product
from django.core.paginator import Paginator
from Orders.models import orderItem
# Create your views here.

def index(request):
    Latest_products = product.objects.order_by('-id')[:3]
    brands = brand.objects.all()
    mobiles = product.objects.all()
    pro_pages = Paginator(mobiles,3)
    page_num = request.GET.get('page')
    mobiles= pro_pages.get_page(page_num)
    return render(request, 'index.html', {'brands':brands, 'mobiles': mobiles, 'pro_pages':pro_pages, 'Latest_products':Latest_products})

def productsLists(request):
    brands = brand.objects.all()
    mobiles = product.objects.all()
    pro_pages = Paginator(mobiles,3)
    page_num = request.GET.get('page')
    mobiles= pro_pages.get_page(page_num)
    return render(request, 'productsList.html', {'brands':brands,  'mobiles': mobiles, 'pro_pages':pro_pages})

def base(request):
    brands = brand.objects.all()
    return render(request, 'base.html', {'brands':brands} )
    


def brand_mob(request, Brand_name):
    mobiles = product.objects.filter(Brand_name__Brand_name=Brand_name)
    if mobiles.exists():
        brands = brand.objects.all()
        pro_pages = Paginator(mobiles,3)
        page_num = request.GET.get('page')
        mobiles= pro_pages.get_page(page_num)
        return render(request, 'brand.html', {'brands': brands, 'mobiles': mobiles, 'pro_pages':pro_pages})
    else:
        brands = brand.objects.all()
        message = "This brand's product is not available now"
        return render(request, 'brand.html',  {'message':message,'brands': brands})



    
    
def productDetails(request, pk, Brand_name):
    mobile = product.objects.get( id = pk)
    Brand = product.objects.filter(Brand_name__Brand_name=Brand_name)
    brands= brand.objects.all()
    return render(request, 'product_details.html', {'mobile':mobile, 'Brand': Brand, 'brands':brands})



