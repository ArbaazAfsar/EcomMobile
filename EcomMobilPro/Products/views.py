from django.shortcuts import render
from .models import brand,product

# Create your views here.

def index(request):
    brands = brand.objects.all()
    mobiles = product.objects.all()
    return render(request, 'index.html', {'brands':brands, 'mobiles': mobiles})



