from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User, auth
import pickle
import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
import csv
from datetime import datetime
# Create your views here.

def predict(request):
	list_three.clear()
	stype = request.POST['stype']	
	dur = int(request.POST['dur'])
	temp = int(request.POST['temp'])
	rain = int(request.POST['rain'])
	ph = float(request.POST['ph'])
	oc = request.POST['oc']
	n = request.POST['n']
	p2 = request.POST['p2']
	k2 = request.POST['k2']
	s = request.POST['s']
	zn = request.POST['zn']
	b = request.POST['b']
	fe = request.POST['fe']
	mn = request.POST['mn']
	cu = request.POST['cu']

	
	if(stype.casefold() == 'clay'):
		stype = 1
	elif(stype.casefold() == 'clay loam'):
		stype = 2
	elif(stype.casefold() == 'loam'):
		stype = 3
	elif(stype.casefold() == 'sandy loam'):
		stype = 4
	elif(stype.casefold() == 'sandy'):
		stype = 5

	oc= checkType(oc)
	n=checkType(n)
	p2=checkType(p2)
	k2=checkType(k2)
	s=checkType(s)
	zn=checkType(zn)
	b=checkType(b)
	fe=checkType(fe)
	mn=checkType(mn)
	cu=checkType(cu)
	
	

	
	model = joblib.load('templates\lrnd_api.pkl')
	
	import csv
	row_list = [["soil_type_int","Duration", "Temp", "Rainfall","pH","OrgCarbon_int","N_int","P2O5_int","K2O_int","S_int","Zn_int","B_int","Fe_int","Mn_int","Cu_int"],
				[2,130,27,6,6.2,3,3,3,3,1,1,1,1,1,1],
				[1,130,26,6,6.2,3,3,3,3,1,1,1,1,1,1],
				[3,110,15,2,6.9,3,4,4,3,1,1,2,2,1,2],
				[4,95,22,2,5.9,3,4,4,3,1,2,1,1,1,2],
				[4,120,27,1,7.7,4,5,4,4,2,1,2,1,1,1],
				[4,400,28,3,6.7,3,2,3,5,2,1,1,1,2,1],
				[4,100,32,1,6.3,4,4,3,3,1,1,1,1,1,2],
				[4,95,25,2,6.2,3,4,4,3,1,1,1,2,1,2],
				[4,95,30,2,5.8,3,3,4,3,1,1,1,2,1,2],
             [stype,dur,temp,rain,ph,oc,n,p2,k2,s,zn,b,fe,mn,cu]]
	with open('temp.csv', 'w') as file:
		writer = csv.writer(file)
		writer.writerows(row_list)
	
	#x_test=np.array([dur,temp,ph,rain,n,p,k]).reshape(1,-1)
	x_test=pd.read_csv(r"temp.csv")
	#print(np.isnan(x_test1).any())
	#x_train1[np.isnan(x_train1)] = np.median(x_train1[~np.isnan(x_train1)])
	#x_test=np.array([dur,temp,ph,rain,n,p,k])
	#x_test=x_test.reshape(1,-1)
	#x_test=pd.read_csv(r"templates/tc.csv")
	print(x_test)
	scale=MinMaxScaler()
	#x_train1=scale.fit_transform(x_train)
	x_test1=scale.fit_transform(x_test)
	
	x_test1[np.isnan(x_test1)] = np.median(x_test1[~np.isnan(x_test1)])
	print(np.isnan(x_test1).any())


	#from sklearn.linear_model import LogisticRegression

	#teacher=LogisticRegression()
	#learner=teacher.fit(x_train1,y_train)
	probs = model.predict_proba(x_test1)
	temp=model.classes_
	#print(probs)

	best_n=np.argsort(probs)[:, -3:][:, ::-1]
	#print(best_n)
	for i in range(len(x_test)):
		x=probs[i][best_n[i]]
		print(x)
		for j in range (3):
			for k in range(len(probs[0])):
				if(x[j]==probs[i][k]):
					list1.append(temp[k])
	print(list1)
	print(x)  #x is the probability list
	
	#list_three = []
	for d in range(30):
		if(list1[d]==1):
			list1[d]='Rice'
		elif(list1[d]==2):
			list1[d]='Wheat'
		elif(list1[d]==3):
			list1[d]='Maize'
		elif(list1[d]==4):
			list1[d]='Jowar'
		elif(list1[d]==5):
			list1[d]='Bajra'
		elif(list1[d]==6):
			list1[d]='Sugarcane'
	
	list_three.append(list1[27])
	list_three.append(list1[28])
	list_three.append(list1[29])
	global_x.append(x[0])
	global_x.append(x[1])
	global_x.append(x[2])
	print(list1[27])
	print(list_three)
	print(model.predict(x_test1))
	#sejal = list_three.copy();
	#print("Sejal la print kartoy")
	#print(sejal)

	#Yp=model.predict(x_test1)
	
	#res=val1+val2
	return render(request,'results.html',{'result':list_three})


def pie(request):
	c1 = global_x[0]
	c2 = global_x[1]
	c3 = global_x[2]

	fig = Figure()
	canvas = FigureCanvas(fig)

	label = [list1[27],list1[28],list1[29]]
	probabilities = [
		c1,c2,c3
	]
	
	plt.pie(probabilities, labels = label,autopct='%1.2f%%')
	

	buf = io.BytesIO()
	plt.savefig(buf,format='png')
	plt.close(fig)
	response = HttpResponse(buf.getvalue(),content_type='image/png')