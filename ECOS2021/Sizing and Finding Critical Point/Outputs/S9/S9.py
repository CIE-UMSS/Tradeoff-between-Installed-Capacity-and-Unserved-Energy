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
S9_0=pd.read_csv('S9_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_005=pd.read_csv('S9_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_01=pd.read_csv('S9_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_015=pd.read_csv('S9_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_02=pd.read_csv('S9_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_025=pd.read_csv('S9_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_03=pd.read_csv('S9_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_035=pd.read_csv('S9_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_04=pd.read_csv('S9_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_045=pd.read_csv('S9_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_05=pd.read_csv('S9_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_1=pd.read_csv('S9_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_2=pd.read_csv('S9_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_3=pd.read_csv('S9_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_4=pd.read_csv('S9_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_5=pd.read_csv('S9_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_6=pd.read_csv('S9_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_7=pd.read_csv('S9_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_8=pd.read_csv('S9_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_9=pd.read_csv('S9_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S9_10=pd.read_csv('S9_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S9_0_f=S9_0.pivot(index =S9_005.index, columns ='Unnamed: 0')
S9_0_f=S9_0_f.apply(lambda x: pd.Series(x.dropna().values))
S9_0_f.columns = S9_0_f.columns.droplevel(0)
S9_0_f = S9_0_f.loc[:, ~S9_0_f.columns.str.contains('^Unnamed')]

S9_005_f=S9_005.pivot(index =S9_005.index, columns ='Unnamed: 0')
S9_005_f=S9_005_f.apply(lambda x: pd.Series(x.dropna().values))
S9_005_f.columns = S9_005_f.columns.droplevel(0)
S9_005_f = S9_005_f.loc[:, ~S9_005_f.columns.str.contains('^Unnamed')]

S9_01_f=S9_01.pivot(index =S9_01.index, columns ='Unnamed: 0')
S9_01_f=S9_01_f.apply(lambda x: pd.Series(x.dropna().values))
S9_01_f.columns = S9_01_f.columns.droplevel(0)
S9_01_f = S9_01_f.loc[:, ~S9_01_f.columns.str.contains('^Unnamed')]

S9_015_f=S9_015.pivot(index =S9_015.index, columns ='Unnamed: 0')
S9_015_f=S9_015_f.apply(lambda x: pd.Series(x.dropna().values))
S9_015_f.columns = S9_015_f.columns.droplevel(0)
S9_015_f = S9_015_f.loc[:, ~S9_015_f.columns.str.contains('^Unnamed')]

S9_02_f=S9_02.pivot(index =S9_02.index, columns ='Unnamed: 0')
S9_02_f=S9_02_f.apply(lambda x: pd.Series(x.dropna().values))
S9_02_f.columns = S9_02_f.columns.droplevel(0)
S9_02_f = S9_02_f.loc[:, ~S9_02_f.columns.str.contains('^Unnamed')]

S9_025_f=S9_025.pivot(index =S9_025.index, columns ='Unnamed: 0')
S9_025_f=S9_025_f.apply(lambda x: pd.Series(x.dropna().values))
S9_025_f.columns = S9_025_f.columns.droplevel(0)
S9_025_f = S9_025_f.loc[:, ~S9_025_f.columns.str.contains('^Unnamed')]

S9_03_f=S9_03.pivot(index =S9_03.index, columns ='Unnamed: 0')
S9_03_f=S9_03_f.apply(lambda x: pd.Series(x.dropna().values))
S9_03_f.columns = S9_03_f.columns.droplevel(0)
S9_03_f = S9_03_f.loc[:, ~S9_03_f.columns.str.contains('^Unnamed')]

S9_035_f=S9_035.pivot(index =S9_035.index, columns ='Unnamed: 0')
S9_035_f=S9_035_f.apply(lambda x: pd.Series(x.dropna().values))
S9_035_f.columns = S9_035_f.columns.droplevel(0)
S9_035_f = S9_035_f.loc[:, ~S9_035_f.columns.str.contains('^Unnamed')]

S9_04_f=S9_04.pivot(index =S9_04.index, columns ='Unnamed: 0')
S9_04_f=S9_04_f.apply(lambda x: pd.Series(x.dropna().values))
S9_04_f.columns = S9_04_f.columns.droplevel(0)
S9_04_f = S9_04_f.loc[:, ~S9_04_f.columns.str.contains('^Unnamed')]

S9_045_f=S9_045.pivot(index =S9_045.index, columns ='Unnamed: 0')
S9_045_f=S9_045_f.apply(lambda x: pd.Series(x.dropna().values))
S9_045_f.columns = S9_045_f.columns.droplevel(0)
S9_045_f = S9_045_f.loc[:, ~S9_045_f.columns.str.contains('^Unnamed')]

S9_05_f=S9_05.pivot(index =S9_05.index, columns ='Unnamed: 0')
S9_05_f=S9_05_f.apply(lambda x: pd.Series(x.dropna().values))
S9_05_f.columns = S9_05_f.columns.droplevel(0)
S9_05_f = S9_05_f.loc[:, ~S9_05_f.columns.str.contains('^Unnamed')]

S9_1_f=S9_1.pivot(index =S9_1.index, columns ='Unnamed: 0')
S9_1_f=S9_1_f.apply(lambda x: pd.Series(x.dropna().values))
S9_1_f.columns = S9_1_f.columns.droplevel(0)
S9_1_f = S9_1_f.loc[:, ~S9_1_f.columns.str.contains('^Unnamed')]

S9_2_f=S9_2.pivot(index =S9_2.index, columns ='Unnamed: 0')
S9_2_f=S9_2_f.apply(lambda x: pd.Series(x.dropna().values))
S9_2_f.columns = S9_2_f.columns.droplevel(0)
S9_2_f = S9_2_f.loc[:, ~S9_2_f.columns.str.contains('^Unnamed')]

S9_3_f=S9_3.pivot(index =S9_3.index, columns ='Unnamed: 0')
S9_3_f=S9_3_f.apply(lambda x: pd.Series(x.dropna().values))
S9_3_f.columns = S9_3_f.columns.droplevel(0)
S9_3_f = S9_3_f.loc[:, ~S9_3_f.columns.str.contains('^Unnamed')]

S9_4_f=S9_4.pivot(index =S9_4.index, columns ='Unnamed: 0')
S9_4_f=S9_4_f.apply(lambda x: pd.Series(x.dropna().values))
S9_4_f.columns = S9_4_f.columns.droplevel(0)
S9_4_f = S9_4_f.loc[:, ~S9_4_f.columns.str.contains('^Unnamed')]

S9_5_f=S9_5.pivot(index =S9_5.index, columns ='Unnamed: 0')
S9_5_f=S9_5_f.apply(lambda x: pd.Series(x.dropna().values))
S9_5_f.columns = S9_5_f.columns.droplevel(0)
S9_5_f = S9_5_f.loc[:, ~S9_5_f.columns.str.contains('^Unnamed')]

S9_6_f=S9_6.pivot(index =S9_6.index, columns ='Unnamed: 0')
S9_6_f=S9_6_f.apply(lambda x: pd.Series(x.dropna().values))
S9_6_f.columns = S9_6_f.columns.droplevel(0)
S9_6_f = S9_6_f.loc[:, ~S9_6_f.columns.str.contains('^Unnamed')]

S9_7_f=S9_7.pivot(index =S9_7.index, columns ='Unnamed: 0')
S9_7_f=S9_7_f.apply(lambda x: pd.Series(x.dropna().values))
S9_7_f.columns = S9_7_f.columns.droplevel(0)
S9_7_f = S9_7_f.loc[:, ~S9_7_f.columns.str.contains('^Unnamed')]

S9_8_f=S9_8.pivot(index =S9_8.index, columns ='Unnamed: 0')
S9_8_f=S9_8_f.apply(lambda x: pd.Series(x.dropna().values))
S9_8_f.columns = S9_8_f.columns.droplevel(0)
S9_8_f = S9_8_f.loc[:, ~S9_8_f.columns.str.contains('^Unnamed')]

S9_9_f=S9_9.pivot(index =S9_9.index, columns ='Unnamed: 0')
S9_9_f=S9_9_f.apply(lambda x: pd.Series(x.dropna().values))
S9_9_f.columns = S9_9_f.columns.droplevel(0)
S9_9_f = S9_9_f.loc[:, ~S9_9_f.columns.str.contains('^Unnamed')]

S9_10_f=S9_10.pivot(index =S9_10.index, columns ='Unnamed: 0')
S9_10_f=S9_10_f.apply(lambda x: pd.Series(x.dropna().values))
S9_10_f.columns = S9_10_f.columns.droplevel(0)
S9_10_f = S9_10_f.loc[:, ~S9_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S9_0_f,S9_005_f,S9_01_f,S9_015_f,S9_02_f,S9_025_f,S9_03_f,S9_035_f,S9_04_f,S9_045_f,S9_05_f,S9_1_f,S9_2_f,S9_3_f,S9_4_f,S9_5_f,S9_6_f,S9_7_f,S9_8_f,S9_9_f,S9_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S9.csv', header=True)