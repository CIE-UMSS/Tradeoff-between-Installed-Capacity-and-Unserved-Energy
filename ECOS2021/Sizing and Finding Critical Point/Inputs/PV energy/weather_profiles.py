#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:29:06 2021

@author: alejandrosoto
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.pyplot import figure
import datetime
import matplotlib.dates as mdates


raq = pd.read_csv('raq_weather.csv', sep=' ', decimal='.', encoding='latin1', error_bad_lines=False)
#raq.shape
raq.drop(raq.columns[3:17], axis=1, inplace=True)
raq.drop(raq.index[0:2], axis=0, inplace=True)
raq.reset_index(drop=True)
raq= raq.rename(columns={'#': 'date','Renewables.ninja':'local_time','Weather':'temp'})
raq[['time','local_date']] = raq.local_time.str.split(",",expand=True,)
raq.drop(raq.columns[1], axis=1, inplace=True)
raq['temp'] = raq['temp'].map(lambda x: x.rstrip(','))
raq[['local_time','t']] = raq.temp.str.split(",",expand=True,)
raq.drop(raq.columns[1], axis=1, inplace=True)
raq[['local_day','local_month','local_year']] = raq.local_date.str.split("/",expand=True,)
raq['t'] = raq['t'].astype(float)
raq
raq=raq.drop([2,3,4,5])
raq=raq.reset_index(drop=True)

raq['time']=pd.date_range(start='1/1/2018', end='1/1/2019', freq='1H', closed='left')

raq['time'] = pd.to_datetime(raq['time'], format='%Y-%m-%d %H:%M:%S')
#.dt.strftime('%Y-%m-%d %H:%M:%S')

raq['t'] = raq['t'].astype(float)

xls = pd.ExcelFile('PV_Energy.xls')
sheetX=xls.parse(0)
df=sheetX[1]
#pd.DataFrame(df)
PV=pd.DataFrame(df)
PV=PV.astype(float)


raq1 = pd.read_csv('raq_PV.csv', sep=' ', decimal='.', encoding='latin1', error_bad_lines=False)
raq1.drop(raq1.columns[3:17], axis=1, inplace=True)
raq1.drop(raq1.index[0:2], axis=0, inplace=True)
raq1.reset_index(drop=True)
raq1= raq1.rename(columns={'#': 'date','Renewables.ninja':'local_time','Weather':'temp'})
raq1[['time','local_date']] = raq1.local_time.str.split(",",expand=True,)
raq1.drop(raq1.columns[1], axis=1, inplace=True)
raq1['temp'] = raq1['temp'].map(lambda x: x.rstrip(','))
raq1[['local_time','PV']] = raq1.temp.str.split(",",expand=True,)
del raq1['date']
del raq1['temp']
del raq1['time']
del raq1['local_date']
raq1=raq1.reset_index(drop=True)
raq1=raq1.drop([0,1,2,3])
raq1=raq1.reset_index(drop=True)
del raq1['local_time']
raq1['PV']=raq1['PV'].astype(float)
#del raq['local_time']
'''
raq1.drop(raq.columns[1], axis=1, inplace=True)
raq1[['local_day','local_month','local_year']] = raq1.local_date.str.split("/",expand=True,)
raq1['t'] = raq1['t'].astype(float)
raq1
raq1=raq1.drop([2,3,4,5])
raq1=raq1.reset_index(drop=True)
'''

# Set the locator
locator = mdates.MonthLocator()  # every month
# Specify the format - %b gives us Jan, Feb...
fmt = mdates.DateFormatter('%b')

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(raq['time'],raq1['PV'], color='blue')
ax2.plot(raq['time'],raq['t'], color='red')


ax1.set_xlabel('Months')
ax2.set_ylabel('Temperature $(^{o}C)$')
ax1.set_ylabel('Horizontal Irradation $W/m^{2}$')
ax2.set_ylim([-5, 100])

X = plt.gca().xaxis
X.set_major_locator(locator)
# Specify formatter
X.set_major_formatter(fmt)
fig.subplots_adjust(wspace=0, hspace=0)
plt.margins(x=0,y=0)
#plt.savefig('weather_raq.png', bbox_inches='tight', pad_inches=0.0)
fig.savefig('weather_raqaypampa.png',dpi=600,bbox_inches="tight")
plt.show()

