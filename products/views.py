from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Product,Offer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def new(request):
    offers = Offer.objects.all()
    return render(request,'index2.html', {'offers': offers})
def con(request):
    return render (request,'contact.html')
def log(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                 login(request,user)
                 return redirect('index/')
            else:
                messages.info(request,'none')
                return  redirect('home')
        else:
            messages.info(request,'try again')
            return redirect('home')
    else:
        return render(request,'home.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))      




    return render (request,'home.html')