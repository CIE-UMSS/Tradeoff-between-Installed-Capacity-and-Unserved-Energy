#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:32:18 2021

@author: alejandrosoto
"""

import pandas as pd
Jan=pd.read_csv('Ocasional_Day/Jan_BSA_o.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Feb=pd.read_csv('Ocasional_Day/Feb_BSA_o.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Mar=pd.read_csv('Ocasional_Day/Mar_BSA_o.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Apr=pd.read_csv('Ocasional_Day/Apr_BSA_o.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
May=pd.read_csv('Ocasional_Day/May_BSA_o.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jun=pd.read_csv('Ocasional_Day/Jun_BSA_o.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jul=pd.read_csv('Ocasional_Day/Jul_BSA_o.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Aug=pd.read_csv('Ocasional_Day/Aug_BSA_o.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Sep=pd.read_csv('Ocasional_Day/Sep_BSA_o.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Oct=pd.read_csv('Ocasional_Day/Oct_BSA_o.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Nov=pd.read_csv('Ocasional_Day/Nov_BSA_o.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Dec=pd.read_csv('Ocasional_Day/Dec_BSA_o.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jan['0'] = Jan['0'].astype(float)
Jan['Unnamed: 0'] = Jan['Unnamed: 0'].astype(float)
Feb['0'] = Feb['0'].astype(float)
Feb['Unnamed: 0'] = Feb['Unnamed: 0'].astype(float)
Mar['0'] = Mar['0'].astype(float)
Mar['Unnamed: 0'] = Mar['Unnamed: 0'].astype(float)
Apr['0'] = Apr['0'].astype(float)
Apr['Unnamed: 0'] = Apr['Unnamed: 0'].astype(float)
May['0'] = May['0'].astype(float)
May['Unnamed: 0'] = May['Unnamed: 0'].astype(float)
Jun['0'] = Jun['0'].astype(float)
Jun['Unnamed: 0'] = Jun['Unnamed: 0'].astype(float)
Jul['0'] = Jul['0'].astype(float)
Jul['Unnamed: 0'] = Jul['Unnamed: 0'].astype(float)
Aug['0'] = Aug['0'].astype(float)
Aug['Unnamed: 0'] = Aug['Unnamed: 0'].astype(float)
Sep['0'] = Sep['0'].astype(float)
Sep['Unnamed: 0'] = Sep['Unnamed: 0'].astype(float)
Oct['0'] = Oct['0'].astype(float)
Oct['Unnamed: 0'] = Oct['Unnamed: 0'].astype(float)
Nov['0'] = Nov['0'].astype(float)
Nov['Unnamed: 0'] = Nov['Unnamed: 0'].astype(float) 
Dec['0'] = Dec['0'].astype(float)

import pandas as pd
Jan_1=pd.read_csv('Typical_Day/Jan_BSA_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Feb_1=pd.read_csv('Typical_Day/Feb_BSA_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Mar_1=pd.read_csv('Typical_Day/Mar_BSA_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Apr_1=pd.read_csv('Typical_Day/Apr_BSA_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
May_1=pd.read_csv('Typical_Day/May_BSA_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jun_1=pd.read_csv('Typical_Day/Jun_BSA_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jul_1=pd.read_csv('Typical_Day/Jul_BSA_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Aug_1=pd.read_csv('Typical_Day/Aug_BSA_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Sep_1=pd.read_csv('Typical_Day/Sep_BSA_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Oct_1=pd.read_csv('Typical_Day/Oct_BSA_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Nov_1=pd.read_csv('Typical_Day/Nov_BSA_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Dec_1=pd.read_csv('Typical_Day/Dec_BSA_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jan_1['0'] = Jan_1['0'].astype(float)
Jan_1['Unnamed: 0'] = Jan_1['Unnamed: 0'].astype(float)
Feb_1['0'] = Feb_1['0'].astype(float)
Feb_1['Unnamed: 0'] = Feb_1['Unnamed: 0'].astype(float)
Mar_1['0'] = Mar_1['0'].astype(float)
Mar_1['Unnamed: 0'] = Mar_1['Unnamed: 0'].astype(float)
Apr_1['0'] = Apr_1['0'].astype(float)
Apr_1['Unnamed: 0'] = Apr_1['Unnamed: 0'].astype(float)
May_1['0'] = May_1['0'].astype(float)
May_1['Unnamed: 0'] = May_1['Unnamed: 0'].astype(float)
Jun_1['0'] = Jun_1['0'].astype(float)
Jun_1['Unnamed: 0'] = Jun_1['Unnamed: 0'].astype(float)
Jul_1['0'] = Jul_1['0'].astype(float)
Jul_1['Unnamed: 0'] = Jul_1['Unnamed: 0'].astype(float)
Aug_1['0'] = Aug_1['0'].astype(float)
Aug_1['Unnamed: 0'] = Aug_1['Unnamed: 0'].astype(float)
Sep_1['0'] = Sep_1['0'].astype(float)
Sep_1['Unnamed: 0'] = Sep_1['Unnamed: 0'].astype(float)
Oct_1['0'] = Oct_1['0'].astype(float)
Oct_1['Unnamed: 0'] = Oct_1['Unnamed: 0'].astype(float)
Nov_1['0'] = Nov_1['0'].astype(float)
Nov_1['Unnamed: 0'] = Nov_1['Unnamed: 0'].astype(float) 
Dec_1['0'] = Dec_1['0'].astype(float)

import numpy as np
Jan['time_series']=np.arange(0,len(Jan),1)
Jan['time_series']=Jan['time_series']/60
Feb['time_series']=np.arange(0,len(Feb),1)
Feb['time_series']=Feb['time_series']/60
Mar['time_series']=np.arange(0,len(Mar),1)
Mar['time_series']=Mar['time_series']/60
Apr['time_series']=np.arange(0,len(Apr),1)
Apr['time_series']=Apr['time_series']/60
May['time_series']=np.arange(0,len(May),1)
May['time_series']=May['time_series']/60
Jun['time_series']=np.arange(0,len(Jun),1)
Jun['time_series']=Jun['time_series']/60
Jul['time_series']=np.arange(0,len(Jul),1)
Jul['time_series']=Jul['time_series']/60
Aug['time_series']=np.arange(0,len(Aug),1)
Aug['time_series']=Aug['time_series']/60
Sep['time_series']=np.arange(0,len(Sep),1)
Sep['time_series']=Sep['time_series']/60
Oct['time_series']=np.arange(0,len(Oct),1)
Oct['time_series']=Oct['time_series']/60
Nov['time_series']=np.arange(0,len(Nov),1)
Nov['time_series']=Nov['time_series']/60
Dec['time_series']=np.arange(0,len(Dec),1)
Dec['time_series']=Dec['time_series']/60

import numpy as np
Jan_1['time_series']=np.arange(0,len(Jan),1)
Jan_1['time_series']=Jan_1['time_series']/60
Feb_1['time_series']=np.arange(0,len(Feb),1)
Feb_1['time_series']=Feb_1['time_series']/60
Mar_1['time_series']=np.arange(0,len(Mar),1)
Mar_1['time_series']=Mar_1['time_series']/60
Apr_1['time_series']=np.arange(0,len(Apr),1)
Apr_1['time_series']=Apr_1['time_series']/60
May_1['time_series']=np.arange(0,len(May),1)
May_1['time_series']=May_1['time_series']/60
Jun_1['time_series']=np.arange(0,len(Jun),1)
Jun_1['time_series']=Jun_1['time_series']/60
Jul_1['time_series']=np.arange(0,len(Jul),1)
Jul_1['time_series']=Jul_1['time_series']/60
Aug_1['time_series']=np.arange(0,len(Aug),1)
Aug_1['time_series']=Aug_1['time_series']/60
Sep_1['time_series']=np.arange(0,len(Sep),1)
Sep_1['time_series']=Sep_1['time_series']/60
Oct_1['time_series']=np.arange(0,len(Oct),1)
Oct_1['time_series']=Oct_1['time_series']/60
Nov_1['time_series']=np.arange(0,len(Nov),1)
Nov_1['time_series']=Nov_1['time_series']/60
Dec_1['time_series']=np.arange(0,len(Dec),1)
Dec_1['time_series']=Dec_1['time_series']/60

Jan_BS_A=pd.read_csv('Jan_BS_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Feb_BS_A=pd.read_csv('Feb_BS_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Mar_BS_A=pd.read_csv('Mar_BS_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Apr_BS_A=pd.read_csv('Apr_BS_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
May_BS_A=pd.read_csv('May_BS_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jun_BS_A=pd.read_csv('Jun_BS_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jul_BS_A=pd.read_csv('Jul_BS_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Aug_BS_A=pd.read_csv('Aug_BS_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Sep_BS_A=pd.read_csv('Sep_BS_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Oct_BS_A=pd.read_csv('Oct_BS_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Nov_BS_A=pd.read_csv('Nov_BS_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Dec_BS_A=pd.read_csv('Dec_BS_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jan_BS_A['0'] = Jan_BS_A['0'].astype(float)
Jan_BS_A['Unnamed: 0'] = Jan_BS_A['Unnamed: 0'].astype(float)
Feb_BS_A['0'] = Feb_BS_A['0'].astype(float)
Feb_BS_A['Unnamed: 0'] = Feb_BS_A['Unnamed: 0'].astype(float)
Mar_BS_A['0'] = Mar_BS_A['0'].astype(float)
Mar_BS_A['Unnamed: 0'] = Mar_BS_A['Unnamed: 0'].astype(float)
Apr_BS_A['0'] = Apr_BS_A['0'].astype(float)
Apr_BS_A['Unnamed: 0'] = Apr_BS_A['Unnamed: 0'].astype(float)
May_BS_A['0'] = May_BS_A['0'].astype(float)
May_BS_A['Unnamed: 0'] = May_BS_A['Unnamed: 0'].astype(float)
Jun_BS_A['0'] = Jun_BS_A['0'].astype(float)
Jun_BS_A['Unnamed: 0'] = Jun_BS_A['Unnamed: 0'].astype(float)
Jul_BS_A['0'] = Jul_BS_A['0'].astype(float)
Jul_BS_A['Unnamed: 0'] = Jul_BS_A['Unnamed: 0'].astype(float)
Aug_BS_A['0'] = Aug_BS_A['0'].astype(float)
Aug_BS_A['Unnamed: 0'] = Aug_BS_A['Unnamed: 0'].astype(float)
Sep_BS_A['0'] = Sep_BS_A['0'].astype(float)
Sep_BS_A['Unnamed: 0'] = Sep_BS_A['Unnamed: 0'].astype(float)
Oct_BS_A['0'] = Oct_BS_A['0'].astype(float)
Oct_BS_A['Unnamed: 0'] = Oct_BS_A['Unnamed: 0'].astype(float)
Nov_BS_A['0'] = Nov_BS_A['0'].astype(float)
Nov_BS_A['Unnamed: 0'] = Nov_BS_A['Unnamed: 0'].astype(float) 
Dec_BS_A['0'] = Dec_BS_A['0'].astype(float)
Dec_BS_A['Unnamed: 0'] = Dec_BS_A['Unnamed: 0'].astype(float)


Jan_BS_A['time']=pd.date_range(start='1/1/2018', end='2/1/2018', freq='1min', closed='left')
Jan_BS_A['time'] = Jan_BS_A['time'].astype('str') 
Jan_BS_A[['local_date','local_time']] = Jan_BS_A.time.str.split(" ",expand=True,)


Jan_BS_A_mean=Jan_BS_A.groupby(Jan_BS_A.local_time).mean()
del Jan_BS_A_mean['Unnamed: 0']
Jan_BS_A_mean['time_series']=np.arange(0,len(Jan_BS_A_mean),1)
Jan_BS_A_mean=Jan_BS_A_mean.rename(columns={'0':'power'})
Jan_BS_A_mean['power']=Jan_BS_A_mean['power']
Jan_BS_A_mean['time_series']=Jan_BS_A_mean['time_series']/60




Feb_BS_A['time']=pd.date_range(start='2/1/2018', end='3/1/2018', freq='1min', closed='left')
Feb_BS_A['time'] = Feb_BS_A['time'].astype('str') 
Feb_BS_A[['local_date','local_time']] = Feb_BS_A.time.str.split(" ",expand=True,)
Feb_BS_A_mean=Feb_BS_A.groupby(Feb_BS_A.local_time).mean()
del Feb_BS_A_mean['Unnamed: 0']
Feb_BS_A_mean['time_series']=np.arange(0,len(Feb_BS_A_mean),1)
Feb_BS_A_mean=Feb_BS_A_mean.rename(columns={'0':'power'})
Feb_BS_A_mean['power']=Feb_BS_A_mean['power']
Feb_BS_A_mean['time_series']=Feb_BS_A_mean['time_series']/60

Mar_BS_A['time']=pd.date_range(start='3/1/2018', end='4/1/2018', freq='1min', closed='left')
Mar_BS_A['time'] = Mar_BS_A['time'].astype('str') 
Mar_BS_A[['local_date','local_time']] = Mar_BS_A.time.str.split(" ",expand=True,)
Mar_BS_A_mean=Mar_BS_A.groupby(Mar_BS_A.local_time).mean()
del Mar_BS_A_mean['Unnamed: 0']
Mar_BS_A_mean['time_series']=np.arange(0,len(Mar_BS_A_mean),1)
Mar_BS_A_mean=Mar_BS_A_mean.rename(columns={'0':'power'})
Mar_BS_A_mean['power']=Mar_BS_A_mean['power']
Mar_BS_A_mean['time_series']=Mar_BS_A_mean['time_series']/60

Apr_BS_A['time']=pd.date_range(start='4/1/2018', end='5/1/2018', freq='1min', closed='left')
Apr_BS_A['time'] = Apr_BS_A['time'].astype('str') 
Apr_BS_A[['local_date','local_time']] = Apr_BS_A.time.str.split(" ",expand=True,)
Apr_BS_A_mean=Apr_BS_A.groupby(Apr_BS_A.local_time).mean()
del Apr_BS_A_mean['Unnamed: 0']
Apr_BS_A_mean['time_series']=np.arange(0,len(Apr_BS_A_mean),1)
Apr_BS_A_mean=Apr_BS_A_mean.rename(columns={'0':'power'})
Apr_BS_A_mean['power']=Apr_BS_A_mean['power']
Apr_BS_A_mean['time_series']=Apr_BS_A_mean['time_series']/60

May_BS_A['time']=pd.date_range(start='5/1/2018', end='6/1/2018', freq='1min', closed='left')
May_BS_A['time'] = May_BS_A['time'].astype('str') 
May_BS_A[['local_date','local_time']] = May_BS_A.time.str.split(" ",expand=True,)
May_BS_A_mean=May_BS_A.groupby(May_BS_A.local_time).mean()
del May_BS_A_mean['Unnamed: 0']
May_BS_A_mean['time_series']=np.arange(0,len(May_BS_A_mean),1)
May_BS_A_mean=May_BS_A_mean.rename(columns={'0':'power'})
May_BS_A_mean['power']=May_BS_A_mean['power']
May_BS_A_mean['time_series']=May_BS_A_mean['time_series']/60

Jun_BS_A['time']=pd.date_range(start='6/1/2018', end='7/1/2018', freq='1min', closed='left')
Jun_BS_A['time'] = Jun_BS_A['time'].astype('str') 
Jun_BS_A[['local_date','local_time']] = Jun_BS_A.time.str.split(" ",expand=True,)
Jun_BS_A_mean=Jun_BS_A.groupby(Jun_BS_A.local_time).mean()
del Jun_BS_A_mean['Unnamed: 0']
Jun_BS_A_mean['time_series']=np.arange(0,len(Jun_BS_A_mean),1)
Jun_BS_A_mean=Jun_BS_A_mean.rename(columns={'0':'power'})
Jun_BS_A_mean['power']=Jun_BS_A_mean['power']
Jun_BS_A_mean['time_series']=Jun_BS_A_mean['time_series']/60

Jul_BS_A['time']=pd.date_range(start='7/1/2018', end='8/1/2018', freq='1min', closed='left')
Jul_BS_A['time'] = Jul_BS_A['time'].astype('str') 
Jul_BS_A[['local_date','local_time']] = Jul_BS_A.time.str.split(" ",expand=True,)
Jul_BS_A_mean=Jul_BS_A.groupby(Jul_BS_A.local_time).mean()
del Jul_BS_A_mean['Unnamed: 0']
Jul_BS_A_mean['time_series']=np.arange(0,len(Jul_BS_A_mean),1)
Jul_BS_A_mean=Jul_BS_A_mean.rename(columns={'0':'power'})
Jul_BS_A_mean['power']=Jul_BS_A_mean['power']
Jul_BS_A_mean['time_series']=Jul_BS_A_mean['time_series']/60

Aug_BS_A['time']=pd.date_range(start='8/1/2018', end='9/1/2018', freq='1min', closed='left')
Aug_BS_A['time'] = Aug_BS_A['time'].astype('str') 
Aug_BS_A[['local_date','local_time']] = Aug_BS_A.time.str.split(" ",expand=True,)
Aug_BS_A_mean=Aug_BS_A.groupby(Aug_BS_A.local_time).mean()
del Aug_BS_A_mean['Unnamed: 0']
Aug_BS_A_mean['time_series']=np.arange(0,len(Aug_BS_A_mean),1)
Aug_BS_A_mean=Aug_BS_A_mean.rename(columns={'0':'power'})
Aug_BS_A_mean['power']=Aug_BS_A_mean['power']
Aug_BS_A_mean['time_series']=Aug_BS_A_mean['time_series']/60

Sep_BS_A['time']=pd.date_range(start='9/1/2018', end='10/1/2018', freq='1min', closed='left')
Sep_BS_A['time'] = Sep_BS_A['time'].astype('str') 
Sep_BS_A[['local_date','local_time']] = Sep_BS_A.time.str.split(" ",expand=True,)
Sep_BS_A_mean=Sep_BS_A.groupby(Sep_BS_A.local_time).mean()
del Sep_BS_A_mean['Unnamed: 0']
Sep_BS_A_mean['time_series']=np.arange(0,len(Sep_BS_A_mean),1)
Sep_BS_A_mean=Sep_BS_A_mean.rename(columns={'0':'power'})
Sep_BS_A_mean['power']=Sep_BS_A_mean['power']
Sep_BS_A_mean['time_series']=Sep_BS_A_mean['time_series']/60

Oct_BS_A['time']=pd.date_range(start='10/1/2018', end='11/1/2018', freq='1min', closed='left')
Oct_BS_A['time'] = Oct_BS_A['time'].astype('str') 
Oct_BS_A[['local_date','local_time']] = Oct_BS_A.time.str.split(" ",expand=True,)
Oct_BS_A_mean=Oct_BS_A.groupby(Oct_BS_A.local_time).mean()
del Oct_BS_A_mean['Unnamed: 0']
Oct_BS_A_mean['time_series']=np.arange(0,len(Oct_BS_A_mean),1)
Oct_BS_A_mean=Oct_BS_A_mean.rename(columns={'0':'power'})
Oct_BS_A_mean['power']=Oct_BS_A_mean['power']
Oct_BS_A_mean['time_series']=Oct_BS_A_mean['time_series']/60

Nov_BS_A['time']=pd.date_range(start='11/1/2018', end='12/1/2018', freq='1min', closed='left')
Nov_BS_A['time'] = Nov_BS_A['time'].astype('str') 
Nov_BS_A[['local_date','local_time']] = Nov_BS_A.time.str.split(" ",expand=True,)
Nov_BS_A_mean=Nov_BS_A.groupby(Nov_BS_A.local_time).mean()
del Nov_BS_A_mean['Unnamed: 0']
Nov_BS_A_mean['time_series']=np.arange(0,len(Nov_BS_A_mean),1)
Nov_BS_A_mean=Nov_BS_A_mean.rename(columns={'0':'power'})
Nov_BS_A_mean['power']=Nov_BS_A_mean['power']
Nov_BS_A_mean['time_series']=Nov_BS_A_mean['time_series']/60

Dec_BS_A['time']=pd.date_range(start='12/1/2018', end='1/1/2019', freq='1min', closed='left')
Dec_BS_A['time'] = Dec_BS_A['time'].astype('str') 
Dec_BS_A[['local_date','local_time']] = Dec_BS_A.time.str.split(" ",expand=True,)
Dec_BS_A_mean=Dec_BS_A.groupby(Dec_BS_A.local_time).mean()
del Dec_BS_A_mean['Unnamed: 0']
Dec_BS_A_mean['time_series']=np.arange(0,len(Dec_BS_A_mean),1)
Dec_BS_A_mean=Dec_BS_A_mean.rename(columns={'0':'power'})
Dec_BS_A_mean['power']=Dec_BS_A_mean['power']
Dec_BS_A_mean['time_series']=Dec_BS_A_mean['time_series']/60



import matplotlib.pyplot as plt 
fig, axs = plt.subplots(3, 4)
l0,=axs[0, 0].plot(Jan['time_series'], Jan['0'],color='pink',linewidth=1)
l1,=axs[0, 0].plot(Jan_1['time_series'], Jan_1['0'],color='lightsteelblue',linewidth=1)
l2,=axs[0, 0].plot(Jan_BS_A_mean['time_series'], Jan_BS_A_mean['power'],color='blue',linewidth=1)
axs[0, 0].set_title('January')
#axs[0, 0].set_yticks([0, 5, 10, 15, 20, 25])
axs[0, 1].plot(Feb['time_series'], Feb['0'],color='pink',linewidth=1)
axs[0, 1].plot(Feb_1['time_series'], Feb_1['0'],color='lightsteelblue',linewidth=1)
axs[0, 1].plot(Feb_BS_A_mean['time_series'], Feb_BS_A_mean['power'],color='blue',linewidth=1)
axs[0, 1].set_title('February')
axs[0, 2].plot(Mar['time_series'], Mar['0'],color='pink',linewidth=1)
axs[0, 2].plot(Mar_1['time_series'], Mar_1['0'],color='lightsteelblue',linewidth=1)
axs[0, 2].plot(Mar_BS_A_mean['time_series'], Jan_BS_A_mean['power'],color='blue',linewidth=1)
axs[0, 2].set_title('March')
axs[0, 3].plot(Apr['time_series'], Apr['0'],color='pink',linewidth=1)
axs[0, 3].plot(Apr_1['time_series'], Apr_1['0'],color='lightsteelblue',linewidth=1)
axs[0, 3].plot(Apr_BS_A_mean['time_series'], Apr_BS_A_mean['power'],color='blue',linewidth=1)
axs[0, 3].set_title('April')
axs[1, 0].plot(May['time_series'], May['0'],color='pink',linewidth=1)
axs[1, 0].plot(May_1['time_series'], May_1['0'],color='lightsteelblue',linewidth=1)
axs[1, 0].plot(May_BS_A_mean['time_series'], May_BS_A_mean['power'],color='blue',linewidth=1)
axs[1, 0].set_title('May')
#axs[1, 0].set_yticks([0, 5, 10, 15, 20, 25])
axs[1, 1].plot(Jun['time_series'], Jun['0'],color='pink',linewidth=1)
axs[1, 1].plot(Jun_1['time_series'], Jun_1['0'],color='lightsteelblue',linewidth=1)
axs[1, 1].plot(Jun_BS_A_mean['time_series'], Jun_BS_A_mean['power'],color='blue',linewidth=1)
axs[1, 1].set_title('June')
axs[1, 2].plot(Jul['time_series'], Jul['0'],color='pink',linewidth=1)
axs[1, 2].plot(Jul_1['time_series'], Jul_1['0'],color='lightsteelblue',linewidth=1)
axs[1, 2].plot(Jul_BS_A_mean['time_series'], Jul_BS_A_mean['power'],color='blue',linewidth=1)
axs[1, 2].set_title('July')
axs[1, 3].plot(Aug['time_series'], Aug['0'],color='pink',linewidth=1)
axs[1, 3].plot(Aug_1['time_series'], Aug_1['0'],color='lightsteelblue',linewidth=1)
axs[1, 3].plot(Aug_BS_A_mean['time_series'], Aug_BS_A_mean['power'],color='blue',linewidth=1)
axs[1, 3].set_title('August')
axs[2, 0].plot(Sep['time_series'], Sep['0'],color='pink',linewidth=1)
axs[2, 0].plot(Sep_1['time_series'], Sep_1['0'],color='lightsteelblue',linewidth=1)
axs[2, 0].plot(Sep_BS_A_mean['time_series'], Sep_BS_A_mean['power'],color='blue',linewidth=1)
axs[2, 0].set_title('September')
#axs[2, 0].set_yticks([0, 5, 10, 15, 20, 25])
axs[2, 0].set_xticks([0, 10, 20])
axs[2, 1].plot(Oct['time_series'], Oct['0'],color='pink',linewidth=1)
axs[2, 1].plot(Oct_1['time_series'], Oct_1['0'],color='lightsteelblue',linewidth=1)
axs[2, 1].plot(Oct_BS_A_mean['time_series'], Oct_BS_A_mean['power'],color='blue',linewidth=1)
axs[2, 1].set_title('October')
axs[2, 1].set_xticks([0, 10, 20])
axs[2, 2].plot(Nov['time_series'], Nov['0'],color='pink',linewidth=1)
axs[2, 2].plot(Nov_1['time_series'], Nov_1['0'],color='lightsteelblue',linewidth=1)
axs[2, 2].plot(Nov_BS_A_mean['time_series'], Nov_BS_A_mean['power'],color='blue',linewidth=1)
axs[2, 2].set_title('November')
axs[2, 2].set_xticks([0, 10, 20])
axs[2, 3].plot(Dec['time_series'], Dec['0'],color='pink',linewidth=1)
axs[2, 3].plot(Dec_1['time_series'], Dec_1['0'],color='lightsteelblue',linewidth=1)
axs[2, 3].plot(Dec_BS_A_mean['time_series'], Dec_BS_A_mean['power'],color='blue',linewidth=1)
axs[2, 3].set_title('December')
axs[2, 3].set_xticks([0, 10, 20])
for ax in axs.flat:
    ax.set(xlabel='Local time (h)', ylabel='Power (W)')
#Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
plt.subplots_adjust(bottom=0.1, right=1.7, top=1.5)
plt.figure(figsize=(25,50))
plt.tight_layout(pad=0.4, w_pad=1, h_pad=1.0)
#plt.savefig('profiles_temp_raq_2018.png', dpi=200,bbox_inches="tight")
ax.legend(handles = [l0,l1,l2] , labels=['atypical', 'occasional', 'average'],bbox_to_anchor=(1.7,3.5),fancybox=False,loc='upper right', shadow=False)
fig.savefig('demand_profiles_raq_bs.png',dpi=600,bbox_inches="tight")
plt.show()

Jan_sort=Jan
Jan_sort=Jan.sort_values(['0'],ascending=False)
Jan_sort=Jan_sort.reset_index()
Jan_sort
del Jan_sort['index']
del Jan_sort['time_series']
Jan_sort['index_1']=Jan_sort.index[()]
for i in range (0,len(Jan_sort),1):
     Jan_sort.loc[Jan_sort['index_1']>=0, 'index_2'] = Jan_sort['index_1']/(len(Jan_sort)-1)
Feb_sort=Feb
Feb_sort=Feb.sort_values(['0'],ascending=False)
Feb_sort=Feb_sort.reset_index()
del Feb_sort['index']
del Feb_sort['time_series']
Feb_sort['index_1']=Feb_sort.index[()]
for i in range (0,len(Feb_sort),1):
     Feb_sort.loc[Feb_sort['index_1']>=0, 'index_2'] = Feb_sort['index_1']/(len(Feb_sort)-1)
Mar_sort=Mar
Mar_sort=Mar.sort_values(['0'],ascending=False)
Mar_sort=Mar_sort.reset_index()
Mar_sort
del Mar_sort['index']
del Mar_sort['time_series']
Mar_sort['index_1']=Mar_sort.index[()]
for i in range (0,len(Mar_sort),1):
     Mar_sort.loc[Mar_sort['index_1']>=0, 'index_2'] = Mar_sort['index_1']/(len(Mar_sort)-1)
Apr_sort=Apr
Apr_sort=Apr.sort_values(['0'],ascending=False)
Apr_sort=Apr_sort.reset_index()
Apr_sort
del Apr_sort['index']
del Apr_sort['time_series']
Apr_sort['index_1']=Apr_sort.index[()]
for i in range (0,len(Apr_sort),1):
     Apr_sort.loc[Apr_sort['index_1']>=0, 'index_2'] = Apr_sort['index_1']/(len(Apr_sort)-1)
May_sort=May
May_sort=May.sort_values(['0'],ascending=False)
May_sort=May_sort.reset_index()
May_sort
del May_sort['index']
del May_sort['time_series']
May_sort['index_1']=May_sort.index[()]
for i in range (0,len(May_sort),1):
     May_sort.loc[May_sort['index_1']>=0, 'index_2'] = May_sort['index_1']/(len(May_sort)-1)
Jun_sort=Jun
Jun_sort=Jun.sort_values(['0'],ascending=False)
Jun_sort=Jun_sort.reset_index()
Jun_sort
del Jun_sort['index']
del Jun_sort['time_series']
Jun_sort['index_1']=Jun_sort.index[()]
for i in range (0,len(Jun_sort),1):
     Jun_sort.loc[Jun_sort['index_1']>=0, 'index_2'] = Jun_sort['index_1']/(len(Jun_sort)-1)
Jul_sort=Jul
Jul_sort=Jul.sort_values(['0'],ascending=False)
Jul_sort=Jul_sort.reset_index()
Jul_sort
del Jul_sort['index']
del Jul_sort['time_series']
Jul_sort['index_1']=Jul_sort.index[()]
for i in range (0,len(Jul_sort),1):
     Jul_sort.loc[Jul_sort['index_1']>=0, 'index_2'] = Jul_sort['index_1']/(len(Jul_sort)-1)
Aug_sort=Aug
Aug_sort=Aug.sort_values(['0'],ascending=False)
Aug_sort=Aug_sort.reset_index()
Aug_sort
del Aug_sort['index']
del Aug_sort['time_series']
Aug_sort['index_1']=Aug_sort.index[()]
for i in range (0,len(Aug_sort),1):
     Aug_sort.loc[Aug_sort['index_1']>=0, 'index_2'] = Aug_sort['index_1']/(len(Aug_sort)-1)
Sep_sort=Sep
Sep_sort=Sep.sort_values(['0'],ascending=False)
Sep_sort=Sep_sort.reset_index()
Sep_sort
del Sep_sort['index']
del Sep_sort['time_series']
Sep_sort['index_1']=Sep_sort.index[()]
for i in range (0,len(Sep_sort),1):
     Sep_sort.loc[Sep_sort['index_1']>=0, 'index_2'] = Sep_sort['index_1']/(len(Sep_sort)-1)
Oct_sort=Oct
Oct_sort=Oct.sort_values(['0'],ascending=False)
Oct_sort=Oct_sort.reset_index()
Oct_sort
del Oct_sort['index']
del Oct_sort['time_series']
Oct_sort['index_1']=Oct_sort.index[()]
for i in range (0,len(Oct_sort),1):
     Oct_sort.loc[Oct_sort['index_1']>=0, 'index_2'] = Oct_sort['index_1']/(len(Oct_sort)-1)
Nov_sort=Nov
Nov_sort=Nov.sort_values(['0'],ascending=False)
Nov_sort=Nov_sort.reset_index()
Nov_sort
del Nov_sort['index']
del Nov_sort['time_series']
Nov_sort['index_1']=Nov_sort.index[()]
for i in range (0,len(Nov_sort),1):
     Nov_sort.loc[Nov_sort['index_1']>=0, 'index_2'] = Nov_sort['index_1']/(len(Nov_sort)-1)
Dec_sort=Dec
Dec_sort=Dec.sort_values(['0'],ascending=False)
Dec_sort=Dec_sort.reset_index()
Dec_sort
del Dec_sort['index']
del Dec_sort['time_series']
Dec_sort['index_1']=Dec_sort.index[()]
for i in range (0,len(Dec_sort),1):
     Dec_sort.loc[Dec_sort['index_1']>=0, 'index_2'] = Dec_sort['index_1']/(len(Dec_sort)-1)

Jan_1_sort=Jan_1
Jan_1_sort=Jan_1.sort_values(['0'],ascending=False)
Jan_1_sort=Jan_1_sort.reset_index()
Jan_1_sort
del Jan_1_sort['index']
del Jan_1_sort['time_series']
Jan_1_sort['index_1']=Jan_1_sort.index[()]
for i in range (0,len(Jan_1_sort),1):
     Jan_1_sort.loc[Jan_1_sort['index_1']>=0, 'index_2'] = Jan_1_sort['index_1']/(len(Jan_1_sort)-1)
Feb_1_sort=Feb_1
Feb_1_sort=Feb_1.sort_values(['0'],ascending=False)
Feb_1_sort=Feb_1_sort.reset_index()
del Feb_1_sort['index']
del Feb_1_sort['time_series']
Feb_1_sort['index_1']=Feb_1_sort.index[()]
for i in range (0,len(Feb_1_sort),1):
     Feb_1_sort.loc[Feb_1_sort['index_1']>=0, 'index_2'] = Feb_1_sort['index_1']/(len(Feb_1_sort)-1)
Mar_1_sort=Mar_1
Mar_1_sort=Mar_1.sort_values(['0'],ascending=False)
Mar_1_sort=Mar_1_sort.reset_index()
Mar_1_sort
del Mar_1_sort['index']
del Mar_1_sort['time_series']
Mar_1_sort['index_1']=Mar_1_sort.index[()]
for i in range (0,len(Mar_1_sort),1):
     Mar_1_sort.loc[Mar_1_sort['index_1']>=0, 'index_2'] = Mar_1_sort['index_1']/(len(Mar_1_sort)-1)
Apr_1_sort=Apr_1
Apr_1_sort=Apr_1.sort_values(['0'],ascending=False)
Apr_1_sort=Apr_1_sort.reset_index()
Apr_1_sort
del Apr_1_sort['index']
del Apr_1_sort['time_series']
Apr_1_sort['index_1']=Apr_1_sort.index[()]
for i in range (0,len(Apr_1_sort),1):
     Apr_1_sort.loc[Apr_1_sort['index_1']>=0, 'index_2'] = Apr_1_sort['index_1']/(len(Apr_1_sort)-1)
May_1_sort=May_1
May_1_sort=May_1.sort_values(['0'],ascending=False)
May_1_sort=May_1_sort.reset_index()
May_1_sort
del May_1_sort['index']
del May_1_sort['time_series']
May_1_sort['index_1']=May_1_sort.index[()]
for i in range (0,len(May_1_sort),1):
     May_1_sort.loc[May_1_sort['index_1']>=0, 'index_2'] = May_1_sort['index_1']/(len(May_1_sort)-1)
Jun_1_sort=Jun_1
Jun_1_sort=Jun_1.sort_values(['0'],ascending=False)
Jun_1_sort=Jun_1_sort.reset_index()
Jun_1_sort
del Jun_1_sort['index']
del Jun_1_sort['time_series']
Jun_1_sort['index_1']=Jun_1_sort.index[()]
for i in range (0,len(Jun_1_sort),1):
     Jun_1_sort.loc[Jun_1_sort['index_1']>=0, 'index_2'] = Jun_1_sort['index_1']/(len(Jun_1_sort)-1)
Jul_1_sort=Jul_1
Jul_1_sort=Jul_1.sort_values(['0'],ascending=False)
Jul_1_sort=Jul_1_sort.reset_index()
Jul_1_sort
del Jul_1_sort['index']
del Jul_1_sort['time_series']
Jul_1_sort['index_1']=Jul_1_sort.index[()]
for i in range (0,len(Jul_1_sort),1):
     Jul_1_sort.loc[Jul_1_sort['index_1']>=0, 'index_2'] = Jul_1_sort['index_1']/(len(Jul_1_sort)-1)
Aug_1_sort=Aug_1
Aug_1_sort=Aug_1.sort_values(['0'],ascending=False)
Aug_1_sort=Aug_1_sort.reset_index()
Aug_1_sort
del Aug_1_sort['index']
del Aug_1_sort['time_series']
Aug_1_sort['index_1']=Aug_1_sort.index[()]
for i in range (0,len(Aug_1_sort),1):
     Aug_1_sort.loc[Aug_1_sort['index_1']>=0, 'index_2'] = Aug_1_sort['index_1']/(len(Aug_1_sort)-1)
Sep_1_sort=Sep_1
Sep_1_sort=Sep_1.sort_values(['0'],ascending=False)
Sep_1_sort=Sep_1_sort.reset_index()
Sep_1_sort
del Sep_1_sort['index']
del Sep_1_sort['time_series']
Sep_1_sort['index_1']=Sep_1_sort.index[()]
for i in range (0,len(Sep_1_sort),1):
     Sep_1_sort.loc[Sep_1_sort['index_1']>=0, 'index_2'] = Sep_1_sort['index_1']/(len(Sep_1_sort)-1)
Oct_1_sort=Oct_1
Oct_1_sort=Oct_1.sort_values(['0'],ascending=False)
Oct_1_sort=Oct_1_sort.reset_index()
Oct_1_sort
del Oct_1_sort['index']
del Oct_1_sort['time_series']
Oct_1_sort['index_1']=Oct_1_sort.index[()]
for i in range (0,len(Oct_1_sort),1):
     Oct_1_sort.loc[Oct_1_sort['index_1']>=0, 'index_2'] = Oct_1_sort['index_1']/(len(Oct_1_sort)-1)
Nov_1_sort=Nov_1
Nov_1_sort=Nov_1.sort_values(['0'],ascending=False)
Nov_1_sort=Nov_1_sort.reset_index()
Nov_1_sort
del Nov_1_sort['index']
del Nov_1_sort['time_series']
Nov_1_sort['index_1']=Nov_1_sort.index[()]
for i in range (0,len(Nov_1_sort),1):
     Nov_1_sort.loc[Nov_1_sort['index_1']>=0, 'index_2'] = Nov_1_sort['index_1']/(len(Nov_1_sort)-1)
Dec_1_sort=Dec_1
Dec_1_sort=Dec_1.sort_values(['0'],ascending=False)
Dec_1_sort=Dec_1_sort.reset_index()
Dec_1_sort
del Dec_1_sort['index']
del Dec_1_sort['time_series']
Dec_1_sort['index_1']=Dec_1_sort.index[()]
for i in range (0,len(Dec_1_sort),1):
     Dec_1_sort.loc[Dec_1_sort['index_1']>=0, 'index_2'] = Dec_1_sort['index_1']/(len(Dec_1_sort)-1)



Jan_BS_A_mean_sort=Jan_BS_A_mean
Jan_BS_A_mean_sort=Jan_BS_A_mean.sort_values(['power'],ascending=False)
Jan_BS_A_mean_sort=Jan_BS_A_mean_sort.reset_index()
del Jan_BS_A_mean_sort['local_time']
del Jan_BS_A_mean_sort['time_series']
Jan_BS_A_mean_sort['index_1']=Jan_BS_A_mean_sort.index[()]
for i in range (0,len(Jan_BS_A_mean_sort),1):
     Jan_BS_A_mean_sort.loc[Jan_BS_A_mean_sort['index_1']>=0, 'index_2'] = Jan_BS_A_mean_sort['index_1']/(len(Jan_BS_A_mean_sort)-1)

Feb_BS_A_mean_sort=Feb_BS_A_mean
Feb_BS_A_mean_sort=Feb_BS_A_mean.sort_values(['power'],ascending=False)
Feb_BS_A_mean_sort=Feb_BS_A_mean_sort.reset_index()
del Feb_BS_A_mean_sort['local_time']
del Feb_BS_A_mean_sort['time_series']
Feb_BS_A_mean_sort['index_1']=Feb_BS_A_mean_sort.index[()]
for i in range (0,len(Feb_BS_A_mean_sort),1):
     Feb_BS_A_mean_sort.loc[Feb_BS_A_mean_sort['index_1']>=0, 'index_2'] = Feb_BS_A_mean_sort['index_1']/(len(Feb_BS_A_mean_sort)-1)

Mar_BS_A_mean_sort=Mar_BS_A_mean
Mar_BS_A_mean_sort=Mar_BS_A_mean.sort_values(['power'],ascending=False)
Mar_BS_A_mean_sort=Mar_BS_A_mean_sort.reset_index()
Mar_BS_A_mean_sort
del Mar_BS_A_mean_sort['local_time']
del Mar_BS_A_mean_sort['time_series']
Mar_BS_A_mean_sort['index_1']=Mar_BS_A_mean_sort.index[()]
for i in range (0,len(Mar_BS_A_mean_sort),1):
     Mar_BS_A_mean_sort.loc[Mar_BS_A_mean_sort['index_1']>=0, 'index_2'] = Mar_BS_A_mean_sort['index_1']/(len(Mar_BS_A_mean_sort)-1)
Apr_BS_A_mean_sort=Apr_BS_A_mean
Apr_BS_A_mean_sort=Apr_BS_A_mean.sort_values(['power'],ascending=False)
Apr_BS_A_mean_sort=Apr_BS_A_mean_sort.reset_index()
Apr_BS_A_mean_sort
del Apr_BS_A_mean_sort['local_time']
del Apr_BS_A_mean_sort['time_series']
Apr_BS_A_mean_sort['index_1']=Apr_BS_A_mean_sort.index[()]
for i in range (0,len(Apr_BS_A_mean_sort),1):
     Apr_BS_A_mean_sort.loc[Apr_BS_A_mean_sort['index_1']>=0, 'index_2'] = Apr_BS_A_mean_sort['index_1']/(len(Apr_BS_A_mean_sort)-1)
May_BS_A_mean_sort=May_BS_A_mean
May_BS_A_mean_sort=May_BS_A_mean.sort_values(['power'],ascending=False)
May_BS_A_mean_sort=May_BS_A_mean_sort.reset_index()
May_BS_A_mean_sort
del May_BS_A_mean_sort['local_time']
del May_BS_A_mean_sort['time_series']
May_BS_A_mean_sort['index_1']=May_BS_A_mean_sort.index[()]
for i in range (0,len(May_BS_A_mean_sort),1):
     May_BS_A_mean_sort.loc[May_BS_A_mean_sort['index_1']>=0, 'index_2'] = May_BS_A_mean_sort['index_1']/(len(May_BS_A_mean_sort)-1)
Jun_BS_A_mean_sort=Jun_BS_A_mean
Jun_BS_A_mean_sort=Jun_BS_A_mean.sort_values(['power'],ascending=False)
Jun_BS_A_mean_sort=Jun_BS_A_mean_sort.reset_index()
Jun_BS_A_mean_sort
del Jun_BS_A_mean_sort['local_time']
del Jun_BS_A_mean_sort['time_series']
Jun_BS_A_mean_sort['index_1']=Jun_BS_A_mean_sort.index[()]
for i in range (0,len(Jun_BS_A_mean_sort),1):
     Jun_BS_A_mean_sort.loc[Jun_BS_A_mean_sort['index_1']>=0, 'index_2'] = Jun_BS_A_mean_sort['index_1']/(len(Jun_BS_A_mean_sort)-1)
Jul_BS_A_mean_sort=Jul_BS_A_mean
Jul_BS_A_mean_sort=Jul_BS_A_mean.sort_values(['power'],ascending=False)
Jul_BS_A_mean_sort=Jul_BS_A_mean_sort.reset_index()
Jul_BS_A_mean_sort
del Jul_BS_A_mean_sort['local_time']
del Jul_BS_A_mean_sort['time_series']
Jul_BS_A_mean_sort['index_1']=Jul_BS_A_mean_sort.index[()]
for i in range (0,len(Jul_BS_A_mean_sort),1):
     Jul_BS_A_mean_sort.loc[Jul_BS_A_mean_sort['index_1']>=0, 'index_2'] = Jul_BS_A_mean_sort['index_1']/(len(Jul_BS_A_mean_sort)-1)
Aug_BS_A_mean_sort=Aug_BS_A_mean
Aug_BS_A_mean_sort=Aug_BS_A_mean.sort_values(['power'],ascending=False)
Aug_BS_A_mean_sort=Aug_BS_A_mean_sort.reset_index()
Aug_BS_A_mean_sort
del Aug_BS_A_mean_sort['local_time']
del Aug_BS_A_mean_sort['time_series']
Aug_BS_A_mean_sort['index_1']=Aug_BS_A_mean_sort.index[()]
for i in range (0,len(Aug_BS_A_mean_sort),1):
     Aug_BS_A_mean_sort.loc[Aug_BS_A_mean_sort['index_1']>=0, 'index_2'] = Aug_BS_A_mean_sort['index_1']/(len(Aug_BS_A_mean_sort)-1)
Sep_BS_A_mean_sort=Sep_BS_A_mean
Sep_BS_A_mean_sort=Sep_BS_A_mean.sort_values(['power'],ascending=False)
Sep_BS_A_mean_sort=Sep_BS_A_mean_sort.reset_index()
Sep_BS_A_mean_sort
del Sep_BS_A_mean_sort['local_time']
del Sep_BS_A_mean_sort['time_series']
Sep_BS_A_mean_sort['index_1']=Sep_BS_A_mean_sort.index[()]
for i in range (0,len(Sep_BS_A_mean_sort),1):
     Sep_BS_A_mean_sort.loc[Sep_BS_A_mean_sort['index_1']>=0, 'index_2'] = Sep_BS_A_mean_sort['index_1']/(len(Sep_BS_A_mean_sort)-1)
Oct_BS_A_mean_sort=Oct_BS_A_mean
Oct_BS_A_mean_sort=Oct_BS_A_mean.sort_values(['power'],ascending=False)
Oct_BS_A_mean_sort=Oct_BS_A_mean_sort.reset_index()
Oct_BS_A_mean_sort
del Oct_BS_A_mean_sort['local_time']
del Oct_BS_A_mean_sort['time_series']
Oct_BS_A_mean_sort['index_1']=Oct_BS_A_mean_sort.index[()]
for i in range (0,len(Oct_BS_A_mean_sort),1):
     Oct_BS_A_mean_sort.loc[Oct_BS_A_mean_sort['index_1']>=0, 'index_2'] = Oct_BS_A_mean_sort['index_1']/(len(Oct_BS_A_mean_sort)-1)
Nov_BS_A_mean_sort=Nov_BS_A_mean
Nov_BS_A_mean_sort=Nov_BS_A_mean.sort_values(['power'],ascending=False)
Nov_BS_A_mean_sort=Nov_BS_A_mean_sort.reset_index()
Nov_BS_A_mean_sort
del Nov_BS_A_mean_sort['local_time']
del Nov_BS_A_mean_sort['time_series']
Nov_BS_A_mean_sort['index_1']=Nov_BS_A_mean_sort.index[()]
for i in range (0,len(Nov_BS_A_mean_sort),1):
     Nov_BS_A_mean_sort.loc[Nov_BS_A_mean_sort['index_1']>=0, 'index_2'] = Nov_BS_A_mean_sort['index_1']/(len(Nov_BS_A_mean_sort)-1)
Dec_BS_A_mean_sort=Dec_BS_A_mean
Dec_BS_A_mean_sort=Dec_BS_A_mean.sort_values(['power'],ascending=False)
Dec_BS_A_mean_sort=Dec_BS_A_mean_sort.reset_index()
Dec_BS_A_mean_sort
del Dec_BS_A_mean_sort['local_time']
del Dec_BS_A_mean_sort['time_series']
Dec_BS_A_mean_sort['index_1']=Dec_BS_A_mean_sort.index[()]
for i in range (0,len(Dec_BS_A_mean_sort),1):
     Dec_BS_A_mean_sort.loc[Dec_BS_A_mean_sort['index_1']>=0, 'index_2'] = Dec_BS_A_mean_sort['index_1']/(len(Dec_BS_A_mean_sort)-1)
     
     
import matplotlib.ticker as mtick

import matplotlib.pyplot as plt 
fig, axs = plt.subplots(nrows=4, ncols=3)
axs[0, 0].plot(Jan_sort['index_2'], Jan_sort['0'],color='pink',linewidth=1)
axs[0, 0].plot(Jan_1_sort['index_2'], Jan_1_sort['0'],color='lightsteelblue',linewidth=1)
axs[0, 0].plot(Jan_BS_A_mean_sort['index_2'], Jan_BS_A_mean_sort['power'],color='blue',linewidth=1)
axs[0, 0].set_title('January')
#axs[0, 0].set_yticks([0, 5, 10, 15, 20, 25])
axs[0, 0].set_xticks([0,0.2,0.4,0.6,0.8,1])
axs[0, 0].xaxis.set_tick_params(direction='in', which='both')
axs[0, 0].yaxis.set_tick_params(direction='in', which='both')
axs[0, 0].yaxis.set_ticks_position('both')
axs[0, 0].xaxis.set_ticks_position('both')
axs[0, 0].xaxis.set_major_formatter(mtick.PercentFormatter(1))
axs[0, 1].plot(Feb_sort['index_2'], Feb_sort['0'],color='pink',linewidth=1)
axs[0, 1].plot(Feb_1_sort['index_2'], Feb_1_sort['0'],color='lightsteelblue',linewidth=1)
axs[0, 1].plot(Feb_BS_A_mean_sort['index_2'], Feb_BS_A_mean_sort['power'],color='blue',linewidth=1)
axs[0, 1].set_title('February')
#axs[0, 1].set_yticks([0, 5, 10, 15, 20, 25])
axs[0, 1].set_xticks([0,0.2,0.4,0.6,0.8,1])
axs[0, 1].xaxis.set_tick_params(direction='in', which='both')
axs[0, 1].yaxis.set_tick_params(direction='in', which='both')
axs[0, 1].yaxis.set_ticks_position('both')
axs[0, 1].xaxis.set_ticks_position('both')
axs[0, 1].xaxis.set_major_formatter(mtick.PercentFormatter(1))
axs[0, 2].plot(Mar_sort['index_2'], Mar_sort['0'],color='pink',linewidth=1)
axs[0, 2].plot(Mar_1_sort['index_2'], Mar_1_sort['0'],color='lightsteelblue',linewidth=1)
axs[0, 2].plot(Mar_BS_A_mean_sort['index_2'], Mar_BS_A_mean_sort['power'],color='blue',linewidth=1)
axs[0, 2].set_title('March')
#axs[0, 2].set_yticks([0, 5, 10, 15, 20, 25])
axs[0, 2].set_xticks([0,0.2,0.4,0.6,0.8,1])
axs[0, 2].xaxis.set_tick_params(direction='in', which='both')
axs[0, 2].yaxis.set_tick_params(direction='in', which='both')
axs[0, 2].yaxis.set_ticks_position('both')
axs[0, 2].xaxis.set_ticks_position('both')
axs[0, 2].xaxis.set_major_formatter(mtick.PercentFormatter(1))
axs[1, 0].plot(Apr_sort['index_2'], Apr_sort['0'],color='pink',linewidth=1)
axs[1, 0].plot(Apr_1_sort['index_2'], Apr_1_sort['0'],color='lightsteelblue',linewidth=1)
axs[1, 0].plot(Apr_BS_A_mean_sort['index_2'], Apr_BS_A_mean_sort['power'],color='blue',linewidth=1)
axs[1, 0].set_title('April')
#axs[1, 0].set_yticks([0, 5, 10, 15, 20, 25])
axs[1, 0].set_xticks([0,0.2,0.4,0.6,0.8,1])
axs[1, 0].xaxis.set_tick_params(direction='in', which='both')
axs[1, 0].yaxis.set_tick_params(direction='in', which='both')
axs[1, 0].yaxis.set_ticks_position('both')
axs[1, 0].xaxis.set_ticks_position('both')
axs[1, 0].xaxis.set_major_formatter(mtick.PercentFormatter(1))
axs[1, 1].plot(May_sort['index_2'], May_sort['0'],color='pink',linewidth=1)
axs[1, 1].plot(May_1_sort['index_2'], May_1_sort['0'],color='lightsteelblue',linewidth=1)
axs[1, 1].plot(May_BS_A_mean_sort['index_2'], May_BS_A_mean_sort['power'],color='blue',linewidth=1)
axs[1, 1].set_title('May')
#axs[1, 1].set_yticks([0, 5, 10, 15, 20, 25])
axs[1, 1].set_xticks([0,0.2,0.4,0.6,0.8,1])
axs[1, 1].xaxis.set_tick_params(direction='in', which='both')
axs[1, 1].yaxis.set_tick_params(direction='in', which='both')
axs[1, 1].yaxis.set_ticks_position('both')
axs[1, 1].xaxis.set_ticks_position('both')
axs[1, 1].xaxis.set_major_formatter(mtick.PercentFormatter(1))
axs[1, 2].plot(Jun_sort['index_2'], Jun_sort['0'],color='pink',linewidth=1)
axs[1, 2].plot(Jun_1_sort['index_2'], Jun_1_sort['0'],color='lightsteelblue',linewidth=1)
axs[1, 2].plot(Jun_BS_A_mean_sort['index_2'], Jun_BS_A_mean_sort['power'],color='blue',linewidth=1)
axs[1, 2].set_title('June')
#axs[1, 2].set_yticks([0, 5, 10, 15, 20, 25])
axs[1, 2].set_xticks([0,0.2,0.4,0.6,0.8,1])
axs[1, 2].xaxis.set_tick_params(direction='in', which='both')
axs[1, 2].yaxis.set_tick_params(direction='in', which='both')
axs[1, 2].yaxis.set_ticks_position('both')
axs[1, 2].xaxis.set_ticks_position('both')
axs[1, 2].xaxis.set_major_formatter(mtick.PercentFormatter(1))
axs[2, 0].plot(Jul_sort['index_2'], Jul_sort['0'],color='pink',linewidth=1)
axs[2, 0].plot(Jul_1_sort['index_2'], Jul_1_sort['0'],color='lightsteelblue',linewidth=1)
axs[2, 0].plot(Jul_BS_A_mean_sort['index_2'], Jul_BS_A_mean_sort['power'],color='blue',linewidth=1)
axs[2, 0].set_title('July')
#axs[2, 0].set_yticks([0, 5, 10, 15, 20, 25])
axs[2, 0].set_xticks([0,0.2,0.4,0.6,0.8,1])
axs[2, 0].xaxis.set_tick_params(direction='in', which='both')
axs[2, 0].yaxis.set_tick_params(direction='in', which='both')
axs[2, 0].yaxis.set_ticks_position('both')
axs[2, 0].xaxis.set_ticks_position('both')
axs[2, 0].xaxis.set_major_formatter(mtick.PercentFormatter(1))
axs[2, 1].plot(Aug_sort['index_2'], Aug_sort['0'],color='pink',linewidth=1)
axs[2, 1].plot(Aug_1_sort['index_2'], Aug_1_sort['0'],color='lightsteelblue',linewidth=1)
axs[2, 1].plot(Aug_BS_A_mean_sort['index_2'], Aug_BS_A_mean_sort['power'],color='blue',linewidth=1)
axs[2, 1].set_title('August')
#axs[2, 1].set_yticks([0, 5, 10, 15, 20, 25])
axs[2, 1].set_xticks([0,0.2,0.4,0.6,0.8,1])
axs[2, 1].xaxis.set_tick_params(direction='in', which='both')
axs[2, 1].yaxis.set_tick_params(direction='in', which='both')
axs[2, 1].yaxis.set_ticks_position('both')
axs[2, 1].xaxis.set_ticks_position('both')
axs[2, 1].xaxis.set_major_formatter(mtick.PercentFormatter(1))
axs[2, 2].plot(Sep_sort['index_2'], Sep_sort['0'],color='pink',linewidth=1)
axs[2, 2].plot(Sep_1_sort['index_2'], Sep_1_sort['0'],color='lightsteelblue',linewidth=1)
axs[2, 2].plot(Sep_BS_A_mean_sort['index_2'], Sep_BS_A_mean_sort['power'],color='blue',linewidth=1)
axs[2, 2].set_title('September')
#axs[2, 2].set_yticks([0, 5, 10, 15, 20, 25])
axs[2, 2].set_xticks([0, 0.2, 0.4,0.6,0.8,1])
axs[2, 2].xaxis.set_tick_params(direction='in', which='both')
axs[2, 2].yaxis.set_tick_params(direction='in', which='both')
axs[2, 2].yaxis.set_ticks_position('both')
axs[2, 2].xaxis.set_ticks_position('both')
axs[2, 2].xaxis.set_major_formatter(mtick.PercentFormatter(1))
axs[3, 0].plot(Oct_sort['index_2'], Oct_sort['0'],color='pink',linewidth=1)
axs[3, 0].plot(Oct_1_sort['index_2'], Oct_1_sort['0'],color='lightsteelblue',linewidth=1)
axs[3, 0].plot(Oct_BS_A_mean_sort['index_2'], Oct_BS_A_mean_sort['power'],color='blue',linewidth=1)
axs[3, 0].set_title('October')
#axs[3, 0].set_yticks([0, 5, 10, 15, 20, 25])
axs[3, 0].set_xticks([0,0.2,0.4,0.6,0.8,1])
axs[3, 0].xaxis.set_tick_params(direction='in', which='both')
axs[3, 0].yaxis.set_tick_params(direction='in', which='both')
axs[3, 0].yaxis.set_ticks_position('both')
axs[3, 0].xaxis.set_ticks_position('both')
axs[3, 0].xaxis.set_major_formatter(mtick.PercentFormatter(1))
axs[3, 1].plot(Nov_sort['index_2'], Nov_sort['0'],color='pink',linewidth=1)
axs[3, 1].plot(Nov_1_sort['index_2'], Nov_1_sort['0'],color='lightsteelblue',linewidth=1)
axs[3, 1].plot(Nov_BS_A_mean_sort['index_2'], Nov_BS_A_mean_sort['power'],color='blue',linewidth=1)
axs[3, 1].set_title('November')
#axs[3, 1].set_yticks([0, 5, 10, 15, 20, 25])
axs[3, 1].set_xticks([0,0.2,0.4,0.6,0.8,1])
axs[3, 1].xaxis.set_tick_params(direction='in', which='both')
axs[3, 1].yaxis.set_tick_params(direction='in', which='both')
axs[3, 1].yaxis.set_ticks_position('both')
axs[3, 1].xaxis.set_ticks_position('both')
axs[3, 1].xaxis.set_major_formatter(mtick.PercentFormatter(1))
axs[3, 2].plot(Dec_sort['index_2'], Dec_sort['0'],color='pink',linewidth=1)
axs[3, 2].plot(Dec_1_sort['index_2'], Dec_1_sort['0'],color='lightsteelblue',linewidth=1)
axs[3, 2].plot(Dec_BS_A_mean_sort['index_2'], Dec_BS_A_mean_sort['power'],color='blue',linewidth=1)
axs[3, 2].set_title('December')
#axs[3, 2].set_yticks([0, 5, 10, 15, 20, 25])
axs[3, 2].set_xticks([0,0.2,0.4,0.6,0.8,1])
axs[3, 2].xaxis.set_tick_params(direction='in', which='both')
axs[3, 2].yaxis.set_tick_params(direction='in', which='both')
axs[3, 2].yaxis.set_ticks_position('both')
axs[3, 2].xaxis.set_ticks_position('both')
axs[3, 2].xaxis.set_major_formatter(mtick.PercentFormatter(1))

for ax in axs.flat:
    ax.set(xlabel='Percentage (%)', ylabel='Power (W)')
#Hide x labels and tick labels for top plots and y ticks for right plots.
#for ax in axs.flat:
    #ax.label_outer()
plt.subplots_adjust(bottom=0.1, right=2, top=2, hspace=0.55, wspace = 0.2)
plt.figure(figsize=(20,50))
plt.tight_layout(pad=0.5, w_pad=1, h_pad=1)
ax.set_xlim(0, 1)
ax.xaxis.set_tick_params(direction='in', which='both')
ax.yaxis.set_tick_params(direction='in', which='both')
#plt.savefig('profiles_temp_raq_2018.png', dpi=200,bbox_inches="tight")
ax.legend(handles = [l0,l1,l2] , labels=['atypical', 'occasional', 'average'],bbox_to_anchor=(1.5,5.5),fancybox=False,loc='upper right', shadow=False)
fig.savefig('frecuency_profiles_raq.png',dpi=600,bbox_inches="tight")
plt.show()
