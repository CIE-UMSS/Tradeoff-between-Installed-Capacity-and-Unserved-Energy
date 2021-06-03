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
S11_0=pd.read_csv('S11_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_005=pd.read_csv('S11_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_01=pd.read_csv('S11_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_015=pd.read_csv('S11_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_02=pd.read_csv('S11_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_025=pd.read_csv('S11_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_03=pd.read_csv('S11_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_035=pd.read_csv('S11_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_04=pd.read_csv('S11_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_045=pd.read_csv('S11_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_05=pd.read_csv('S11_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_1=pd.read_csv('S11_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_2=pd.read_csv('S11_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_3=pd.read_csv('S11_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_4=pd.read_csv('S11_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_5=pd.read_csv('S11_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_6=pd.read_csv('S11_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_7=pd.read_csv('S11_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_8=pd.read_csv('S11_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_9=pd.read_csv('S11_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S11_10=pd.read_csv('S11_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S11_0_f=S11_0.pivot(index =S11_005.index, columns ='Unnamed: 0')
S11_0_f=S11_0_f.apply(lambda x: pd.Series(x.dropna().values))
S11_0_f.columns = S11_0_f.columns.droplevel(0)
S11_0_f = S11_0_f.loc[:, ~S11_0_f.columns.str.contains('^Unnamed')]

S11_005_f=S11_005.pivot(index =S11_005.index, columns ='Unnamed: 0')
S11_005_f=S11_005_f.apply(lambda x: pd.Series(x.dropna().values))
S11_005_f.columns = S11_005_f.columns.droplevel(0)
S11_005_f = S11_005_f.loc[:, ~S11_005_f.columns.str.contains('^Unnamed')]

S11_01_f=S11_01.pivot(index =S11_01.index, columns ='Unnamed: 0')
S11_01_f=S11_01_f.apply(lambda x: pd.Series(x.dropna().values))
S11_01_f.columns = S11_01_f.columns.droplevel(0)
S11_01_f = S11_01_f.loc[:, ~S11_01_f.columns.str.contains('^Unnamed')]

S11_015_f=S11_015.pivot(index =S11_015.index, columns ='Unnamed: 0')
S11_015_f=S11_015_f.apply(lambda x: pd.Series(x.dropna().values))
S11_015_f.columns = S11_015_f.columns.droplevel(0)
S11_015_f = S11_015_f.loc[:, ~S11_015_f.columns.str.contains('^Unnamed')]

S11_02_f=S11_02.pivot(index =S11_02.index, columns ='Unnamed: 0')
S11_02_f=S11_02_f.apply(lambda x: pd.Series(x.dropna().values))
S11_02_f.columns = S11_02_f.columns.droplevel(0)
S11_02_f = S11_02_f.loc[:, ~S11_02_f.columns.str.contains('^Unnamed')]

S11_025_f=S11_025.pivot(index =S11_025.index, columns ='Unnamed: 0')
S11_025_f=S11_025_f.apply(lambda x: pd.Series(x.dropna().values))
S11_025_f.columns = S11_025_f.columns.droplevel(0)
S11_025_f = S11_025_f.loc[:, ~S11_025_f.columns.str.contains('^Unnamed')]

S11_03_f=S11_03.pivot(index =S11_03.index, columns ='Unnamed: 0')
S11_03_f=S11_03_f.apply(lambda x: pd.Series(x.dropna().values))
S11_03_f.columns = S11_03_f.columns.droplevel(0)
S11_03_f = S11_03_f.loc[:, ~S11_03_f.columns.str.contains('^Unnamed')]

S11_035_f=S11_035.pivot(index =S11_035.index, columns ='Unnamed: 0')
S11_035_f=S11_035_f.apply(lambda x: pd.Series(x.dropna().values))
S11_035_f.columns = S11_035_f.columns.droplevel(0)
S11_035_f = S11_035_f.loc[:, ~S11_035_f.columns.str.contains('^Unnamed')]

S11_04_f=S11_04.pivot(index =S11_04.index, columns ='Unnamed: 0')
S11_04_f=S11_04_f.apply(lambda x: pd.Series(x.dropna().values))
S11_04_f.columns = S11_04_f.columns.droplevel(0)
S11_04_f = S11_04_f.loc[:, ~S11_04_f.columns.str.contains('^Unnamed')]

S11_045_f=S11_045.pivot(index =S11_045.index, columns ='Unnamed: 0')
S11_045_f=S11_045_f.apply(lambda x: pd.Series(x.dropna().values))
S11_045_f.columns = S11_045_f.columns.droplevel(0)
S11_045_f = S11_045_f.loc[:, ~S11_045_f.columns.str.contains('^Unnamed')]

S11_05_f=S11_05.pivot(index =S11_05.index, columns ='Unnamed: 0')
S11_05_f=S11_05_f.apply(lambda x: pd.Series(x.dropna().values))
S11_05_f.columns = S11_05_f.columns.droplevel(0)
S11_05_f = S11_05_f.loc[:, ~S11_05_f.columns.str.contains('^Unnamed')]

S11_1_f=S11_1.pivot(index =S11_1.index, columns ='Unnamed: 0')
S11_1_f=S11_1_f.apply(lambda x: pd.Series(x.dropna().values))
S11_1_f.columns = S11_1_f.columns.droplevel(0)
S11_1_f = S11_1_f.loc[:, ~S11_1_f.columns.str.contains('^Unnamed')]

S11_2_f=S11_2.pivot(index =S11_2.index, columns ='Unnamed: 0')
S11_2_f=S11_2_f.apply(lambda x: pd.Series(x.dropna().values))
S11_2_f.columns = S11_2_f.columns.droplevel(0)
S11_2_f = S11_2_f.loc[:, ~S11_2_f.columns.str.contains('^Unnamed')]

S11_3_f=S11_3.pivot(index =S11_3.index, columns ='Unnamed: 0')
S11_3_f=S11_3_f.apply(lambda x: pd.Series(x.dropna().values))
S11_3_f.columns = S11_3_f.columns.droplevel(0)
S11_3_f = S11_3_f.loc[:, ~S11_3_f.columns.str.contains('^Unnamed')]

S11_4_f=S11_4.pivot(index =S11_4.index, columns ='Unnamed: 0')
S11_4_f=S11_4_f.apply(lambda x: pd.Series(x.dropna().values))
S11_4_f.columns = S11_4_f.columns.droplevel(0)
S11_4_f = S11_4_f.loc[:, ~S11_4_f.columns.str.contains('^Unnamed')]

S11_5_f=S11_5.pivot(index =S11_5.index, columns ='Unnamed: 0')
S11_5_f=S11_5_f.apply(lambda x: pd.Series(x.dropna().values))
S11_5_f.columns = S11_5_f.columns.droplevel(0)
S11_5_f = S11_5_f.loc[:, ~S11_5_f.columns.str.contains('^Unnamed')]

S11_6_f=S11_6.pivot(index =S11_6.index, columns ='Unnamed: 0')
S11_6_f=S11_6_f.apply(lambda x: pd.Series(x.dropna().values))
S11_6_f.columns = S11_6_f.columns.droplevel(0)
S11_6_f = S11_6_f.loc[:, ~S11_6_f.columns.str.contains('^Unnamed')]

S11_7_f=S11_7.pivot(index =S11_7.index, columns ='Unnamed: 0')
S11_7_f=S11_7_f.apply(lambda x: pd.Series(x.dropna().values))
S11_7_f.columns = S11_7_f.columns.droplevel(0)
S11_7_f = S11_7_f.loc[:, ~S11_7_f.columns.str.contains('^Unnamed')]

S11_8_f=S11_8.pivot(index =S11_8.index, columns ='Unnamed: 0')
S11_8_f=S11_8_f.apply(lambda x: pd.Series(x.dropna().values))
S11_8_f.columns = S11_8_f.columns.droplevel(0)
S11_8_f = S11_8_f.loc[:, ~S11_8_f.columns.str.contains('^Unnamed')]

S11_9_f=S11_9.pivot(index =S11_9.index, columns ='Unnamed: 0')
S11_9_f=S11_9_f.apply(lambda x: pd.Series(x.dropna().values))
S11_9_f.columns = S11_9_f.columns.droplevel(0)
S11_9_f = S11_9_f.loc[:, ~S11_9_f.columns.str.contains('^Unnamed')]

S11_10_f=S11_10.pivot(index =S11_10.index, columns ='Unnamed: 0')
S11_10_f=S11_10_f.apply(lambda x: pd.Series(x.dropna().values))
S11_10_f.columns = S11_10_f.columns.droplevel(0)
S11_10_f = S11_10_f.loc[:, ~S11_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S11_0_f,S11_005_f,S11_01_f,S11_015_f,S11_02_f,S11_025_f,S11_03_f,S11_035_f,S11_04_f,S11_045_f,S11_05_f,S11_1_f,S11_2_f,S11_3_f,S11_4_f,S11_5_f,S11_6_f,S11_7_f,S11_8_f,S11_9_f,S11_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S11.csv', header=True)