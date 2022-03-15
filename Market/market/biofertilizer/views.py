from urllib import request
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from biofertilizer import models
# Create your views here.

def home2(request):
     return render(request,'home2.html')

def admin(request):
    return render(request,'admin.html')

def home(request):
    return render(request,'home.html')

def seller(request):
    if request.method=="POST":
        name=request.POST['name']
        quant=request.POST['quant']
        loc=request.POST['loc']
        price=request.POST['price']
        transport=request.POST['transport']
        tprice=request.POST['tprice']
        ins=models.seller(name=name,quant=quant,loc=loc,price=price,transport=transport,tprice=tprice)
        ins.save();

    return render(request,'seller.html')
    
def buyer(request):
    return render(request,'home1.html')

def cart(request):
    return render(request,'cart.html')

def cart2(request):
    return render(request,'cart2.html')

def cart3(request):
    return render(request,'car3.html')

def homeN(request):
    return render(request,'homeN.html')

def cartN(request):
    return render(request,'cartN.html')

def c2(request):
    return render(request,'c2.html')
 