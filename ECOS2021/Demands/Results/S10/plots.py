#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 10:41:47 2021

@author: alejandrosoto
"""

import pandas as pd
import numpy as np
#Ocasional
Jan=pd.read_csv('Jan_S10_o.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

Jan['0'] = Jan['0'].astype(float)
Jan['Unnamed: 0'] = Jan['Unnamed: 0'].astype(float)

#Typical
Jan_1=pd.read_csv('Jan_S10_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Feb_1=pd.read_csv('Feb_S10_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Mar_1=pd.read_csv('Mar_S10_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Apr_1=pd.read_csv('Apr_S10_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
May_1=pd.read_csv('May_S10_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jun_1=pd.read_csv('Jun_S10_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jul_1=pd.read_csv('Jul_S10_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Aug_1=pd.read_csv('Aug_S10_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Sep_1=pd.read_csv('Sep_S10_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Oct_1=pd.read_csv('Oct_S10_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Nov_1=pd.read_csv('Nov_S10_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Dec_1=pd.read_csv('Dec_S10_t.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
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


#Time conv
Jan['time_series']=np.arange(0,len(Jan),1)
Jan['time_series']=Jan['time_series']/60

Jan_1['time_series']=np.arange(0,len(Jan),1)
Jan_1['time_series']=Jan_1['time_series']/60
Feb_1['time_series']=np.arange(0,len(Feb_1),1)
Feb_1['time_series']=Feb_1['time_series']/60
Mar_1['time_series']=np.arange(0,len(Mar_1),1)
Mar_1['time_series']=Mar_1['time_series']/60
Apr_1['time_series']=np.arange(0,len(Apr_1),1)
Apr_1['time_series']=Apr_1['time_series']/60
May_1['time_series']=np.arange(0,len(May_1),1)
May_1['time_series']=May_1['time_series']/60
Jun_1['time_series']=np.arange(0,len(Jun_1),1)
Jun_1['time_series']=Jun_1['time_series']/60
Jul_1['time_series']=np.arange(0,len(Jul_1),1)
Jul_1['time_series']=Jul_1['time_series']/60
Aug_1['time_series']=np.arange(0,len(Aug_1),1)
Aug_1['time_series']=Aug_1['time_series']/60
Sep_1['time_series']=np.arange(0,len(Sep_1),1)
Sep_1['time_series']=Sep_1['time_series']/60
Oct_1['time_series']=np.arange(0,len(Oct_1),1)
Oct_1['time_series']=Oct_1['time_series']/60
Nov_1['time_series']=np.arange(0,len(Nov_1),1)
Nov_1['time_series']=Nov_1['time_series']/60
Dec_1['time_series']=np.arange(0,len(Dec_1),1)
Dec_1['time_series']=Dec_1['time_series']/60


#Scenarios (Created for S4 extented for Sn)

Jan_S4=pd.read_csv('Jan_S10_B.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Feb_S4=pd.read_csv('Feb_S10_B.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Mar_S4=pd.read_csv('Mar_S10_B.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Apr_S4=pd.read_csv('Apr_S10_B.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
May_S4=pd.read_csv('May_S10_B.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jun_S4=pd.read_csv('Jun_S10_B.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jul_S4=pd.read_csv('Jul_S10_B.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Aug_S4=pd.read_csv('Aug_S10_B.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Sep_S4=pd.read_csv('Sep_S10_B.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Oct_S4=pd.read_csv('Oct_S10_B.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Nov_S4=pd.read_csv('Nov_S10_B.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Dec_S4=pd.read_csv('Dec_S10_B.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jan_S4['0'] = Jan_S4['0'].astype(float)
Jan_S4['Unnamed: 0'] = Jan_S4['Unnamed: 0'].astype(float)
Feb_S4['0'] = Feb_S4['0'].astype(float)
Feb_S4['Unnamed: 0'] = Feb_S4['Unnamed: 0'].astype(float)
Mar_S4['0'] = Mar_S4['0'].astype(float)
Mar_S4['Unnamed: 0'] = Mar_S4['Unnamed: 0'].astype(float)
Apr_S4['0'] = Apr_S4['0'].astype(float)
Apr_S4['Unnamed: 0'] = Apr_S4['Unnamed: 0'].astype(float)
May_S4['0'] = May_S4['0'].astype(float)
May_S4['Unnamed: 0'] = May_S4['Unnamed: 0'].astype(float)
Jun_S4['0'] = Jun_S4['0'].astype(float)
Jun_S4['Unnamed: 0'] = Jun_S4['Unnamed: 0'].astype(float)
Jul_S4['0'] = Jul_S4['0'].astype(float)
Jul_S4['Unnamed: 0'] = Jul_S4['Unnamed: 0'].astype(float)
Aug_S4['0'] = Aug_S4['0'].astype(float)
Aug_S4['Unnamed: 0'] = Aug_S4['Unnamed: 0'].astype(float)
Sep_S4['0'] = Sep_S4['0'].astype(float)
Sep_S4['Unnamed: 0'] = Sep_S4['Unnamed: 0'].astype(float)
Oct_S4['0'] = Oct_S4['0'].astype(float)
Oct_S4['Unnamed: 0'] = Oct_S4['Unnamed: 0'].astype(float)
Nov_S4['0'] = Nov_S4['0'].astype(float)
Nov_S4['Unnamed: 0'] = Nov_S4['Unnamed: 0'].astype(float) 
Dec_S4['0'] = Dec_S4['0'].astype(float)
Dec_S4['Unnamed: 0'] = Dec_S4['Unnamed: 0'].astype(float)

#Mean at the same time for every point

Jan_S4['time']=pd.date_range(start='1/1/2018', end='2/1/2018', freq='1min', closed='left')
Jan_S4['time'] = Jan_S4['time'].astype('str') 
Jan_S4[['local_date','local_time']] = Jan_S4.time.str.split(" ",expand=True,)
Jan_S4_mean=Jan_S4.groupby(Jan_S4.local_time).mean()
del Jan_S4_mean['Unnamed: 0']
Jan_S4_mean['time_series']=np.arange(0,len(Jan_S4_mean),1)
Jan_S4_mean=Jan_S4_mean.rename(columns={'0':'power'})
Jan_S4_mean['power']=Jan_S4_mean['power']
Jan_S4_mean['time_series']=Jan_S4_mean['time_series']/60

Feb_S4['time']=pd.date_range(start='2/1/2018', end='3/1/2018', freq='1min', closed='left')
Feb_S4['time'] = Feb_S4['time'].astype('str') 
Feb_S4[['local_date','local_time']] = Feb_S4.time.str.split(" ",expand=True,)
Feb_S4_mean=Feb_S4.groupby(Feb_S4.local_time).mean()
del Feb_S4_mean['Unnamed: 0']
Feb_S4_mean['time_series']=np.arange(0,len(Feb_S4_mean),1)
Feb_S4_mean=Feb_S4_mean.rename(columns={'0':'power'})
Feb_S4_mean['power']=Feb_S4_mean['power']
Feb_S4_mean['time_series']=Feb_S4_mean['time_series']/60

Mar_S4['time']=pd.date_range(start='3/1/2018', end='4/1/2018', freq='1min', closed='left')
Mar_S4['time'] = Mar_S4['time'].astype('str') 
Mar_S4[['local_date','local_time']] = Mar_S4.time.str.split(" ",expand=True,)
Mar_S4_mean=Mar_S4.groupby(Mar_S4.local_time).mean()
del Mar_S4_mean['Unnamed: 0']
Mar_S4_mean['time_series']=np.arange(0,len(Mar_S4_mean),1)
Mar_S4_mean=Mar_S4_mean.rename(columns={'0':'power'})
Mar_S4_mean['power']=Mar_S4_mean['power']
Mar_S4_mean['time_series']=Mar_S4_mean['time_series']/60

Apr_S4['time']=pd.date_range(start='4/1/2018', end='5/1/2018', freq='1min', closed='left')
Apr_S4['time'] = Apr_S4['time'].astype('str') 
Apr_S4[['local_date','local_time']] = Apr_S4.time.str.split(" ",expand=True,)
Apr_S4_mean=Apr_S4.groupby(Apr_S4.local_time).mean()
del Apr_S4_mean['Unnamed: 0']
Apr_S4_mean['time_series']=np.arange(0,len(Apr_S4_mean),1)
Apr_S4_mean=Apr_S4_mean.rename(columns={'0':'power'})
Apr_S4_mean['power']=Apr_S4_mean['power']
Apr_S4_mean['time_series']=Apr_S4_mean['time_series']/60

May_S4['time']=pd.date_range(start='5/1/2018', end='6/1/2018', freq='1min', closed='left')
May_S4['time'] = May_S4['time'].astype('str') 
May_S4[['local_date','local_time']] = May_S4.time.str.split(" ",expand=True,)
May_S4_mean=May_S4.groupby(May_S4.local_time).mean()
del May_S4_mean['Unnamed: 0']
May_S4_mean['time_series']=np.arange(0,len(May_S4_mean),1)
May_S4_mean=May_S4_mean.rename(columns={'0':'power'})
May_S4_mean['power']=May_S4_mean['power']
May_S4_mean['time_series']=May_S4_mean['time_series']/60

Jun_S4['time']=pd.date_range(start='6/1/2018', end='7/1/2018', freq='1min', closed='left')
Jun_S4['time'] = Jun_S4['time'].astype('str') 
Jun_S4[['local_date','local_time']] = Jun_S4.time.str.split(" ",expand=True,)
Jun_S4_mean=Jun_S4.groupby(Jun_S4.local_time).mean()
del Jun_S4_mean['Unnamed: 0']
Jun_S4_mean['time_series']=np.arange(0,len(Jun_S4_mean),1)
Jun_S4_mean=Jun_S4_mean.rename(columns={'0':'power'})
Jun_S4_mean['power']=Jun_S4_mean['power']
Jun_S4_mean['time_series']=Jun_S4_mean['time_series']/60

Jul_S4['time']=pd.date_range(start='7/1/2018', end='8/1/2018', freq='1min', closed='left')
Jul_S4['time'] = Jul_S4['time'].astype('str') 
Jul_S4[['local_date','local_time']] = Jul_S4.time.str.split(" ",expand=True,)
Jul_S4_mean=Jul_S4.groupby(Jul_S4.local_time).mean()
del Jul_S4_mean['Unnamed: 0']
Jul_S4_mean['time_series']=np.arange(0,len(Jul_S4_mean),1)
Jul_S4_mean=Jul_S4_mean.rename(columns={'0':'power'})
Jul_S4_mean['power']=Jul_S4_mean['power']
Jul_S4_mean['time_series']=Jul_S4_mean['time_series']/60

Aug_S4['time']=pd.date_range(start='8/1/2018', end='9/1/2018', freq='1min', closed='left')
Aug_S4['time'] = Aug_S4['time'].astype('str') 
Aug_S4[['local_date','local_time']] = Aug_S4.time.str.split(" ",expand=True,)
Aug_S4_mean=Aug_S4.groupby(Aug_S4.local_time).mean()
del Aug_S4_mean['Unnamed: 0']
Aug_S4_mean['time_series']=np.arange(0,len(Aug_S4_mean),1)
Aug_S4_mean=Aug_S4_mean.rename(columns={'0':'power'})
Aug_S4_mean['power']=Aug_S4_mean['power']
Aug_S4_mean['time_series']=Aug_S4_mean['time_series']/60

Sep_S4['time']=pd.date_range(start='9/1/2018', end='10/1/2018', freq='1min', closed='left')
Sep_S4['time'] = Sep_S4['time'].astype('str') 
Sep_S4[['local_date','local_time']] = Sep_S4.time.str.split(" ",expand=True,)
Sep_S4_mean=Sep_S4.groupby(Sep_S4.local_time).mean()
del Sep_S4_mean['Unnamed: 0']
Sep_S4_mean['time_series']=np.arange(0,len(Sep_S4_mean),1)
Sep_S4_mean=Sep_S4_mean.rename(columns={'0':'power'})
Sep_S4_mean['power']=Sep_S4_mean['power']
Sep_S4_mean['time_series']=Sep_S4_mean['time_series']/60

Oct_S4['time']=pd.date_range(start='10/1/2018', end='11/1/2018', freq='1min', closed='left')
Oct_S4['time'] = Oct_S4['time'].astype('str') 
Oct_S4[['local_date','local_time']] = Oct_S4.time.str.split(" ",expand=True,)
Oct_S4_mean=Oct_S4.groupby(Oct_S4.local_time).mean()
del Oct_S4_mean['Unnamed: 0']
Oct_S4_mean['time_series']=np.arange(0,len(Oct_S4_mean),1)
Oct_S4_mean=Oct_S4_mean.rename(columns={'0':'power'})
Oct_S4_mean['power']=Oct_S4_mean['power']
Oct_S4_mean['time_series']=Oct_S4_mean['time_series']/60

Nov_S4['time']=pd.date_range(start='11/1/2018', end='12/1/2018', freq='1min', closed='left')
Nov_S4['time'] = Nov_S4['time'].astype('str') 
Nov_S4[['local_date','local_time']] = Nov_S4.time.str.split(" ",expand=True,)
Nov_S4_mean=Nov_S4.groupby(Nov_S4.local_time).mean()
del Nov_S4_mean['Unnamed: 0']
Nov_S4_mean['time_series']=np.arange(0,len(Nov_S4_mean),1)
Nov_S4_mean=Nov_S4_mean.rename(columns={'0':'power'})
Nov_S4_mean['power']=Nov_S4_mean['power']
Nov_S4_mean['time_series']=Nov_S4_mean['time_series']/60

Dec_S4['time']=pd.date_range(start='12/1/2018', end='1/1/2019', freq='1min', closed='left')
Dec_S4['time'] = Dec_S4['time'].astype('str') 
Dec_S4[['local_date','local_time']] = Dec_S4.time.str.split(" ",expand=True,)
Dec_S4_mean=Dec_S4.groupby(Dec_S4.local_time).mean()
del Dec_S4_mean['Unnamed: 0']
Dec_S4_mean['time_series']=np.arange(0,len(Dec_S4_mean),1)
Dec_S4_mean=Dec_S4_mean.rename(columns={'0':'power'})
Dec_S4_mean['power']=Dec_S4_mean['power']
Dec_S4_mean['time_series']=Dec_S4_mean['time_series']/60

#Plot demand

import matplotlib.pyplot as plt 
fig, axs = plt.subplots(3, 4)
axs[0, 0].plot(Jan['time_series'], Jan['0'],color='pink',linewidth=1)
axs[0, 0].plot(Jan_1['time_series'], Jan_1['0'],color='lightsteelblue',linewidth=1)
axs[0, 0].plot(Jan_S4_mean['time_series'], Jan_S4_mean['power'],color='blue',linewidth=1)
axs[0, 0].set_title('January')
#axs[0, 0].set_yticks([0, 5, 10, 15, 20, 25])
#axs[0, 1].plot(Feb['time_series'], Feb['0'],color='pink',linewidth=1)
axs[0, 1].plot(Feb_1['time_series'], Feb_1['0'],color='lightsteelblue',linewidth=1)
axs[0, 1].plot(Feb_S4_mean['time_series'], Feb_S4_mean['power'],color='blue',linewidth=1)
axs[0, 1].set_title('February')
#axs[0, 2].plot(Mar['time_series'], Mar['0'],color='pink',linewidth=1)
axs[0, 2].plot(Mar_1['time_series'], Mar_1['0'],color='lightsteelblue',linewidth=1)
axs[0, 2].plot(Mar_S4_mean['time_series'], Jan_S4_mean['power'],color='blue',linewidth=1)
axs[0, 2].set_title('March')
#axs[0, 3].plot(Apr['time_series'], Apr['0'],color='pink',linewidth=1)
axs[0, 3].plot(Apr_1['time_series'], Apr_1['0'],color='lightsteelblue',linewidth=1)
axs[0, 3].plot(Apr_S4_mean['time_series'], Apr_S4_mean['power'],color='blue',linewidth=1)
axs[0, 3].set_title('April')
#axs[1, 0].plot(May['time_series'], May['0'],color='pink',linewidth=1)
axs[1, 0].plot(May_1['time_series'], May_1['0'],color='lightsteelblue',linewidth=1)
axs[1, 0].plot(May_S4_mean['time_series'], May_S4_mean['power'],color='blue',linewidth=1)
axs[1, 0].set_title('May')
#axs[1, 0].set_yticks([0, 5, 10, 15, 20, 25])
#axs[1, 1].plot(Jun['time_series'], Jun['0'],color='pink',linewidth=1)
axs[1, 1].plot(Jun_1['time_series'], Jun_1['0'],color='lightsteelblue',linewidth=1)
axs[1, 1].plot(Jun_S4_mean['time_series'], Jun_S4_mean['power'],color='blue',linewidth=1)
axs[1, 1].set_title('June')
#axs[1, 2].plot(Jul['time_series'], Jul['0'],color='pink',linewidth=1)
axs[1, 2].plot(Jul_1['time_series'], Jul_1['0'],color='lightsteelblue',linewidth=1)
axs[1, 2].plot(Jul_S4_mean['time_series'], Jul_S4_mean['power'],color='blue',linewidth=1)
axs[1, 2].set_title('July')
#axs[1, 3].plot(Aug['time_series'], Aug['0'],color='pink',linewidth=1)
axs[1, 3].plot(Aug_1['time_series'], Aug_1['0'],color='lightsteelblue',linewidth=1)
axs[1, 3].plot(Aug_S4_mean['time_series'], Aug_S4_mean['power'],color='blue',linewidth=1)
axs[1, 3].set_title('August')
#axs[2, 0].plot(Sep['time_series'], Sep['0'],color='pink',linewidth=1)
axs[2, 0].plot(Sep_1['time_series'], Sep_1['0'],color='lightsteelblue',linewidth=1)
axs[2, 0].plot(Sep_S4_mean['time_series'], Sep_S4_mean['power'],color='blue',linewidth=1)
axs[2, 0].set_title('September')
#axs[2, 0].set_yticks([0, 5, 10, 15, 20, 25])
axs[2, 0].set_xticks([0, 10, 20])
#axs[2, 1].plot(Oct['time_series'], Oct['0'],color='pink',linewidth=1)
axs[2, 1].plot(Oct_1['time_series'], Oct_1['0'],color='lightsteelblue',linewidth=1)
axs[2, 1].plot(Oct_S4_mean['time_series'], Oct_S4_mean['power'],color='blue',linewidth=1)
axs[2, 1].set_title('October')
axs[2, 1].set_xticks([0, 10, 20])
#axs[2, 1].set_yticks([0, 10, 20])
#axs[2, 2].plot(Nov['time_series'], Nov['0'],color='pink',linewidth=1)
axs[2, 2].plot(Nov_1['time_series'], Nov_1['0'],color='lightsteelblue',linewidth=1)
axs[2, 2].plot(Nov_S4_mean['time_series'], Nov_S4_mean['power'],color='blue',linewidth=1)
axs[2, 2].set_title('November')
axs[2, 2].set_xticks([0, 10, 20])
#axs[2, 3].plot(Dec['time_series'], Dec['0'],color='pink',linewidth=1)
axs[2, 3].plot(Dec_1['time_series'], Dec_1['0'],color='lightsteelblue',linewidth=1)
axs[2, 3].plot(Dec_S4_mean['time_series'], Dec_S4_mean['power'],color='blue',linewidth=1)
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
fig.savefig('demand_profiles_raq_bs.png',dpi=600,bbox_inches="tight")
plt.show()


