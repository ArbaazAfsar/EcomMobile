from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout


# Create your views here.

def account(request):
    if request.POST and 'register' in request.POST:
        try :
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            
            user = User.objects.create_user(
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully.")
            return redirect('index')
        else:
            messages.success(request, "User is not exist. Please Register.")
            
        
        
    return render(request, 'account.html', {})

def Sign_out(request):
    logout(request)
    return redirect('index')
    
