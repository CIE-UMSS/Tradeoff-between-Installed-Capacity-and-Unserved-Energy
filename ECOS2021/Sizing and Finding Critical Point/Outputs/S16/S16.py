#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:54:43 2020

@author: alejandrosoto
"""

import pandas as pd
import numpy as np

'''
df = pd.DataFrame(Data[0])
df.to_csv ('Results.csv', header=True)
'''
S16_0=pd.read_csv('S16_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_005=pd.read_csv('S16_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_01=pd.read_csv('S16_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_015=pd.read_csv('S16_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_02=pd.read_csv('S16_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_025=pd.read_csv('S16_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_03=pd.read_csv('S16_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_035=pd.read_csv('S16_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_04=pd.read_csv('S16_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_045=pd.read_csv('S16_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_05=pd.read_csv('S16_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_1=pd.read_csv('S16_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_2=pd.read_csv('S16_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_3=pd.read_csv('S16_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_4=pd.read_csv('S16_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_5=pd.read_csv('S16_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_6=pd.read_csv('S16_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_7=pd.read_csv('S16_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_8=pd.read_csv('S16_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_9=pd.read_csv('S16_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S16_10=pd.read_csv('S16_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S16_0_f=S16_0.pivot(index =S16_005.index, columns ='Unnamed: 0')
S16_0_f=S16_0_f.apply(lambda x: pd.Series(x.dropna().values))
S16_0_f.columns = S16_0_f.columns.droplevel(0)
S16_0_f = S16_0_f.loc[:, ~S16_0_f.columns.str.contains('^Unnamed')]

S16_005_f=S16_005.pivot(index =S16_005.index, columns ='Unnamed: 0')
S16_005_f=S16_005_f.apply(lambda x: pd.Series(x.dropna().values))
S16_005_f.columns = S16_005_f.columns.droplevel(0)
S16_005_f = S16_005_f.loc[:, ~S16_005_f.columns.str.contains('^Unnamed')]

S16_01_f=S16_01.pivot(index =S16_01.index, columns ='Unnamed: 0')
S16_01_f=S16_01_f.apply(lambda x: pd.Series(x.dropna().values))
S16_01_f.columns = S16_01_f.columns.droplevel(0)
S16_01_f = S16_01_f.loc[:, ~S16_01_f.columns.str.contains('^Unnamed')]

S16_015_f=S16_015.pivot(index =S16_015.index, columns ='Unnamed: 0')
S16_015_f=S16_015_f.apply(lambda x: pd.Series(x.dropna().values))
S16_015_f.columns = S16_015_f.columns.droplevel(0)
S16_015_f = S16_015_f.loc[:, ~S16_015_f.columns.str.contains('^Unnamed')]

S16_02_f=S16_02.pivot(index =S16_02.index, columns ='Unnamed: 0')
S16_02_f=S16_02_f.apply(lambda x: pd.Series(x.dropna().values))
S16_02_f.columns = S16_02_f.columns.droplevel(0)
S16_02_f = S16_02_f.loc[:, ~S16_02_f.columns.str.contains('^Unnamed')]

S16_025_f=S16_025.pivot(index =S16_025.index, columns ='Unnamed: 0')
S16_025_f=S16_025_f.apply(lambda x: pd.Series(x.dropna().values))
S16_025_f.columns = S16_025_f.columns.droplevel(0)
S16_025_f = S16_025_f.loc[:, ~S16_025_f.columns.str.contains('^Unnamed')]

S16_03_f=S16_03.pivot(index =S16_03.index, columns ='Unnamed: 0')
S16_03_f=S16_03_f.apply(lambda x: pd.Series(x.dropna().values))
S16_03_f.columns = S16_03_f.columns.droplevel(0)
S16_03_f = S16_03_f.loc[:, ~S16_03_f.columns.str.contains('^Unnamed')]

S16_035_f=S16_035.pivot(index =S16_035.index, columns ='Unnamed: 0')
S16_035_f=S16_035_f.apply(lambda x: pd.Series(x.dropna().values))
S16_035_f.columns = S16_035_f.columns.droplevel(0)
S16_035_f = S16_035_f.loc[:, ~S16_035_f.columns.str.contains('^Unnamed')]

S16_04_f=S16_04.pivot(index =S16_04.index, columns ='Unnamed: 0')
S16_04_f=S16_04_f.apply(lambda x: pd.Series(x.dropna().values))
S16_04_f.columns = S16_04_f.columns.droplevel(0)
S16_04_f = S16_04_f.loc[:, ~S16_04_f.columns.str.contains('^Unnamed')]

S16_045_f=S16_045.pivot(index =S16_045.index, columns ='Unnamed: 0')
S16_045_f=S16_045_f.apply(lambda x: pd.Series(x.dropna().values))
S16_045_f.columns = S16_045_f.columns.droplevel(0)
S16_045_f = S16_045_f.loc[:, ~S16_045_f.columns.str.contains('^Unnamed')]

S16_05_f=S16_05.pivot(index =S16_05.index, columns ='Unnamed: 0')
S16_05_f=S16_05_f.apply(lambda x: pd.Series(x.dropna().values))
S16_05_f.columns = S16_05_f.columns.droplevel(0)
S16_05_f = S16_05_f.loc[:, ~S16_05_f.columns.str.contains('^Unnamed')]

S16_1_f=S16_1.pivot(index =S16_1.index, columns ='Unnamed: 0')
S16_1_f=S16_1_f.apply(lambda x: pd.Series(x.dropna().values))
S16_1_f.columns = S16_1_f.columns.droplevel(0)
S16_1_f = S16_1_f.loc[:, ~S16_1_f.columns.str.contains('^Unnamed')]

S16_2_f=S16_2.pivot(index =S16_2.index, columns ='Unnamed: 0')
S16_2_f=S16_2_f.apply(lambda x: pd.Series(x.dropna().values))
S16_2_f.columns = S16_2_f.columns.droplevel(0)
S16_2_f = S16_2_f.loc[:, ~S16_2_f.columns.str.contains('^Unnamed')]

S16_3_f=S16_3.pivot(index =S16_3.index, columns ='Unnamed: 0')
S16_3_f=S16_3_f.apply(lambda x: pd.Series(x.dropna().values))
S16_3_f.columns = S16_3_f.columns.droplevel(0)
S16_3_f = S16_3_f.loc[:, ~S16_3_f.columns.str.contains('^Unnamed')]

S16_4_f=S16_4.pivot(index =S16_4.index, columns ='Unnamed: 0')
S16_4_f=S16_4_f.apply(lambda x: pd.Series(x.dropna().values))
S16_4_f.columns = S16_4_f.columns.droplevel(0)
S16_4_f = S16_4_f.loc[:, ~S16_4_f.columns.str.contains('^Unnamed')]

S16_5_f=S16_5.pivot(index =S16_5.index, columns ='Unnamed: 0')
S16_5_f=S16_5_f.apply(lambda x: pd.Series(x.dropna().values))
S16_5_f.columns = S16_5_f.columns.droplevel(0)
S16_5_f = S16_5_f.loc[:, ~S16_5_f.columns.str.contains('^Unnamed')]

S16_6_f=S16_6.pivot(index =S16_6.index, columns ='Unnamed: 0')
S16_6_f=S16_6_f.apply(lambda x: pd.Series(x.dropna().values))
S16_6_f.columns = S16_6_f.columns.droplevel(0)
S16_6_f = S16_6_f.loc[:, ~S16_6_f.columns.str.contains('^Unnamed')]

S16_7_f=S16_7.pivot(index =S16_7.index, columns ='Unnamed: 0')
S16_7_f=S16_7_f.apply(lambda x: pd.Series(x.dropna().values))
S16_7_f.columns = S16_7_f.columns.droplevel(0)
S16_7_f = S16_7_f.loc[:, ~S16_7_f.columns.str.contains('^Unnamed')]

S16_8_f=S16_8.pivot(index =S16_8.index, columns ='Unnamed: 0')
S16_8_f=S16_8_f.apply(lambda x: pd.Series(x.dropna().values))
S16_8_f.columns = S16_8_f.columns.droplevel(0)
S16_8_f = S16_8_f.loc[:, ~S16_8_f.columns.str.contains('^Unnamed')]

S16_9_f=S16_9.pivot(index =S16_9.index, columns ='Unnamed: 0')
S16_9_f=S16_9_f.apply(lambda x: pd.Series(x.dropna().values))
S16_9_f.columns = S16_9_f.columns.droplevel(0)
S16_9_f = S16_9_f.loc[:, ~S16_9_f.columns.str.contains('^Unnamed')]

S16_10_f=S16_10.pivot(index =S16_10.index, columns ='Unnamed: 0')
S16_10_f=S16_10_f.apply(lambda x: pd.Series(x.dropna().values))
S16_10_f.columns = S16_10_f.columns.droplevel(0)
S16_10_f = S16_10_f.loc[:, ~S16_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S16_0_f,S16_005_f,S16_01_f,S16_015_f,S16_02_f,S16_025_f,S16_03_f,S16_035_f,S16_04_f,S16_045_f,S16_05_f,S16_1_f,S16_2_f,S16_3_f,S16_4_f,S16_5_f,S16_6_f,S16_7_f,S16_8_f,S16_9_f,S16_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S16.csv', header=True)