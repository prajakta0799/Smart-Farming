from typing import Pattern
from django.contrib import admin
from django.urls import path
from biofertilizer import views
'''App'''
urlpatterns = [
    path("",views.home2,name='biofertilizer'),                 #Main Home
    #path("admin",views.admin,name='admin'),
    path("home.html",views.home,name='home'),
    path("seller.html",views.seller,name='seller'),     
    path("home1.html",views.buyer,name='buyer'),
    path("cart.html",views.cart,name='cart'),               #cart1
    path("cart2.html",views.cart2,name='cart2') ,            #cart2
    path("cart3.html",views.cart2,name='cart3') ,            #cart3

    #Nursery

    path("homeN.html",views.homeN,name='nursery1') ,
    path("cartN.html",views.cartN,name='cartN')  ,
    path("c2.html",views.c2,name='c2') 
    
]