from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages


# Create your views here.

def account(request):
    if request.POST and 'register' in request.POST:
        try :
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            
            user = User.objects.create(
                username = username,
                password = password,
                email= email,
                
            )
        
            customer = Customer.objects.create(
                name = username,
                user = user,
                phone = phone,
            ) 
            print(customer)
            messages.success(request, 'User registered successfully. Please login')
            
        
        except Exception as e:
            msg = 'Username is already exist'
            messages.error(request, msg)
            
    elif request.POST and 'login' in request.POST:
        
        
     return render(request, 'account.html', {})
