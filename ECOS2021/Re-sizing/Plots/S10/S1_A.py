#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:01:10 2020

@author: alejandrosoto
"""

import pandas as pd
import numpy as np

p=pd.read_csv('year.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

#p=pd.concat([Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec],ignore_index=True)
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
df.to_csv('hourly_S1_A.csv')

