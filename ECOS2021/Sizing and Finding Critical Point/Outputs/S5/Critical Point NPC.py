#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 21:34:26 2021

@author: alejandrosoto
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
BSA=pd.read_csv('S5.csv', sep=',', decimal='.', encoding='latin1')
df=pd.concat([BSA['LLC'], BSA['NPC (USD)']], axis=1, keys=['LLP', 'NPC'])
df['NPC']=df['NPC']/1000
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def func5(x, a, b, c,d,e,f,g, h, i):
    return (a*x-b)/(c*x**e+d+g*x**f+h*x**i)
xdata = df['LLP']
ydata=df['NPC']
plt.figure(figsize=(10,10))
plt.plot(xdata, ydata, 'b-', label='data')
popt, pcov = curve_fit(func5, xdata, ydata)
popt

residuals = ydata- func5(xdata, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((ydata-np.mean(ydata))**2)
r_squared = 1 - (ss_res / ss_tot)



x_1 = df['LLP']
y_1 = df['NPC']
a = Symbol('a')
j = Symbol('j')
x = Symbol('x')

from numpy import ones,vstack
from numpy.linalg import lstsq
points = [df.iloc[0],df.iloc[20]]
x_coords, y_coords = zip(*points)
A = vstack([x_coords,ones(len(x_coords))]).T
m, c = lstsq(A, y_coords)[0]
#print("Line Solution is y = {m}x + {c}".format(m=m,c=c))

y1=m*x+c
z1=np.array([m, c])
p1= np.poly1d(z1)
m1=-1/m


#a*x-b)/(c*x**e+d+g*x**f+h*x**i)
f=(popt[0]*x-popt[1])/(popt[2]*x**popt[4]+popt[3]+popt[6]*x**popt[5]+popt[7]*x**popt[8])
#eq1=Eq(l1-j)
eq3=Eq(f-j)



#Solucionador iterativo de sistema de ecuaciones no lineales
liminf=0
limsup=8.7
r=list()
for a in np.arange(liminf,limsup,0.05):
    l1=m1*x+a
    z2=np.array([m1, a])
    p2=np.poly1d(z2)
    eq1=Eq(l1-j)
    eq3=Eq(f-j)
    sol1 = nsolve((eq1, eq3), (x,j), (0.0005, 1.1))  
    r.append([sol1])
r=pd.DataFrame(r)
r['sol'] = r[0].astype(str)
r[['x','y']] = r.sol.str.split(",",expand=True)
r[['g','g1','x1']] = r.x.str.split("[",expand=True)
del r['g']
del r['g1']
r[['x1','g1']] = r.x1.str.split("]",expand=True)
del r['g1']
r[['y1','g','g1']] = r.y.str.split("]",expand=True)
del r['g1']
del r['g']
r[['g','y2']] = r.y1.str.split("[",expand=True)
del r['g']
del r['y1']
del r['x']
del r['y']
del r[0]
del r['sol']
r = r.rename(columns={'y2': 'y1'})
r['x1'] = r['x1'].astype(float)
r['y1'] = r['y1'].astype(float)
r1=r


points = [df.iloc[0],df.iloc[20]]
x_coords, y_coords = zip(*points)
A = vstack([x_coords,ones(len(x_coords))]).T
m, c = lstsq(A, y_coords)[0]
#print("Line Solution is y = {m}x + {c}".format(m=m,c=c))
y1=m*x+c
z1=np.array([m, c])
p1= np.poly1d(z1)

#Solucionador iteritvo ecuaciones lineales

r=list()
for a in np.arange(liminf,limsup,0.05):
    l1=m1*x+a
    z2=np.array([m1, a])
    p2=np.poly1d(z2)
    eq1=Eq(l1-j)
    sol = solve((l1-j, y1-j),(x, j))
    x1_1=float(sol[x])
    y1_1=float(sol[j])
    r.append([sol])
r=pd.DataFrame(r)
r['sol'] = r[0].astype(str)
r[['x','y']] = r.sol.str.split(",",expand=True)
r[['g','x1']] = r.x.str.split(":",expand=True)
del r['g']
r[['g1','y1']] = r.y.str.split(":",expand=True)
del r['g1']
r[['y1','g2']] = r.y1.str.split("}",expand=True)
del r['g2']
del r['sol']
del r[0]
del r['x']
del r['y']
r = r.rename(columns={'x1': 'x', 'y1': 'y'})
r['x'] = r['x'].astype(float)
r['y'] = r['y'].astype(float)
#print(r)

rt = pd.concat([r, r1], axis=1, join='inner')
rt['step']=np.arange(liminf,limsup,0.05)
rt['d']=((rt['x']-rt['x1'])**2+(rt['y']-rt['y1'])**2)**0.5
print('x de d max:',rt['x1'].iloc[rt['d'].idxmax()])
print('y de d max:',rt['y1'].iloc[rt['d'].idxmax()])
print('Distancia Máxima',rt['d'].max())


a=rt['step'].iloc[rt['d'].idxmax()]
l1=m1*x+a
z2=np.array([m1, a])
p2=np.poly1d(z2)




S5f=popt
S5r2=r_squared
S5x=rt['x1'].iloc[rt['d'].idxmax()]
S5y=rt['y1'].iloc[rt['d'].idxmax()]


plt.figure(figsize=(10,6.7))
xp = np.linspace(0,1, 100)
_ = plt.plot(x_1, y_1, '.',label='data', color='blue')
o= plt.plot(xp, func5(xp,*popt), '--', label='fit', color='green')
o1=plt.plot(xp, p1(xp), '-', label='secant', color='red')
_=plt.plot(xp, p2(xp), '-', label='distance', color='black')
plt.plot(rt['x1'].iloc[rt['d'].idxmax()], rt['y1'].iloc[rt['d'].idxmax()], marker='o', markersize=3, color="green")
#plt.plot(x_1, y_1, '-')
plt.plot(S5x,S5y, marker='o', markersize=5, color="red", label='critical point')
#escala real


plt.ylabel('NPC [Thousand USD]')
plt.xlabel('LLP')
plt.axis('scaled')
plt.legend()
#plt.savefig('critical point1.png',dpi=600,bbox_inches="tight")
#plt.show()
plt.show()


#Results

print('R2=',r_squared)
print('parameters=',popt)
print('critical point=',S5x)



