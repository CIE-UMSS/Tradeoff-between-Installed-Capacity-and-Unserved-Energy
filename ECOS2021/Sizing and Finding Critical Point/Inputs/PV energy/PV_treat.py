#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:15:14 2021

@author: alejandrosoto
"""

import pandas as pd
import numpy as np
PV = pd.read_csv('Data_PV.csv', sep=' ', decimal='.', encoding='latin1', error_bad_lines=False)
PV= PV.rename(columns={',1': 'power'})
PV[['time_step','power_kW']] = PV.power.str.split(",",expand=True,)
PV['power_kW'] = PV['power_kW'].astype(float)
PV['time_step'] = PV['time_step'].astype(float)
del PV['power']
PV['power_W']=PV['power_kW']*100
del PV['power_kW']
del PV['time_step']
PV=PV.rename(columns={'power_W': '1'})
PV.index = np.arange(1, len(PV)+1)
PV.to_csv('PV_Energy.csv')
