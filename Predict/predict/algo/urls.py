from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import login

urlpatterns = [
    path('',views.index,name='Home'),
    path('contactus',views.contactus,name='ContactUs'),
      path('govtschemes/',views.govtschemes,name='GovtSchemes'),
       path('aboutus/',views.aboutus,name='aboutus'),
      path('predict',views.predict,name='predict'),
      path('retrievePrice',views.retrievePrice,name='retrievePrice'),
      path('sendCSV',views.sendCSV,name='sendCSV'),
      path('pie', views.pie,name='pie'),
      path('login',views.login,name='LogIn'),
     path('signup',views.signup,name='SignUP'),
     path('aftersignup',views.aftersignup,name='AfterSignUP'),
      path('logout_request',views.logout_request,name='LogOut'),
     path('csm',views.csm,name='csm')

]