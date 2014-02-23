#! /usr/bin/env python
import re
import numpy as np
import pandas as pd
import pickle
import Quandl as qd
import matplotlib.pyplot as plt

from unipath import Path

PROJECT_DIR = Path(__file__).ancestor(1)
pickledir = PROJECT_DIR.child("codeandcord.p")
qd.get("NSE/OIL", rows=1, authtoken="2WmizyAqrqKpokFbMyYM")

#takes commands:
#name sure the authtoken pickle is in the same folder
# -ngdp returns all nations in a 
#long string of form 3lettercode, converted long, converted lat.
# -3lettercode returns the long form name of the nation that matches
def addrates (info, rates):
	exrate = 1
	y = 0
	for country in info:
		currency = country[4]
		currency = currency.replace(" ","")
		for label in rates.columns:
			code = label
			code = label.split("USD")[1]
			code = code.split(" ")[0]
			if (code == currency):
				exrate = rates[label][len(rates.index)-1]
				j = 2
				while (np.isnan(exrate)):
					if (j == len(rates.index)):
						break
					exrate = rates[label][len(rates.index)-j]
					j= j+1
				if (np.isnan(exrate)):
					exrate = 1
				exrate = 1/exrate
				info[y].append(exrate)		
		y = y+1
	return info
def exchange (info):
	currencylist = []
	currency = ""
	y = 0
	for country in info:	
		if (currency == "USD"):
			info[y].append(1)
			next
		else:
			currencylist.append('QUANDL/USD'+country[4]+".1")
			currency = country[4]	
	y = y+1
	if(len(currencylist)>=100):
		temp = currencylist
		currencylist = []
		x = int(len(temp)/100)
		for y in range (0,x+1):
			currencylist.append(temp[y*100:(y+1)*100])
	else:
		temp = currencylist
		currencylist = []
		currencylist.append (temp[:100])
	for chunk in currencylist:
		rates = qd.get(chunk,trim_start="2013-01-01",trim_end="2014-01-01")
		info = addrates(info, rates)
	currencylist = []
	for point in info:
		if len(point) ==5:
			currencylist.append('QUANDL/USD'+point[4])
	while y < len(currencylist)-1: 
		temp = currencylist [y:y+25]
		y = y+25
		rates = qd.get(temp,trim_start="2013-01-01",trim_end="2014-01-01")
		info = addrates(info,rates)
	y = 0		
	for point in info:
		if len(point) ==5:
			info[y].append(1)
		y=y+1		
	return info
def gather (datatype):
	tag = ""
	if (datatype == "NGDP"):
		tag = "ODA"
<<<<<<< HEAD
	countries = pickle.load (open(pickledir,"rb"))
=======
	countries = pickle.load (open("codeandcord.p","rb"))
>>>>>>> 90e2192b069c6aa20cc79a2ad4392fcf9ab45ed0
	longform = []
	columns = []
	mydata = pd.DataFrame ()
	for index , row in countries.iterrows():
		longitude = row['longitude']
		longitude = longitude [1:-1]
		longitude = longitude.replace ("\"\"","\'")
		x1 = longitude.split("\'")[0]
		x2 = longitude.split("\'")[1]
		x3 = longitude.split("\'")[2]
		x2=float(x2)
		x2 = x2/60.0
		x1= float(x1)
		x1 = x1+x2
		if (x3=='W'):
			x1 = -x1/180.0*100
		longitude = x1/180.0*100
		latitude = row['latitude']
		latitude = latitude [1:-1]
		latitude = latitude.replace ("\"\"","\'")
		x1 = latitude.split("\'")[0]
		x2 = latitude.split("\'")[1]
		x3 = latitude.split("\'")[2]
		x2=float(x2)
		x2 = x2/60.0
		x1=float(x1)
		x1 = x1+x2
		#print x3
		if (x3=='S'):
			x1 = -x1/90*100
		latitude = x1/90*100
		#longitude and latitude expressed as precentages
		columns.append ([row['country'], index,longitude,latitude,row['currency']])
		longform.append (tag+"."+index+"_"+datatype) 
	if (len(longform)>=100):
		temp = longform
		longform = []
		x = int(len(temp)/100)
		for y in range (0,x+1):
			longform.append(temp[y*100:(y+1)*100])
	else:
		temp = longform
		longform = []
		longform.append(temp[0:100])
	for chunk in longform:
		#print chunk
		#print "\n"
		temp = qd.get(chunk)
		if (chunk == longform[0]):
			mydata = temp
		else:
			mydata = pd.merge(mydata, temp, right_index=True, left_index=True)
	#mydata = qd.get(longform)
	#print mydata
	#print mydata [tag+"."+index+"_"+datatype+" - Value"] get's specific country
	#get usd to local currency conversion (uses latest in quandl)
	columns = exchange (columns)
	y = 0
	for label in mydata.columns:
		shortform = label.split(" ")[0]
		shortform = shortform.split(".")[1]
		shortform = shortform.split("_")[0]
		for country in columns:
			if shortform == country[1]:
				if country[5] == 1 and  not country[4] == "USD":
					mydata = mydata.drop(label,1)
					next
				else:
					mydata[label] = mydata[label]*country[5]
					longname = str(country[0])+","+str(country[1])+","+str(country[2])+","+str(country[3])
					mydata =  mydata.rename(columns={label : longname})
		y = y+1
	# print mydata
	return mydata	

def parse():
	df = gather ("NGDP")
	times = df.columns
	ind = df.index
	for i in range(0,len(times)):
		vals = times[i].split(",")
		country = vals[0]
		shortname = vals[1]
		longitude = str((float(vals[2])+100)/2)
		latitude =str((float(vals[3])+100)/2)
		print country + "+" + shortname + "+" + longitude + "+" + latitude
		print str(df.iloc[0,i])
		for k in range(0, len(ind)):
			time = str(ind[k].year)
			value = str(df.iloc[k,i])
			# print time + "!" + value


# parse()

