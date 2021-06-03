#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:49:57 2020

@author: alejandrosoto
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.pyplot import figure
import pandas as pd

raq = pd.read_csv('raq_weather.csv', sep=' ', decimal='.', encoding='latin1', error_bad_lines=False)
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
#raq
for i in range (1, len(raq),1):
    jan_raq=raq.loc[raq['local_month'] == '1']
    feb_raq=raq.loc[raq['local_month'] == '2']
    mar_raq=raq.loc[raq['local_month'] == '3']
    apr_raq=raq.loc[raq['local_month'] == '4']
    may_raq=raq.loc[raq['local_month'] == '5']
    jun_raq=raq.loc[raq['local_month'] == '6']
    jul_raq=raq.loc[raq['local_month'] == '7']
    aug_raq=raq.loc[raq['local_month'] == '8']
    sep_raq=raq.loc[raq['local_month'] == '9']
    oct_raq=raq.loc[raq['local_month'] == '10']
    nov_raq=raq.loc[raq['local_month'] == '11']
    dec_raq=raq.loc[raq['local_month'] == '12']
#mar_raq
jan_raq=jan_raq.reset_index(drop=True)
feb_raq=feb_raq.reset_index(drop=True)
mar_raq=mar_raq.reset_index(drop=True)
apr_raq=apr_raq.reset_index(drop=True)
may_raq=may_raq.reset_index(drop=True)
jun_raq=jun_raq.reset_index(drop=True)
jul_raq=jul_raq.reset_index(drop=True)
aug_raq=aug_raq.reset_index(drop=True)
sep_raq=sep_raq.reset_index(drop=True)
oct_raq=oct_raq.reset_index(drop=True)
nov_raq=nov_raq.reset_index(drop=True)
dec_raq=dec_raq.reset_index(drop=True)

dec_raq=dec_raq.drop([0,1,2,3])
dec_raq=dec_raq.reset_index(drop=True)

for j in range (1, len(raq),1):
    jan_4=raq.loc[raq['local_date'] == '4/1/18']
    feb_4=raq.loc[raq['local_date'] == '4/2/18']
    mar_4=raq.loc[raq['local_date'] == '4/3/18']
    apr_4=raq.loc[raq['local_date'] == '4/4/18']
    may_4=raq.loc[raq['local_date'] == '4/5/18']
    jun_4=raq.loc[raq['local_date'] == '4/6/18']
    jul_4=raq.loc[raq['local_date'] == '4/7/18']
    aug_4=raq.loc[raq['local_date'] == '4/8/18']
    sep_4=raq.loc[raq['local_date'] == '4/9/18']
    oct_4=raq.loc[raq['local_date'] == '4/10/18']
    nov_4=raq.loc[raq['local_date'] == '4/11/18']
    dic_4=raq.loc[raq['local_date'] == '4/12/18']
jan_4['delta1'] = np.arange(len(jan_4))
jan_4.reset_index(drop=True)
feb_4['delta1'] = np.arange(len(feb_4))
feb_4.reset_index(drop=True)
mar_4['delta1'] = np.arange(len(mar_4))
mar_4.reset_index(drop=True)
apr_4['delta1'] = np.arange(len(apr_4))
apr_4.reset_index(drop=True)
may_4['delta1'] = np.arange(len(may_4))
may_4.reset_index(drop=True)
jun_4['delta1'] = np.arange(len(jun_4))
jun_4.reset_index(drop=True)
jul_4['delta1'] = np.arange(len(jul_4))
jul_4.reset_index(drop=True)
aug_4['delta1'] = np.arange(len(aug_4))
aug_4.reset_index(drop=True)
sep_4['delta1'] = np.arange(len(sep_4))
sep_4.reset_index(drop=True)
oct_4['delta1'] = np.arange(len(oct_4))
oct_4.reset_index(drop=True)
nov_4['delta1'] = np.arange(len(nov_4))
nov_4.reset_index(drop=True)
dic_4['delta1'] = np.arange(len(dic_4))
dic_4.reset_index(drop=True)

for i in range (1, len(jan_raq),1):
    jan_raq_0=jan_raq.loc[jan_raq['local_time'] == '00:00']
    jan_raq_1=jan_raq.loc[jan_raq['local_time'] == '01:00']
    jan_raq_2=jan_raq.loc[jan_raq['local_time'] == '02:00']
    jan_raq_3=jan_raq.loc[jan_raq['local_time'] == '03:00']
    jan_raq_4=jan_raq.loc[jan_raq['local_time'] == '04:00']
    jan_raq_5=jan_raq.loc[jan_raq['local_time'] == '05:00']
    jan_raq_6=jan_raq.loc[jan_raq['local_time'] == '06:00']
    jan_raq_7=jan_raq.loc[jan_raq['local_time'] == '07:00']
    jan_raq_8=jan_raq.loc[jan_raq['local_time'] == '08:00']
    jan_raq_9=jan_raq.loc[jan_raq['local_time'] == '09:00']
    jan_raq_10=jan_raq.loc[jan_raq['local_time'] == '10:00']
    jan_raq_11=jan_raq.loc[jan_raq['local_time'] == '11:00']
    jan_raq_12=jan_raq.loc[jan_raq['local_time'] == '12:00']
    jan_raq_13=jan_raq.loc[jan_raq['local_time'] == '13:00']
    jan_raq_14=jan_raq.loc[jan_raq['local_time'] == '14:00']
    jan_raq_15=jan_raq.loc[jan_raq['local_time'] == '15:00']
    jan_raq_16=jan_raq.loc[jan_raq['local_time'] == '16:00']
    jan_raq_17=jan_raq.loc[jan_raq['local_time'] == '17:00']
    jan_raq_18=jan_raq.loc[jan_raq['local_time'] == '18:00']
    jan_raq_19=jan_raq.loc[jan_raq['local_time'] == '19:00']
    jan_raq_20=jan_raq.loc[jan_raq['local_time'] == '20:00']
    jan_raq_21=jan_raq.loc[jan_raq['local_time'] == '21:00']
    jan_raq_22=jan_raq.loc[jan_raq['local_time'] == '22:00']
    jan_raq_23=jan_raq.loc[jan_raq['local_time'] == '23:00']
for i in range (1, len(feb_raq),1):
    feb_raq_0=feb_raq.loc[feb_raq['local_time'] == '00:00']
    feb_raq_1=feb_raq.loc[feb_raq['local_time'] == '01:00']
    feb_raq_2=feb_raq.loc[feb_raq['local_time'] == '02:00']
    feb_raq_3=feb_raq.loc[feb_raq['local_time'] == '03:00']
    feb_raq_4=feb_raq.loc[feb_raq['local_time'] == '04:00']
    feb_raq_5=feb_raq.loc[feb_raq['local_time'] == '05:00']
    feb_raq_6=feb_raq.loc[feb_raq['local_time'] == '06:00']
    feb_raq_7=feb_raq.loc[feb_raq['local_time'] == '07:00']
    feb_raq_8=feb_raq.loc[feb_raq['local_time'] == '08:00']
    feb_raq_9=feb_raq.loc[feb_raq['local_time'] == '09:00']
    feb_raq_10=feb_raq.loc[feb_raq['local_time'] == '10:00']
    feb_raq_11=feb_raq.loc[feb_raq['local_time'] == '11:00']
    feb_raq_12=feb_raq.loc[feb_raq['local_time'] == '12:00']
    feb_raq_13=feb_raq.loc[feb_raq['local_time'] == '13:00']
    feb_raq_14=feb_raq.loc[feb_raq['local_time'] == '14:00']
    feb_raq_15=feb_raq.loc[feb_raq['local_time'] == '15:00']
    feb_raq_16=feb_raq.loc[feb_raq['local_time'] == '16:00']
    feb_raq_17=feb_raq.loc[feb_raq['local_time'] == '17:00']
    feb_raq_18=feb_raq.loc[feb_raq['local_time'] == '18:00']
    feb_raq_19=feb_raq.loc[feb_raq['local_time'] == '19:00']
    feb_raq_20=feb_raq.loc[feb_raq['local_time'] == '20:00']
    feb_raq_21=feb_raq.loc[feb_raq['local_time'] == '21:00']
    feb_raq_22=feb_raq.loc[feb_raq['local_time'] == '22:00']
    feb_raq_23=feb_raq.loc[feb_raq['local_time'] == '23:00']
for i in range (1, len(mar_raq),1):
    mar_raq_0=mar_raq.loc[mar_raq['local_time'] == '00:00']
    mar_raq_1=mar_raq.loc[mar_raq['local_time'] == '01:00']
    mar_raq_2=mar_raq.loc[mar_raq['local_time'] == '02:00']
    mar_raq_3=mar_raq.loc[mar_raq['local_time'] == '03:00']
    mar_raq_4=mar_raq.loc[mar_raq['local_time'] == '04:00']
    mar_raq_5=mar_raq.loc[mar_raq['local_time'] == '05:00']
    mar_raq_6=mar_raq.loc[mar_raq['local_time'] == '06:00']
    mar_raq_7=mar_raq.loc[mar_raq['local_time'] == '07:00']
    mar_raq_8=mar_raq.loc[mar_raq['local_time'] == '08:00']
    mar_raq_9=mar_raq.loc[mar_raq['local_time'] == '09:00']
    mar_raq_10=mar_raq.loc[mar_raq['local_time'] == '10:00']
    mar_raq_11=mar_raq.loc[mar_raq['local_time'] == '11:00']
    mar_raq_12=mar_raq.loc[mar_raq['local_time'] == '12:00']
    mar_raq_13=mar_raq.loc[mar_raq['local_time'] == '13:00']
    mar_raq_14=mar_raq.loc[mar_raq['local_time'] == '14:00']
    mar_raq_15=mar_raq.loc[mar_raq['local_time'] == '15:00']
    mar_raq_16=mar_raq.loc[mar_raq['local_time'] == '16:00']
    mar_raq_17=mar_raq.loc[mar_raq['local_time'] == '17:00']
    mar_raq_18=mar_raq.loc[mar_raq['local_time'] == '18:00']
    mar_raq_19=mar_raq.loc[mar_raq['local_time'] == '19:00']
    mar_raq_20=mar_raq.loc[mar_raq['local_time'] == '20:00']
    mar_raq_21=mar_raq.loc[mar_raq['local_time'] == '21:00']
    mar_raq_22=mar_raq.loc[mar_raq['local_time'] == '22:00']
    mar_raq_23=mar_raq.loc[mar_raq['local_time'] == '23:00']
for i in range (1, len(apr_raq),1):
    apr_raq_0=apr_raq.loc[apr_raq['local_time'] == '00:00']
    apr_raq_1=apr_raq.loc[apr_raq['local_time'] == '01:00']
    apr_raq_2=apr_raq.loc[apr_raq['local_time'] == '02:00']
    apr_raq_3=apr_raq.loc[apr_raq['local_time'] == '03:00']
    apr_raq_4=apr_raq.loc[apr_raq['local_time'] == '04:00']
    apr_raq_5=apr_raq.loc[apr_raq['local_time'] == '05:00']
    apr_raq_6=apr_raq.loc[apr_raq['local_time'] == '06:00']
    apr_raq_7=apr_raq.loc[apr_raq['local_time'] == '07:00']
    apr_raq_8=apr_raq.loc[apr_raq['local_time'] == '08:00']
    apr_raq_9=apr_raq.loc[apr_raq['local_time'] == '09:00']
    apr_raq_10=apr_raq.loc[apr_raq['local_time'] == '10:00']
    apr_raq_11=apr_raq.loc[apr_raq['local_time'] == '11:00']
    apr_raq_12=apr_raq.loc[apr_raq['local_time'] == '12:00']
    apr_raq_13=apr_raq.loc[apr_raq['local_time'] == '13:00']
    apr_raq_14=apr_raq.loc[apr_raq['local_time'] == '14:00']
    apr_raq_15=apr_raq.loc[apr_raq['local_time'] == '15:00']
    apr_raq_16=apr_raq.loc[apr_raq['local_time'] == '16:00']
    apr_raq_17=apr_raq.loc[apr_raq['local_time'] == '17:00']
    apr_raq_18=apr_raq.loc[apr_raq['local_time'] == '18:00']
    apr_raq_19=apr_raq.loc[apr_raq['local_time'] == '19:00']
    apr_raq_20=apr_raq.loc[apr_raq['local_time'] == '20:00']
    apr_raq_21=apr_raq.loc[apr_raq['local_time'] == '21:00']
    apr_raq_22=apr_raq.loc[apr_raq['local_time'] == '22:00']
    apr_raq_23=apr_raq.loc[apr_raq['local_time'] == '23:00']
for i in range (1, len(may_raq),1):
    may_raq_0=may_raq.loc[may_raq['local_time'] == '00:00']
    may_raq_1=may_raq.loc[may_raq['local_time'] == '01:00']
    may_raq_2=may_raq.loc[may_raq['local_time'] == '02:00']
    may_raq_3=may_raq.loc[may_raq['local_time'] == '03:00']
    may_raq_4=may_raq.loc[may_raq['local_time'] == '04:00']
    may_raq_5=may_raq.loc[may_raq['local_time'] == '05:00']
    may_raq_6=may_raq.loc[may_raq['local_time'] == '06:00']
    may_raq_7=may_raq.loc[may_raq['local_time'] == '07:00']
    may_raq_8=may_raq.loc[may_raq['local_time'] == '08:00']
    may_raq_9=may_raq.loc[may_raq['local_time'] == '09:00']
    may_raq_10=may_raq.loc[may_raq['local_time'] == '10:00']
    may_raq_11=may_raq.loc[may_raq['local_time'] == '11:00']
    may_raq_12=may_raq.loc[may_raq['local_time'] == '12:00']
    may_raq_13=may_raq.loc[may_raq['local_time'] == '13:00']
    may_raq_14=may_raq.loc[may_raq['local_time'] == '14:00']
    may_raq_15=may_raq.loc[may_raq['local_time'] == '15:00']
    may_raq_16=may_raq.loc[may_raq['local_time'] == '16:00']
    may_raq_17=may_raq.loc[may_raq['local_time'] == '17:00']
    may_raq_18=may_raq.loc[may_raq['local_time'] == '18:00']
    may_raq_19=may_raq.loc[may_raq['local_time'] == '19:00']
    may_raq_20=may_raq.loc[may_raq['local_time'] == '20:00']
    may_raq_21=may_raq.loc[may_raq['local_time'] == '21:00']
    may_raq_22=may_raq.loc[may_raq['local_time'] == '22:00']
    may_raq_23=may_raq.loc[may_raq['local_time'] == '23:00']
for i in range (1, len(jun_raq),1):
    jun_raq_0=jun_raq.loc[jun_raq['local_time'] == '00:00']
    jun_raq_1=jun_raq.loc[jun_raq['local_time'] == '01:00']
    jun_raq_2=jun_raq.loc[jun_raq['local_time'] == '02:00']
    jun_raq_3=jun_raq.loc[jun_raq['local_time'] == '03:00']
    jun_raq_4=jun_raq.loc[jun_raq['local_time'] == '04:00']
    jun_raq_5=jun_raq.loc[jun_raq['local_time'] == '05:00']
    jun_raq_6=jun_raq.loc[jun_raq['local_time'] == '06:00']
    jun_raq_7=jun_raq.loc[jun_raq['local_time'] == '07:00']
    jun_raq_8=jun_raq.loc[jun_raq['local_time'] == '08:00']
    jun_raq_9=jun_raq.loc[jun_raq['local_time'] == '09:00']
    jun_raq_10=jun_raq.loc[jun_raq['local_time'] == '10:00']
    jun_raq_11=jun_raq.loc[jun_raq['local_time'] == '11:00']
    jun_raq_12=jun_raq.loc[jun_raq['local_time'] == '12:00']
    jun_raq_13=jun_raq.loc[jun_raq['local_time'] == '13:00']
    jun_raq_14=jun_raq.loc[jun_raq['local_time'] == '14:00']
    jun_raq_15=jun_raq.loc[jun_raq['local_time'] == '15:00']
    jun_raq_16=jun_raq.loc[jun_raq['local_time'] == '16:00']
    jun_raq_17=jun_raq.loc[jun_raq['local_time'] == '17:00']
    jun_raq_18=jun_raq.loc[jun_raq['local_time'] == '18:00']
    jun_raq_19=jun_raq.loc[jun_raq['local_time'] == '19:00']
    jun_raq_20=jun_raq.loc[jun_raq['local_time'] == '20:00']
    jun_raq_21=jun_raq.loc[jun_raq['local_time'] == '21:00']
    jun_raq_22=jun_raq.loc[jun_raq['local_time'] == '22:00']
    jun_raq_23=jun_raq.loc[jun_raq['local_time'] == '23:00']
for i in range (1, len(jul_raq),1):
    jul_raq_0=jul_raq.loc[jul_raq['local_time'] == '00:00']
    jul_raq_1=jul_raq.loc[jul_raq['local_time'] == '01:00']
    jul_raq_2=jul_raq.loc[jul_raq['local_time'] == '02:00']
    jul_raq_3=jul_raq.loc[jul_raq['local_time'] == '03:00']
    jul_raq_4=jul_raq.loc[jul_raq['local_time'] == '04:00']
    jul_raq_5=jul_raq.loc[jul_raq['local_time'] == '05:00']
    jul_raq_6=jul_raq.loc[jul_raq['local_time'] == '06:00']
    jul_raq_7=jul_raq.loc[jul_raq['local_time'] == '07:00']
    jul_raq_8=jul_raq.loc[jul_raq['local_time'] == '08:00']
    jul_raq_9=jul_raq.loc[jul_raq['local_time'] == '09:00']
    jul_raq_10=jul_raq.loc[jul_raq['local_time'] == '10:00']
    jul_raq_11=jul_raq.loc[jul_raq['local_time'] == '11:00']
    jul_raq_12=jul_raq.loc[jul_raq['local_time'] == '12:00']
    jul_raq_13=jul_raq.loc[jul_raq['local_time'] == '13:00']
    jul_raq_14=jul_raq.loc[jul_raq['local_time'] == '14:00']
    jul_raq_15=jul_raq.loc[jul_raq['local_time'] == '15:00']
    jul_raq_16=jul_raq.loc[jul_raq['local_time'] == '16:00']
    jul_raq_17=jul_raq.loc[jul_raq['local_time'] == '17:00']
    jul_raq_18=jul_raq.loc[jul_raq['local_time'] == '18:00']
    jul_raq_19=jul_raq.loc[jul_raq['local_time'] == '19:00']
    jul_raq_20=jul_raq.loc[jul_raq['local_time'] == '20:00']
    jul_raq_21=jul_raq.loc[jul_raq['local_time'] == '21:00']
    jul_raq_22=jul_raq.loc[jul_raq['local_time'] == '22:00']
    jul_raq_23=jul_raq.loc[jul_raq['local_time'] == '23:00']
for i in range (1, len(aug_raq),1):
    aug_raq_0=aug_raq.loc[aug_raq['local_time'] == '00:00']
    aug_raq_1=aug_raq.loc[aug_raq['local_time'] == '01:00']
    aug_raq_2=aug_raq.loc[aug_raq['local_time'] == '02:00']
    aug_raq_3=aug_raq.loc[aug_raq['local_time'] == '03:00']
    aug_raq_4=aug_raq.loc[aug_raq['local_time'] == '04:00']
    aug_raq_5=aug_raq.loc[aug_raq['local_time'] == '05:00']
    aug_raq_6=aug_raq.loc[aug_raq['local_time'] == '06:00']
    aug_raq_7=aug_raq.loc[aug_raq['local_time'] == '07:00']
    aug_raq_8=aug_raq.loc[aug_raq['local_time'] == '08:00']
    aug_raq_9=aug_raq.loc[aug_raq['local_time'] == '09:00']
    aug_raq_10=aug_raq.loc[aug_raq['local_time'] == '10:00']
    aug_raq_11=aug_raq.loc[aug_raq['local_time'] == '11:00']
    aug_raq_12=aug_raq.loc[aug_raq['local_time'] == '12:00']
    aug_raq_13=aug_raq.loc[aug_raq['local_time'] == '13:00']
    aug_raq_14=aug_raq.loc[aug_raq['local_time'] == '14:00']
    aug_raq_15=aug_raq.loc[aug_raq['local_time'] == '15:00']
    aug_raq_16=aug_raq.loc[aug_raq['local_time'] == '16:00']
    aug_raq_17=aug_raq.loc[aug_raq['local_time'] == '17:00']
    aug_raq_18=aug_raq.loc[aug_raq['local_time'] == '18:00']
    aug_raq_19=aug_raq.loc[aug_raq['local_time'] == '19:00']
    aug_raq_20=aug_raq.loc[aug_raq['local_time'] == '20:00']
    aug_raq_21=aug_raq.loc[aug_raq['local_time'] == '21:00']
    aug_raq_22=aug_raq.loc[aug_raq['local_time'] == '22:00']
    aug_raq_23=aug_raq.loc[aug_raq['local_time'] == '23:00']
for i in range (1, len(sep_raq),1):
    sep_raq_0=sep_raq.loc[sep_raq['local_time'] == '00:00']
    sep_raq_1=sep_raq.loc[sep_raq['local_time'] == '01:00']
    sep_raq_2=sep_raq.loc[sep_raq['local_time'] == '02:00']
    sep_raq_3=sep_raq.loc[sep_raq['local_time'] == '03:00']
    sep_raq_4=sep_raq.loc[sep_raq['local_time'] == '04:00']
    sep_raq_5=sep_raq.loc[sep_raq['local_time'] == '05:00']
    sep_raq_6=sep_raq.loc[sep_raq['local_time'] == '06:00']
    sep_raq_7=sep_raq.loc[sep_raq['local_time'] == '07:00']
    sep_raq_8=sep_raq.loc[sep_raq['local_time'] == '08:00']
    sep_raq_9=sep_raq.loc[sep_raq['local_time'] == '09:00']
    sep_raq_10=sep_raq.loc[sep_raq['local_time'] == '10:00']
    sep_raq_11=sep_raq.loc[sep_raq['local_time'] == '11:00']
    sep_raq_12=sep_raq.loc[sep_raq['local_time'] == '12:00']
    sep_raq_13=sep_raq.loc[sep_raq['local_time'] == '13:00']
    sep_raq_14=sep_raq.loc[sep_raq['local_time'] == '14:00']
    sep_raq_15=sep_raq.loc[sep_raq['local_time'] == '15:00']
    sep_raq_16=sep_raq.loc[sep_raq['local_time'] == '16:00']
    sep_raq_17=sep_raq.loc[sep_raq['local_time'] == '17:00']
    sep_raq_18=sep_raq.loc[sep_raq['local_time'] == '18:00']
    sep_raq_19=sep_raq.loc[sep_raq['local_time'] == '19:00']
    sep_raq_20=sep_raq.loc[sep_raq['local_time'] == '20:00']
    sep_raq_21=sep_raq.loc[sep_raq['local_time'] == '21:00']
    sep_raq_22=sep_raq.loc[sep_raq['local_time'] == '22:00']
    sep_raq_23=sep_raq.loc[sep_raq['local_time'] == '23:00']
for i in range (1, len(oct_raq),1):
    oct_raq_0=oct_raq.loc[oct_raq['local_time'] == '00:00']
    oct_raq_1=oct_raq.loc[oct_raq['local_time'] == '01:00']
    oct_raq_2=oct_raq.loc[oct_raq['local_time'] == '02:00']
    oct_raq_3=oct_raq.loc[oct_raq['local_time'] == '03:00']
    oct_raq_4=oct_raq.loc[oct_raq['local_time'] == '04:00']
    oct_raq_5=oct_raq.loc[oct_raq['local_time'] == '05:00']
    oct_raq_6=oct_raq.loc[oct_raq['local_time'] == '06:00']
    oct_raq_7=oct_raq.loc[oct_raq['local_time'] == '07:00']
    oct_raq_8=oct_raq.loc[oct_raq['local_time'] == '08:00']
    oct_raq_9=oct_raq.loc[oct_raq['local_time'] == '09:00']
    oct_raq_10=oct_raq.loc[oct_raq['local_time'] == '10:00']
    oct_raq_11=oct_raq.loc[oct_raq['local_time'] == '11:00']
    oct_raq_12=oct_raq.loc[oct_raq['local_time'] == '12:00']
    oct_raq_13=oct_raq.loc[oct_raq['local_time'] == '13:00']
    oct_raq_14=oct_raq.loc[oct_raq['local_time'] == '14:00']
    oct_raq_15=oct_raq.loc[oct_raq['local_time'] == '15:00']
    oct_raq_16=oct_raq.loc[oct_raq['local_time'] == '16:00']
    oct_raq_17=oct_raq.loc[oct_raq['local_time'] == '17:00']
    oct_raq_18=oct_raq.loc[oct_raq['local_time'] == '18:00']
    oct_raq_19=oct_raq.loc[oct_raq['local_time'] == '19:00']
    oct_raq_20=oct_raq.loc[oct_raq['local_time'] == '20:00']
    oct_raq_21=oct_raq.loc[oct_raq['local_time'] == '21:00']
    oct_raq_22=oct_raq.loc[oct_raq['local_time'] == '22:00']
    oct_raq_23=oct_raq.loc[oct_raq['local_time'] == '23:00']
for i in range (1, len(nov_raq),1):
    nov_raq_0=nov_raq.loc[nov_raq['local_time'] == '00:00']
    nov_raq_1=nov_raq.loc[nov_raq['local_time'] == '01:00']
    nov_raq_2=nov_raq.loc[nov_raq['local_time'] == '02:00']
    nov_raq_3=nov_raq.loc[nov_raq['local_time'] == '03:00']
    nov_raq_4=nov_raq.loc[nov_raq['local_time'] == '04:00']
    nov_raq_5=nov_raq.loc[nov_raq['local_time'] == '05:00']
    nov_raq_6=nov_raq.loc[nov_raq['local_time'] == '06:00']
    nov_raq_7=nov_raq.loc[nov_raq['local_time'] == '07:00']
    nov_raq_8=nov_raq.loc[nov_raq['local_time'] == '08:00']
    nov_raq_9=nov_raq.loc[nov_raq['local_time'] == '09:00']
    nov_raq_10=nov_raq.loc[nov_raq['local_time'] == '10:00']
    nov_raq_11=nov_raq.loc[nov_raq['local_time'] == '11:00']
    nov_raq_12=nov_raq.loc[nov_raq['local_time'] == '12:00']
    nov_raq_13=nov_raq.loc[nov_raq['local_time'] == '13:00']
    nov_raq_14=nov_raq.loc[nov_raq['local_time'] == '14:00']
    nov_raq_15=nov_raq.loc[nov_raq['local_time'] == '15:00']
    nov_raq_16=nov_raq.loc[nov_raq['local_time'] == '16:00']
    nov_raq_17=nov_raq.loc[nov_raq['local_time'] == '17:00']
    nov_raq_18=nov_raq.loc[nov_raq['local_time'] == '18:00']
    nov_raq_19=nov_raq.loc[nov_raq['local_time'] == '19:00']
    nov_raq_20=nov_raq.loc[nov_raq['local_time'] == '20:00']
    nov_raq_21=nov_raq.loc[nov_raq['local_time'] == '21:00']
    nov_raq_22=nov_raq.loc[nov_raq['local_time'] == '22:00']
    nov_raq_23=nov_raq.loc[nov_raq['local_time'] == '23:00']
for i in range (1, len(dec_raq),1):
    dec_raq_0=dec_raq.loc[dec_raq['local_time'] == '00:00']
    dec_raq_1=dec_raq.loc[dec_raq['local_time'] == '01:00']
    dec_raq_2=dec_raq.loc[dec_raq['local_time'] == '02:00']
    dec_raq_3=dec_raq.loc[dec_raq['local_time'] == '03:00']
    dec_raq_4=dec_raq.loc[dec_raq['local_time'] == '04:00']
    dec_raq_5=dec_raq.loc[dec_raq['local_time'] == '05:00']
    dec_raq_6=dec_raq.loc[dec_raq['local_time'] == '06:00']
    dec_raq_7=dec_raq.loc[dec_raq['local_time'] == '07:00']
    dec_raq_8=dec_raq.loc[dec_raq['local_time'] == '08:00']
    dec_raq_9=dec_raq.loc[dec_raq['local_time'] == '09:00']
    dec_raq_10=dec_raq.loc[dec_raq['local_time'] == '10:00']
    dec_raq_11=dec_raq.loc[dec_raq['local_time'] == '11:00']
    dec_raq_12=dec_raq.loc[dec_raq['local_time'] == '12:00']
    dec_raq_13=dec_raq.loc[dec_raq['local_time'] == '13:00']
    dec_raq_14=dec_raq.loc[dec_raq['local_time'] == '14:00']
    dec_raq_15=dec_raq.loc[dec_raq['local_time'] == '15:00']
    dec_raq_16=dec_raq.loc[dec_raq['local_time'] == '16:00']
    dec_raq_17=dec_raq.loc[dec_raq['local_time'] == '17:00']
    dec_raq_18=dec_raq.loc[dec_raq['local_time'] == '18:00']
    dec_raq_19=dec_raq.loc[dec_raq['local_time'] == '19:00']
    dec_raq_20=dec_raq.loc[dec_raq['local_time'] == '20:00']
    dec_raq_21=dec_raq.loc[dec_raq['local_time'] == '21:00']
    dec_raq_22=dec_raq.loc[dec_raq['local_time'] == '22:00']
    dec_raq_23=dec_raq.loc[dec_raq['local_time'] == '23:00']
    
jan_a={'t':pd.Series([jan_raq_0['t'].mean(),
jan_raq_1['t'].mean(),
jan_raq_2['t'].mean(),
jan_raq_3['t'].mean(),
jan_raq_4['t'].mean(),
jan_raq_5['t'].mean(),
jan_raq_6['t'].mean(),
jan_raq_7['t'].mean(),
jan_raq_8['t'].mean(),
jan_raq_9['t'].mean(),
jan_raq_10['t'].mean(),
jan_raq_11['t'].mean(),
jan_raq_12['t'].mean(),
jan_raq_13['t'].mean(),
jan_raq_14['t'].mean(),
jan_raq_15['t'].mean(),
jan_raq_16['t'].mean(),
jan_raq_17['t'].mean(),
jan_raq_18['t'].mean(),
jan_raq_19['t'].mean(),
jan_raq_20['t'].mean(),
jan_raq_21['t'].mean(),
jan_raq_22['t'].mean(),
jan_raq_23['t'].mean()])}
jan_av=pd.DataFrame(jan_a)
jan_av['delta1'] = np.arange(len(jan_av))
feb_a={'t':pd.Series([feb_raq_0['t'].mean(),
feb_raq_1['t'].mean(),
feb_raq_2['t'].mean(),
feb_raq_3['t'].mean(),
feb_raq_4['t'].mean(),
feb_raq_5['t'].mean(),
feb_raq_6['t'].mean(),
feb_raq_7['t'].mean(),
feb_raq_8['t'].mean(),
feb_raq_9['t'].mean(),
feb_raq_10['t'].mean(),
feb_raq_11['t'].mean(),
feb_raq_12['t'].mean(),
feb_raq_13['t'].mean(),
feb_raq_14['t'].mean(),
feb_raq_15['t'].mean(),
feb_raq_16['t'].mean(),
feb_raq_17['t'].mean(),
feb_raq_18['t'].mean(),
feb_raq_19['t'].mean(),
feb_raq_20['t'].mean(),
feb_raq_21['t'].mean(),
feb_raq_22['t'].mean(),
feb_raq_23['t'].mean()])}
feb_av=pd.DataFrame(feb_a)
feb_av['delta1'] = np.arange(len(feb_av))
mar_a={'t':pd.Series([mar_raq_0['t'].mean(),
mar_raq_1['t'].mean(),
mar_raq_2['t'].mean(),
mar_raq_3['t'].mean(),
mar_raq_4['t'].mean(),
mar_raq_5['t'].mean(),
mar_raq_6['t'].mean(),
mar_raq_7['t'].mean(),
mar_raq_8['t'].mean(),
mar_raq_9['t'].mean(),
mar_raq_10['t'].mean(),
mar_raq_11['t'].mean(),
mar_raq_12['t'].mean(),
mar_raq_13['t'].mean(),
mar_raq_14['t'].mean(),
mar_raq_15['t'].mean(),
mar_raq_16['t'].mean(),
mar_raq_17['t'].mean(),
mar_raq_18['t'].mean(),
mar_raq_19['t'].mean(),
mar_raq_20['t'].mean(),
mar_raq_21['t'].mean(),
mar_raq_22['t'].mean(),
mar_raq_23['t'].mean()])}
mar_av=pd.DataFrame(mar_a)
mar_av['delta1'] = np.arange(len(mar_av))
apr_a={'t':pd.Series([apr_raq_0['t'].mean(),
apr_raq_1['t'].mean(),
apr_raq_2['t'].mean(),
apr_raq_3['t'].mean(),
apr_raq_4['t'].mean(),
apr_raq_5['t'].mean(),
apr_raq_6['t'].mean(),
apr_raq_7['t'].mean(),
apr_raq_8['t'].mean(),
apr_raq_9['t'].mean(),
apr_raq_10['t'].mean(),
apr_raq_11['t'].mean(),
apr_raq_12['t'].mean(),
apr_raq_13['t'].mean(),
apr_raq_14['t'].mean(),
apr_raq_15['t'].mean(),
apr_raq_16['t'].mean(),
apr_raq_17['t'].mean(),
apr_raq_18['t'].mean(),
apr_raq_19['t'].mean(),
apr_raq_20['t'].mean(),
apr_raq_21['t'].mean(),
apr_raq_22['t'].mean(),
apr_raq_23['t'].mean()])}
apr_av=pd.DataFrame(apr_a)
apr_av['delta1'] = np.arange(len(apr_av))
may_a={'t':pd.Series([may_raq_0['t'].mean(),
may_raq_1['t'].mean(),
may_raq_2['t'].mean(),
may_raq_3['t'].mean(),
may_raq_4['t'].mean(),
may_raq_5['t'].mean(),
may_raq_6['t'].mean(),
may_raq_7['t'].mean(),
may_raq_8['t'].mean(),
may_raq_9['t'].mean(),
may_raq_10['t'].mean(),
may_raq_11['t'].mean(),
may_raq_12['t'].mean(),
may_raq_13['t'].mean(),
may_raq_14['t'].mean(),
may_raq_15['t'].mean(),
may_raq_16['t'].mean(),
may_raq_17['t'].mean(),
may_raq_18['t'].mean(),
may_raq_19['t'].mean(),
may_raq_20['t'].mean(),
may_raq_21['t'].mean(),
may_raq_22['t'].mean(),
may_raq_23['t'].mean()])}
may_av=pd.DataFrame(may_a)
may_av['delta1'] = np.arange(len(may_av))
jun_a={'t':pd.Series([jun_raq_0['t'].mean(),
jun_raq_1['t'].mean(),
jun_raq_2['t'].mean(),
jun_raq_3['t'].mean(),
jun_raq_4['t'].mean(),
jun_raq_5['t'].mean(),
jun_raq_6['t'].mean(),
jun_raq_7['t'].mean(),
jun_raq_8['t'].mean(),
jun_raq_9['t'].mean(),
jun_raq_10['t'].mean(),
jun_raq_11['t'].mean(),
jun_raq_12['t'].mean(),
jun_raq_13['t'].mean(),
jun_raq_14['t'].mean(),
jun_raq_15['t'].mean(),
jun_raq_16['t'].mean(),
jun_raq_17['t'].mean(),
jun_raq_18['t'].mean(),
jun_raq_19['t'].mean(),
jun_raq_20['t'].mean(),
jun_raq_21['t'].mean(),
jun_raq_22['t'].mean(),
jun_raq_23['t'].mean()])}
jun_av=pd.DataFrame(jun_a)
jun_av['delta1'] = np.arange(len(jun_av))
jul_a={'t':pd.Series([jul_raq_0['t'].mean(),
jul_raq_1['t'].mean(),
jul_raq_2['t'].mean(),
jul_raq_3['t'].mean(),
jul_raq_4['t'].mean(),
jul_raq_5['t'].mean(),
jul_raq_6['t'].mean(),
jul_raq_7['t'].mean(),
jul_raq_8['t'].mean(),
jul_raq_9['t'].mean(),
jul_raq_10['t'].mean(),
jul_raq_11['t'].mean(),
jul_raq_12['t'].mean(),
jul_raq_13['t'].mean(),
jul_raq_14['t'].mean(),
jul_raq_15['t'].mean(),
jul_raq_16['t'].mean(),
jul_raq_17['t'].mean(),
jul_raq_18['t'].mean(),
jul_raq_19['t'].mean(),
jul_raq_20['t'].mean(),
jul_raq_21['t'].mean(),
jul_raq_22['t'].mean(),
jul_raq_23['t'].mean()])}
jul_av=pd.DataFrame(jul_a)
jul_av['delta1'] = np.arange(len(jul_av))
aug_a={'t':pd.Series([aug_raq_0['t'].mean(),
aug_raq_1['t'].mean(),
aug_raq_2['t'].mean(),
aug_raq_3['t'].mean(),
aug_raq_4['t'].mean(),
aug_raq_5['t'].mean(),
aug_raq_6['t'].mean(),
aug_raq_7['t'].mean(),
aug_raq_8['t'].mean(),
aug_raq_9['t'].mean(),
aug_raq_10['t'].mean(),
aug_raq_11['t'].mean(),
aug_raq_12['t'].mean(),
aug_raq_13['t'].mean(),
aug_raq_14['t'].mean(),
aug_raq_15['t'].mean(),
aug_raq_16['t'].mean(),
aug_raq_17['t'].mean(),
aug_raq_18['t'].mean(),
aug_raq_19['t'].mean(),
aug_raq_20['t'].mean(),
aug_raq_21['t'].mean(),
aug_raq_22['t'].mean(),
aug_raq_23['t'].mean()])}
aug_av=pd.DataFrame(aug_a)
aug_av['delta1'] = np.arange(len(aug_av))
sep_a={'t':pd.Series([sep_raq_0['t'].mean(),
sep_raq_1['t'].mean(),
sep_raq_2['t'].mean(),
sep_raq_3['t'].mean(),
sep_raq_4['t'].mean(),
sep_raq_5['t'].mean(),
sep_raq_6['t'].mean(),
sep_raq_7['t'].mean(),
sep_raq_8['t'].mean(),
sep_raq_9['t'].mean(),
sep_raq_10['t'].mean(),
sep_raq_11['t'].mean(),
sep_raq_12['t'].mean(),
sep_raq_13['t'].mean(),
sep_raq_14['t'].mean(),
sep_raq_15['t'].mean(),
sep_raq_16['t'].mean(),
sep_raq_17['t'].mean(),
sep_raq_18['t'].mean(),
sep_raq_19['t'].mean(),
sep_raq_20['t'].mean(),
sep_raq_21['t'].mean(),
sep_raq_22['t'].mean(),
sep_raq_23['t'].mean()])}
sep_av=pd.DataFrame(sep_a)
sep_av['delta1'] = np.arange(len(sep_av))
oct_a={'t':pd.Series([oct_raq_0['t'].mean(),
oct_raq_1['t'].mean(),
oct_raq_2['t'].mean(),
oct_raq_3['t'].mean(),
oct_raq_4['t'].mean(),
oct_raq_5['t'].mean(),
oct_raq_6['t'].mean(),
oct_raq_7['t'].mean(),
oct_raq_8['t'].mean(),
oct_raq_9['t'].mean(),
oct_raq_10['t'].mean(),
oct_raq_11['t'].mean(),
oct_raq_12['t'].mean(),
oct_raq_13['t'].mean(),
oct_raq_14['t'].mean(),
oct_raq_15['t'].mean(),
oct_raq_16['t'].mean(),
oct_raq_17['t'].mean(),
oct_raq_18['t'].mean(),
oct_raq_19['t'].mean(),
oct_raq_20['t'].mean(),
oct_raq_21['t'].mean(),
oct_raq_22['t'].mean(),
oct_raq_23['t'].mean()])}
oct_av=pd.DataFrame(oct_a)
oct_av['delta1'] = np.arange(len(oct_av))
nov_a={'t':pd.Series([nov_raq_0['t'].mean(),
nov_raq_1['t'].mean(),
nov_raq_2['t'].mean(),
nov_raq_3['t'].mean(),
nov_raq_4['t'].mean(),
nov_raq_5['t'].mean(),
nov_raq_6['t'].mean(),
nov_raq_7['t'].mean(),
nov_raq_8['t'].mean(),
nov_raq_9['t'].mean(),
nov_raq_10['t'].mean(),
nov_raq_11['t'].mean(),
nov_raq_12['t'].mean(),
nov_raq_13['t'].mean(),
nov_raq_14['t'].mean(),
nov_raq_15['t'].mean(),
nov_raq_16['t'].mean(),
nov_raq_17['t'].mean(),
nov_raq_18['t'].mean(),
nov_raq_19['t'].mean(),
nov_raq_20['t'].mean(),
nov_raq_21['t'].mean(),
nov_raq_22['t'].mean(),
nov_raq_23['t'].mean()])}
nov_av=pd.DataFrame(nov_a)
nov_av['delta1'] = np.arange(len(nov_av))
dec_a={'t':pd.Series([dec_raq_0['t'].mean(),
dec_raq_1['t'].mean(),
dec_raq_2['t'].mean(),
dec_raq_3['t'].mean(),
dec_raq_4['t'].mean(),
dec_raq_5['t'].mean(),
dec_raq_6['t'].mean(),
dec_raq_7['t'].mean(),
dec_raq_8['t'].mean(),
dec_raq_9['t'].mean(),
dec_raq_10['t'].mean(),
dec_raq_11['t'].mean(),
dec_raq_12['t'].mean(),
dec_raq_13['t'].mean(),
dec_raq_14['t'].mean(),
dec_raq_15['t'].mean(),
dec_raq_16['t'].mean(),
dec_raq_17['t'].mean(),
dec_raq_18['t'].mean(),
dec_raq_19['t'].mean(),
dec_raq_20['t'].mean(),
dec_raq_21['t'].mean(),
dec_raq_22['t'].mean(),
dec_raq_23['t'].mean()])}
dec_av=pd.DataFrame(dec_a)
dec_av['delta1'] = np.arange(len(dec_av))

jan_a={'t':pd.Series([jan_raq_0['t'].mean(),
jan_raq_1['t'].mean(),
jan_raq_2['t'].mean(),
jan_raq_3['t'].mean(),
jan_raq_4['t'].mean(),
jan_raq_5['t'].mean(),
jan_raq_6['t'].mean(),
jan_raq_7['t'].mean(),
jan_raq_8['t'].mean(),
jan_raq_9['t'].mean(),
jan_raq_10['t'].mean(),
jan_raq_11['t'].mean(),
jan_raq_12['t'].mean(),
jan_raq_13['t'].mean(),
jan_raq_14['t'].mean(),
jan_raq_15['t'].mean(),
jan_raq_16['t'].mean(),
jan_raq_17['t'].mean(),
jan_raq_18['t'].mean(),
jan_raq_19['t'].mean(),
jan_raq_20['t'].mean(),
jan_raq_21['t'].mean(),
jan_raq_22['t'].mean(),
jan_raq_23['t'].mean()])}
jan_av=pd.DataFrame(jan_a)
jan_av['delta1'] = np.arange(len(jan_av))
feb_a={'t':pd.Series([feb_raq_0['t'].mean(),
feb_raq_1['t'].mean(),
feb_raq_2['t'].mean(),
feb_raq_3['t'].mean(),
feb_raq_4['t'].mean(),
feb_raq_5['t'].mean(),
feb_raq_6['t'].mean(),
feb_raq_7['t'].mean(),
feb_raq_8['t'].mean(),
feb_raq_9['t'].mean(),
feb_raq_10['t'].mean(),
feb_raq_11['t'].mean(),
feb_raq_12['t'].mean(),
feb_raq_13['t'].mean(),
feb_raq_14['t'].mean(),
feb_raq_15['t'].mean(),
feb_raq_16['t'].mean(),
feb_raq_17['t'].mean(),
feb_raq_18['t'].mean(),
feb_raq_19['t'].mean(),
feb_raq_20['t'].mean(),
feb_raq_21['t'].mean(),
feb_raq_22['t'].mean(),
feb_raq_23['t'].mean()])}
feb_av=pd.DataFrame(feb_a)
feb_av['delta1'] = np.arange(len(feb_av))
mar_a={'t':pd.Series([mar_raq_0['t'].mean(),
mar_raq_1['t'].mean(),
mar_raq_2['t'].mean(),
mar_raq_3['t'].mean(),
mar_raq_4['t'].mean(),
mar_raq_5['t'].mean(),
mar_raq_6['t'].mean(),
mar_raq_7['t'].mean(),
mar_raq_8['t'].mean(),
mar_raq_9['t'].mean(),
mar_raq_10['t'].mean(),
mar_raq_11['t'].mean(),
mar_raq_12['t'].mean(),
mar_raq_13['t'].mean(),
mar_raq_14['t'].mean(),
mar_raq_15['t'].mean(),
mar_raq_16['t'].mean(),
mar_raq_17['t'].mean(),
mar_raq_18['t'].mean(),
mar_raq_19['t'].mean(),
mar_raq_20['t'].mean(),
mar_raq_21['t'].mean(),
mar_raq_22['t'].mean(),
mar_raq_23['t'].mean()])}
mar_av=pd.DataFrame(mar_a)
mar_av['delta1'] = np.arange(len(mar_av))
apr_a={'t':pd.Series([apr_raq_0['t'].mean(),
apr_raq_1['t'].mean(),
apr_raq_2['t'].mean(),
apr_raq_3['t'].mean(),
apr_raq_4['t'].mean(),
apr_raq_5['t'].mean(),
apr_raq_6['t'].mean(),
apr_raq_7['t'].mean(),
apr_raq_8['t'].mean(),
apr_raq_9['t'].mean(),
apr_raq_10['t'].mean(),
apr_raq_11['t'].mean(),
apr_raq_12['t'].mean(),
apr_raq_13['t'].mean(),
apr_raq_14['t'].mean(),
apr_raq_15['t'].mean(),
apr_raq_16['t'].mean(),
apr_raq_17['t'].mean(),
apr_raq_18['t'].mean(),
apr_raq_19['t'].mean(),
apr_raq_20['t'].mean(),
apr_raq_21['t'].mean(),
apr_raq_22['t'].mean(),
apr_raq_23['t'].mean()])}
apr_av=pd.DataFrame(apr_a)
apr_av['delta1'] = np.arange(len(apr_av))
may_a={'t':pd.Series([may_raq_0['t'].mean(),
may_raq_1['t'].mean(),
may_raq_2['t'].mean(),
may_raq_3['t'].mean(),
may_raq_4['t'].mean(),
may_raq_5['t'].mean(),
may_raq_6['t'].mean(),
may_raq_7['t'].mean(),
may_raq_8['t'].mean(),
may_raq_9['t'].mean(),
may_raq_10['t'].mean(),
may_raq_11['t'].mean(),
may_raq_12['t'].mean(),
may_raq_13['t'].mean(),
may_raq_14['t'].mean(),
may_raq_15['t'].mean(),
may_raq_16['t'].mean(),
may_raq_17['t'].mean(),
may_raq_18['t'].mean(),
may_raq_19['t'].mean(),
may_raq_20['t'].mean(),
may_raq_21['t'].mean(),
may_raq_22['t'].mean(),
may_raq_23['t'].mean()])}
may_av=pd.DataFrame(may_a)
may_av['delta1'] = np.arange(len(may_av))
jun_a={'t':pd.Series([jun_raq_0['t'].mean(),
jun_raq_1['t'].mean(),
jun_raq_2['t'].mean(),
jun_raq_3['t'].mean(),
jun_raq_4['t'].mean(),
jun_raq_5['t'].mean(),
jun_raq_6['t'].mean(),
jun_raq_7['t'].mean(),
jun_raq_8['t'].mean(),
jun_raq_9['t'].mean(),
jun_raq_10['t'].mean(),
jun_raq_11['t'].mean(),
jun_raq_12['t'].mean(),
jun_raq_13['t'].mean(),
jun_raq_14['t'].mean(),
jun_raq_15['t'].mean(),
jun_raq_16['t'].mean(),
jun_raq_17['t'].mean(),
jun_raq_18['t'].mean(),
jun_raq_19['t'].mean(),
jun_raq_20['t'].mean(),
jun_raq_21['t'].mean(),
jun_raq_22['t'].mean(),
jun_raq_23['t'].mean()])}
jun_av=pd.DataFrame(jun_a)
jun_av['delta1'] = np.arange(len(jun_av))
jul_a={'t':pd.Series([jul_raq_0['t'].mean(),
jul_raq_1['t'].mean(),
jul_raq_2['t'].mean(),
jul_raq_3['t'].mean(),
jul_raq_4['t'].mean(),
jul_raq_5['t'].mean(),
jul_raq_6['t'].mean(),
jul_raq_7['t'].mean(),
jul_raq_8['t'].mean(),
jul_raq_9['t'].mean(),
jul_raq_10['t'].mean(),
jul_raq_11['t'].mean(),
jul_raq_12['t'].mean(),
jul_raq_13['t'].mean(),
jul_raq_14['t'].mean(),
jul_raq_15['t'].mean(),
jul_raq_16['t'].mean(),
jul_raq_17['t'].mean(),
jul_raq_18['t'].mean(),
jul_raq_19['t'].mean(),
jul_raq_20['t'].mean(),
jul_raq_21['t'].mean(),
jul_raq_22['t'].mean(),
jul_raq_23['t'].mean()])}
jul_av=pd.DataFrame(jul_a)
jul_av['delta1'] = np.arange(len(jul_av))
aug_a={'t':pd.Series([aug_raq_0['t'].mean(),
aug_raq_1['t'].mean(),
aug_raq_2['t'].mean(),
aug_raq_3['t'].mean(),
aug_raq_4['t'].mean(),
aug_raq_5['t'].mean(),
aug_raq_6['t'].mean(),
aug_raq_7['t'].mean(),
aug_raq_8['t'].mean(),
aug_raq_9['t'].mean(),
aug_raq_10['t'].mean(),
aug_raq_11['t'].mean(),
aug_raq_12['t'].mean(),
aug_raq_13['t'].mean(),
aug_raq_14['t'].mean(),
aug_raq_15['t'].mean(),
aug_raq_16['t'].mean(),
aug_raq_17['t'].mean(),
aug_raq_18['t'].mean(),
aug_raq_19['t'].mean(),
aug_raq_20['t'].mean(),
aug_raq_21['t'].mean(),
aug_raq_22['t'].mean(),
aug_raq_23['t'].mean()])}
aug_av=pd.DataFrame(aug_a)
aug_av['delta1'] = np.arange(len(aug_av))
sep_a={'t':pd.Series([sep_raq_0['t'].mean(),
sep_raq_1['t'].mean(),
sep_raq_2['t'].mean(),
sep_raq_3['t'].mean(),
sep_raq_4['t'].mean(),
sep_raq_5['t'].mean(),
sep_raq_6['t'].mean(),
sep_raq_7['t'].mean(),
sep_raq_8['t'].mean(),
sep_raq_9['t'].mean(),
sep_raq_10['t'].mean(),
sep_raq_11['t'].mean(),
sep_raq_12['t'].mean(),
sep_raq_13['t'].mean(),
sep_raq_14['t'].mean(),
sep_raq_15['t'].mean(),
sep_raq_16['t'].mean(),
sep_raq_17['t'].mean(),
sep_raq_18['t'].mean(),
sep_raq_19['t'].mean(),
sep_raq_20['t'].mean(),
sep_raq_21['t'].mean(),
sep_raq_22['t'].mean(),
sep_raq_23['t'].mean()])}
sep_av=pd.DataFrame(sep_a)
sep_av['delta1'] = np.arange(len(sep_av))
oct_a={'t':pd.Series([oct_raq_0['t'].mean(),
oct_raq_1['t'].mean(),
oct_raq_2['t'].mean(),
oct_raq_3['t'].mean(),
oct_raq_4['t'].mean(),
oct_raq_5['t'].mean(),
oct_raq_6['t'].mean(),
oct_raq_7['t'].mean(),
oct_raq_8['t'].mean(),
oct_raq_9['t'].mean(),
oct_raq_10['t'].mean(),
oct_raq_11['t'].mean(),
oct_raq_12['t'].mean(),
oct_raq_13['t'].mean(),
oct_raq_14['t'].mean(),
oct_raq_15['t'].mean(),
oct_raq_16['t'].mean(),
oct_raq_17['t'].mean(),
oct_raq_18['t'].mean(),
oct_raq_19['t'].mean(),
oct_raq_20['t'].mean(),
oct_raq_21['t'].mean(),
oct_raq_22['t'].mean(),
oct_raq_23['t'].mean()])}
oct_av=pd.DataFrame(oct_a)
oct_av['delta1'] = np.arange(len(oct_av))
nov_a={'t':pd.Series([nov_raq_0['t'].mean(),
nov_raq_1['t'].mean(),
nov_raq_2['t'].mean(),
nov_raq_3['t'].mean(),
nov_raq_4['t'].mean(),
nov_raq_5['t'].mean(),
nov_raq_6['t'].mean(),
nov_raq_7['t'].mean(),
nov_raq_8['t'].mean(),
nov_raq_9['t'].mean(),
nov_raq_10['t'].mean(),
nov_raq_11['t'].mean(),
nov_raq_12['t'].mean(),
nov_raq_13['t'].mean(),
nov_raq_14['t'].mean(),
nov_raq_15['t'].mean(),
nov_raq_16['t'].mean(),
nov_raq_17['t'].mean(),
nov_raq_18['t'].mean(),
nov_raq_19['t'].mean(),
nov_raq_20['t'].mean(),
nov_raq_21['t'].mean(),
nov_raq_22['t'].mean(),
nov_raq_23['t'].mean()])}
nov_av=pd.DataFrame(nov_a)
nov_av['delta1'] = np.arange(len(nov_av))
dec_a={'t':pd.Series([dec_raq_0['t'].mean(),
dec_raq_1['t'].mean(),
dec_raq_2['t'].mean(),
dec_raq_3['t'].mean(),
dec_raq_4['t'].mean(),
dec_raq_5['t'].mean(),
dec_raq_6['t'].mean(),
dec_raq_7['t'].mean(),
dec_raq_8['t'].mean(),
dec_raq_9['t'].mean(),
dec_raq_10['t'].mean(),
dec_raq_11['t'].mean(),
dec_raq_12['t'].mean(),
dec_raq_13['t'].mean(),
dec_raq_14['t'].mean(),
dec_raq_15['t'].mean(),
dec_raq_16['t'].mean(),
dec_raq_17['t'].mean(),
dec_raq_18['t'].mean(),
dec_raq_19['t'].mean(),
dec_raq_20['t'].mean(),
dec_raq_21['t'].mean(),
dec_raq_22['t'].mean(),
dec_raq_23['t'].mean()])}
dec_av=pd.DataFrame(dec_a)
dec_av['delta1'] = np.arange(len(dec_av))

x1 = jan_4['delta1']
x2 = feb_4['delta1']
x3 = mar_4['delta1']
x4 = apr_4['delta1']
x5 = may_4['delta1']
x6 = jun_4['delta1']
x7 = jul_4['delta1']
x8 = aug_4['delta1']
x9 = sep_4['delta1']
x10 = oct_4['delta1']
x11 = nov_4['delta1']
x12 = dic_4['delta1']

y1 = jan_av['t']
y2 = feb_av['t']
y3 = mar_av['t']
y4 = apr_av['t']
y5 = may_av['t']
y6 = jun_av['t']
y7 = jul_av['t']
y8 = aug_av['t']
y9 = sep_av['t']
y10 = oct_av['t']
y11 = nov_av['t']
y12 = dec_av['t']

#jan
plt.subplot(3, 4, 1)
plt.plot(x1, y1,color='red',linewidth=1)
plt.title('January-4')
plt.ylabel('T($^{o}$C)')
plt.tick_params(axis='both', which='both', right=False, left=False, top=False, bottom=False)
#feb
plt.subplot(3, 4, 2)
plt.plot(x2, y2,color='red',linewidth=1)
plt.title('February-4')
#mar
plt.subplot(3, 4, 3)
plt.plot(x3, y3,color='red',linewidth=1)
plt.title('March-4')
plt.show()
#apr
plt.subplot(3, 4, 4)
plt.plot(x4, y4,color='red',linewidth=1)
plt.title('April-4')
#may
plt.subplot(3, 4, 5)
plt.plot(x5, y5,color='red',linewidth=1)
plt.title('May-4')
plt.ylabel('T($^{o}$C)')
#jun
plt.subplot(3, 4, 6)
plt.plot(x6, y6,color='red',linewidth=1)
plt.title('June-4')

#jul
plt.subplot(3, 4, 7)
plt.plot(x7,y7,color='red',linewidth=1)
plt.title('July-4')

#aug
plt.subplot(3, 4, 8)
plt.plot(x8, y8,color='red',linewidth=1)
plt.title('August-4')

#sep
plt.subplot(3, 4, 9)
plt.plot(x9, y9,color='red',linewidth=1)
plt.title('September-4')
plt.ylabel('T($^{o}$C)')
plt.xlabel('Local time (h)')
#Oct
plt.subplot(3, 4, 10)
plt.plot(x10, y10,color='red',linewidth=1)
plt.title('October-4')
plt.ylabel('Local time (h)')

#Nov
plt.subplot(3, 4, 11)
plt.plot(x11, y11,color='red',linewidth=1)
plt.title('November-4')
plt.ylabel('Local time (h)')

#Dic
plt.subplot(3, 4, 12)
plt.plot(x12, y12,color='red',linewidth=1)
plt.title('December-4')
plt.ylabel('Local time (h)')


fig, axs = plt.subplots(3, 4)
axs[0, 0].plot(x1, y1,color='firebrick',linewidth=1)
axs[0, 0].set_title('January')
axs[0, 0].set_yticks([0,5, 10, 15, 20, 25])
axs[0, 0].set_xlim(0,23)
axs[0, 0].set_ylim(0,25)
axs[0, 1].plot(x2, y2,color='firebrick',linewidth=1)
axs[0, 1].set_title('February')
axs[0, 1].set_xlim(0,23)
axs[0, 1].set_ylim(0,25)
axs[0, 2].plot(x3, y3,color='firebrick',linewidth=1)
axs[0, 2].set_title('March')
axs[0, 2].set_xlim(0,23)
axs[0, 2].set_ylim(0,25)
axs[0, 3].plot(x4, y4,color='firebrick',linewidth=1)
axs[0, 3].set_title('April')
axs[0, 3].set_ylim(0,25)
axs[0, 3].set_xlim(0,23)
axs[1, 0].plot(x5, y5,color='firebrick',linewidth=1)
axs[1, 0].set_title('May')
axs[1, 0].set_yticks([0,5, 10, 15, 20, 25])
axs[1, 0].set_ylim(0,25)
axs[1, 0].set_xlim(0,23)
axs[1, 1].plot(x6, y6,color='firebrick',linewidth=1)
axs[1, 1].set_title('June')
axs[1, 1].set_ylim(0,25)
axs[1, 1].set_xlim(0,23)
axs[1, 2].plot(x7, y7,color='firebrick',linewidth=1)
axs[1, 2].set_title('July')
axs[1, 2].set_ylim(0,25)
axs[1, 2].set_xlim(0,23)
axs[1, 3].plot(x8, y8,color='firebrick',linewidth=1)
axs[1, 3].set_title('August')
axs[1, 3].set_ylim(0,25)
axs[1, 3].set_xlim(0,23)
axs[2, 0].plot(x9, y9,color='firebrick',linewidth=1)
axs[2, 0].set_title('September')
axs[2, 0].set_yticks([0,5, 10, 15, 20, 25])
axs[2, 0].set_xticks([0, 10, 20])
axs[2, 0].set_ylim(0,25)
axs[2, 0].set_xlim(0,23)
axs[2, 1].plot(x10, y10,color='firebrick',linewidth=1)
axs[2, 1].set_title('October')
axs[2, 1].set_xticks([0, 10, 20])
axs[2, 1].set_ylim(0,25)
axs[2, 1].set_xlim(0,23)
axs[2, 2].plot(x11, y11,color='firebrick',linewidth=1)
axs[2, 2].set_title('November')
axs[2, 2].set_xticks([0, 10, 20])
axs[2, 2].set_ylim(0,25)
axs[2, 2].set_xlim(0,23)
axs[2, 3].plot(x12, y12,color='firebrick',linewidth=1)
axs[2, 3].set_title('December')
axs[2, 3].set_xticks([0, 10, 20])
axs[2, 3].set_ylim(0,25)
axs[2, 3].set_xlim(0,23)
for ax in axs.flat:
    ax.set(xlabel='Local time (h)', ylabel='T($^{o}C$)')
#Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
plt.subplots_adjust(bottom=0.1, right=1.7, top=1.5)
plt.figure(figsize=(50,50))
plt.tight_layout(pad=0.4, w_pad=1, h_pad=1.0)
#plt.savefig('profiles_temp_raq_2018.png', dpi=200,bbox_inches="tight")
fig.savefig('temp_profile_raq.png',dpi=600,bbox_inches="tight")
plt.show()

