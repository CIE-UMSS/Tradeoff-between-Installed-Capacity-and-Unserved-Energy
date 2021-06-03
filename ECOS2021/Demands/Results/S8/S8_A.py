#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:01:10 2020

@author: alejandrosoto
"""

import pandas as pd
import numpy as np

Jan=pd.read_csv('Jan_S8_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Feb=pd.read_csv('Feb_S8_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Mar=pd.read_csv('Mar_S8_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Apr=pd.read_csv('Apr_S8_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
May=pd.read_csv('May_S8_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jun=pd.read_csv('Jun_S8_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Jul=pd.read_csv('Jul_S8_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Aug=pd.read_csv('Aug_S8_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Sep=pd.read_csv('Sep_S8_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Oct=pd.read_csv('Oct_S8_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Nov=pd.read_csv('Nov_S8_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
Dec=pd.read_csv('Dec_S8_A.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
p=pd.concat([Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec],ignore_index=True)
p['min'] = np.arange(len(p))
p_split = np.array_split(p, 8760)
for i in range (0,8760,1):
    p_split[i]['0'] = p_split[i]['0'].astype(float)
    globals()['string%s' % i]=p_split[i]['0'].mean()
e = []
for i in range (0,8760,1):
    e.append({'power_hourly': globals()['string%s' % i]})
pd.DataFrame(e)
df = pd.DataFrame(np.array([e]).T)
df.columns =['power']
df['power'] = df['power'].astype(str)
df[['gar','power']] = df.power.str.split(":",expand=True,)
df['power'] = df['power'].str.replace(r'}', '')
df['power'] = df['power'].astype(float)
df=df.rename(columns={'power': '1'})
df.index = np.arange(1, len(df)+1)
del df['gar']
df.to_csv('hourly_S8_A.csv')

