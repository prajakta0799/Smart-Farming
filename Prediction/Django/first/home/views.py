from asyncore import read, write
import csv
from tkinter import W
import pandas as pd
import numpy as np
import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
#df=pd.read_csv("tc.csv")
#df.head(3)
#print("Prajakta")


def predict(request):
	list.clear()
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

	oc= type(oc)
	n=type(n)
	p2=type(p2)
	k2=type(k2)
	s=type(s)
	zn=type(zn)
	b=type(b)
	fe=type(fe)
	mn=type(mn)
	cu=type(cu)
	
	

	
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


