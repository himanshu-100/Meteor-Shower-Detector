# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:28:49 2019

@author: user
"""

import csv 
import gmplot
import math
eps=15
undefined=-1
noise=0
minpts=50
def dist(x1,y1,x2,y2):
    return math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
def query(x,y,q):
    neigh=[]
    for d in range(len(x)):
        if(dist(x[d],y[d],x[q],y[q])<=eps):
            neigh.append(d)
    return neigh
def DBSCAN(x,y):
    c=0
    label=[]
    for i in range(len(x)):
        label.append(undefined)
    for i in range(len(x)):
        label[i]=undefined
    for p in range(len(x)):
        if (label[p]!=undefined):
            continue
        neigh=query(x,y,p)
        if(len(neigh)<minpts):
            label[p]=noise
            continue
        c=c+1
        label[p]=c
        print(p)
        print(c)
        s=[]
        s=neigh
        s.remove(p)
        for q in range(len(s)):
            if(label[s[q]]==noise):
                label[s[q]]=c
            if(label[s[q]]!=undefined):
                continue
            label[s[q]]=c
            neigh=query(x,y,s[q])
            if(len(neigh)>=minpts):
                s.extend(neigh)
    gmap=[]
    for k in range(1,c+1):
        gmap.append(gmplot.GoogleMapPlotter(30.3164945, 78.03219179999999, 5 )) 
        x1=[]
        y1=[]
        for g in range(len(x)):
            if(label[g]==k):
                x1.append(x[g])
                y1.append(y[g])
        gmap[len(gmap)-1].heatmap( x1, y1 )
        str1="C:\\Users\\user\\Documents\\ADM Project\\map"
        str1+=str(k)
        str1+=(".html")
        print(str1)
        gmap[len(gmap)-1].draw(str1)
# csv file name   
filename = "data.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r',encoding="utf-8") as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
    # get total number of rows 
    print("Total no. of rows: %d"%(csvreader.line_num)) 
  
# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 
  
#  printing first 5 rows 
print('\nFirst 5 rows are:\n') 
coordinates=[]
for row in rows: 
    # parsing each column of a row 
    #for col in row: 
    #   print("%10s"%col), 
    #print('\n') 
    row[4]=row[4].replace(',','')
    if(len(row[4])>2 and float(row[4])>=500):
        coordinates.append(row[9])
lat=[]
long=[]
for coor in coordinates[:500]:
    length=len(coor)
    temp=coor[1:length-1]
    temp=temp.split(", ")
    if(len(temp)>=2):
        lat.append(float(temp[0]))
        long.append(float(temp[1]))
gmap4 = gmplot.GoogleMapPlotter(30.3164945, 78.03219179999999, 5 ) 
# heatmap plot heating Type 
# points on the Google map 
gmap4.heatmap( lat, long )   
gmap4.draw( "C:\\Users\\user\\Documents\\ADM Project\\map.html" ) 
DBSCAN(lat,long)