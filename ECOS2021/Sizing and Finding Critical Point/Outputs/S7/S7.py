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
S7_0=pd.read_csv('S7_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_005=pd.read_csv('S7_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_01=pd.read_csv('S7_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_015=pd.read_csv('S7_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_02=pd.read_csv('S7_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_025=pd.read_csv('S7_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_03=pd.read_csv('S7_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_035=pd.read_csv('S7_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_04=pd.read_csv('S7_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_045=pd.read_csv('S7_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_05=pd.read_csv('S7_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_1=pd.read_csv('S7_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_2=pd.read_csv('S7_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_3=pd.read_csv('S7_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_4=pd.read_csv('S7_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_5=pd.read_csv('S7_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_6=pd.read_csv('S7_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_7=pd.read_csv('S7_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_8=pd.read_csv('S7_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_9=pd.read_csv('S7_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S7_10=pd.read_csv('S7_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S7_0_f=S7_0.pivot(index =S7_005.index, columns ='Unnamed: 0')
S7_0_f=S7_0_f.apply(lambda x: pd.Series(x.dropna().values))
S7_0_f.columns = S7_0_f.columns.droplevel(0)
S7_0_f = S7_0_f.loc[:, ~S7_0_f.columns.str.contains('^Unnamed')]

S7_005_f=S7_005.pivot(index =S7_005.index, columns ='Unnamed: 0')
S7_005_f=S7_005_f.apply(lambda x: pd.Series(x.dropna().values))
S7_005_f.columns = S7_005_f.columns.droplevel(0)
S7_005_f = S7_005_f.loc[:, ~S7_005_f.columns.str.contains('^Unnamed')]

S7_01_f=S7_01.pivot(index =S7_01.index, columns ='Unnamed: 0')
S7_01_f=S7_01_f.apply(lambda x: pd.Series(x.dropna().values))
S7_01_f.columns = S7_01_f.columns.droplevel(0)
S7_01_f = S7_01_f.loc[:, ~S7_01_f.columns.str.contains('^Unnamed')]

S7_015_f=S7_015.pivot(index =S7_015.index, columns ='Unnamed: 0')
S7_015_f=S7_015_f.apply(lambda x: pd.Series(x.dropna().values))
S7_015_f.columns = S7_015_f.columns.droplevel(0)
S7_015_f = S7_015_f.loc[:, ~S7_015_f.columns.str.contains('^Unnamed')]

S7_02_f=S7_02.pivot(index =S7_02.index, columns ='Unnamed: 0')
S7_02_f=S7_02_f.apply(lambda x: pd.Series(x.dropna().values))
S7_02_f.columns = S7_02_f.columns.droplevel(0)
S7_02_f = S7_02_f.loc[:, ~S7_02_f.columns.str.contains('^Unnamed')]

S7_025_f=S7_025.pivot(index =S7_025.index, columns ='Unnamed: 0')
S7_025_f=S7_025_f.apply(lambda x: pd.Series(x.dropna().values))
S7_025_f.columns = S7_025_f.columns.droplevel(0)
S7_025_f = S7_025_f.loc[:, ~S7_025_f.columns.str.contains('^Unnamed')]

S7_03_f=S7_03.pivot(index =S7_03.index, columns ='Unnamed: 0')
S7_03_f=S7_03_f.apply(lambda x: pd.Series(x.dropna().values))
S7_03_f.columns = S7_03_f.columns.droplevel(0)
S7_03_f = S7_03_f.loc[:, ~S7_03_f.columns.str.contains('^Unnamed')]

S7_035_f=S7_035.pivot(index =S7_035.index, columns ='Unnamed: 0')
S7_035_f=S7_035_f.apply(lambda x: pd.Series(x.dropna().values))
S7_035_f.columns = S7_035_f.columns.droplevel(0)
S7_035_f = S7_035_f.loc[:, ~S7_035_f.columns.str.contains('^Unnamed')]

S7_04_f=S7_04.pivot(index =S7_04.index, columns ='Unnamed: 0')
S7_04_f=S7_04_f.apply(lambda x: pd.Series(x.dropna().values))
S7_04_f.columns = S7_04_f.columns.droplevel(0)
S7_04_f = S7_04_f.loc[:, ~S7_04_f.columns.str.contains('^Unnamed')]

S7_045_f=S7_045.pivot(index =S7_045.index, columns ='Unnamed: 0')
S7_045_f=S7_045_f.apply(lambda x: pd.Series(x.dropna().values))
S7_045_f.columns = S7_045_f.columns.droplevel(0)
S7_045_f = S7_045_f.loc[:, ~S7_045_f.columns.str.contains('^Unnamed')]

S7_05_f=S7_05.pivot(index =S7_05.index, columns ='Unnamed: 0')
S7_05_f=S7_05_f.apply(lambda x: pd.Series(x.dropna().values))
S7_05_f.columns = S7_05_f.columns.droplevel(0)
S7_05_f = S7_05_f.loc[:, ~S7_05_f.columns.str.contains('^Unnamed')]

S7_1_f=S7_1.pivot(index =S7_1.index, columns ='Unnamed: 0')
S7_1_f=S7_1_f.apply(lambda x: pd.Series(x.dropna().values))
S7_1_f.columns = S7_1_f.columns.droplevel(0)
S7_1_f = S7_1_f.loc[:, ~S7_1_f.columns.str.contains('^Unnamed')]

S7_2_f=S7_2.pivot(index =S7_2.index, columns ='Unnamed: 0')
S7_2_f=S7_2_f.apply(lambda x: pd.Series(x.dropna().values))
S7_2_f.columns = S7_2_f.columns.droplevel(0)
S7_2_f = S7_2_f.loc[:, ~S7_2_f.columns.str.contains('^Unnamed')]

S7_3_f=S7_3.pivot(index =S7_3.index, columns ='Unnamed: 0')
S7_3_f=S7_3_f.apply(lambda x: pd.Series(x.dropna().values))
S7_3_f.columns = S7_3_f.columns.droplevel(0)
S7_3_f = S7_3_f.loc[:, ~S7_3_f.columns.str.contains('^Unnamed')]

S7_4_f=S7_4.pivot(index =S7_4.index, columns ='Unnamed: 0')
S7_4_f=S7_4_f.apply(lambda x: pd.Series(x.dropna().values))
S7_4_f.columns = S7_4_f.columns.droplevel(0)
S7_4_f = S7_4_f.loc[:, ~S7_4_f.columns.str.contains('^Unnamed')]

S7_5_f=S7_5.pivot(index =S7_5.index, columns ='Unnamed: 0')
S7_5_f=S7_5_f.apply(lambda x: pd.Series(x.dropna().values))
S7_5_f.columns = S7_5_f.columns.droplevel(0)
S7_5_f = S7_5_f.loc[:, ~S7_5_f.columns.str.contains('^Unnamed')]

S7_6_f=S7_6.pivot(index =S7_6.index, columns ='Unnamed: 0')
S7_6_f=S7_6_f.apply(lambda x: pd.Series(x.dropna().values))
S7_6_f.columns = S7_6_f.columns.droplevel(0)
S7_6_f = S7_6_f.loc[:, ~S7_6_f.columns.str.contains('^Unnamed')]

S7_7_f=S7_7.pivot(index =S7_7.index, columns ='Unnamed: 0')
S7_7_f=S7_7_f.apply(lambda x: pd.Series(x.dropna().values))
S7_7_f.columns = S7_7_f.columns.droplevel(0)
S7_7_f = S7_7_f.loc[:, ~S7_7_f.columns.str.contains('^Unnamed')]

S7_8_f=S7_8.pivot(index =S7_8.index, columns ='Unnamed: 0')
S7_8_f=S7_8_f.apply(lambda x: pd.Series(x.dropna().values))
S7_8_f.columns = S7_8_f.columns.droplevel(0)
S7_8_f = S7_8_f.loc[:, ~S7_8_f.columns.str.contains('^Unnamed')]

S7_9_f=S7_9.pivot(index =S7_9.index, columns ='Unnamed: 0')
S7_9_f=S7_9_f.apply(lambda x: pd.Series(x.dropna().values))
S7_9_f.columns = S7_9_f.columns.droplevel(0)
S7_9_f = S7_9_f.loc[:, ~S7_9_f.columns.str.contains('^Unnamed')]

S7_10_f=S7_10.pivot(index =S7_10.index, columns ='Unnamed: 0')
S7_10_f=S7_10_f.apply(lambda x: pd.Series(x.dropna().values))
S7_10_f.columns = S7_10_f.columns.droplevel(0)
S7_10_f = S7_10_f.loc[:, ~S7_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S7_0_f,S7_005_f,S7_01_f,S7_015_f,S7_02_f,S7_025_f,S7_03_f,S7_035_f,S7_04_f,S7_045_f,S7_05_f,S7_1_f,S7_2_f,S7_3_f,S7_4_f,S7_5_f,S7_6_f,S7_7_f,S7_8_f,S7_9_f,S7_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S7.csv', header=True)
