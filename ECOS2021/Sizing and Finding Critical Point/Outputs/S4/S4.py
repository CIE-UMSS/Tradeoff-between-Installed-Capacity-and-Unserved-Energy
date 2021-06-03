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
S4_0=pd.read_csv('S4_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_005=pd.read_csv('S4_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_01=pd.read_csv('S4_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_015=pd.read_csv('S4_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_02=pd.read_csv('S4_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_025=pd.read_csv('S4_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_03=pd.read_csv('S4_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_035=pd.read_csv('S4_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_04=pd.read_csv('S4_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_045=pd.read_csv('S4_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_05=pd.read_csv('S4_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_1=pd.read_csv('S4_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_2=pd.read_csv('S4_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_3=pd.read_csv('S4_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_4=pd.read_csv('S4_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_5=pd.read_csv('S4_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_6=pd.read_csv('S4_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_7=pd.read_csv('S4_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_8=pd.read_csv('S4_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_9=pd.read_csv('S4_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S4_10=pd.read_csv('S4_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S4_0_f=S4_0.pivot(index =S4_005.index, columns ='Unnamed: 0')
S4_0_f=S4_0_f.apply(lambda x: pd.Series(x.dropna().values))
S4_0_f.columns = S4_0_f.columns.droplevel(0)
S4_0_f = S4_0_f.loc[:, ~S4_0_f.columns.str.contains('^Unnamed')]

S4_005_f=S4_005.pivot(index =S4_005.index, columns ='Unnamed: 0')
S4_005_f=S4_005_f.apply(lambda x: pd.Series(x.dropna().values))
S4_005_f.columns = S4_005_f.columns.droplevel(0)
S4_005_f = S4_005_f.loc[:, ~S4_005_f.columns.str.contains('^Unnamed')]

S4_01_f=S4_01.pivot(index =S4_01.index, columns ='Unnamed: 0')
S4_01_f=S4_01_f.apply(lambda x: pd.Series(x.dropna().values))
S4_01_f.columns = S4_01_f.columns.droplevel(0)
S4_01_f = S4_01_f.loc[:, ~S4_01_f.columns.str.contains('^Unnamed')]

S4_015_f=S4_015.pivot(index =S4_015.index, columns ='Unnamed: 0')
S4_015_f=S4_015_f.apply(lambda x: pd.Series(x.dropna().values))
S4_015_f.columns = S4_015_f.columns.droplevel(0)
S4_015_f = S4_015_f.loc[:, ~S4_015_f.columns.str.contains('^Unnamed')]

S4_02_f=S4_02.pivot(index =S4_02.index, columns ='Unnamed: 0')
S4_02_f=S4_02_f.apply(lambda x: pd.Series(x.dropna().values))
S4_02_f.columns = S4_02_f.columns.droplevel(0)
S4_02_f = S4_02_f.loc[:, ~S4_02_f.columns.str.contains('^Unnamed')]

S4_025_f=S4_025.pivot(index =S4_025.index, columns ='Unnamed: 0')
S4_025_f=S4_025_f.apply(lambda x: pd.Series(x.dropna().values))
S4_025_f.columns = S4_025_f.columns.droplevel(0)
S4_025_f = S4_025_f.loc[:, ~S4_025_f.columns.str.contains('^Unnamed')]

S4_03_f=S4_03.pivot(index =S4_03.index, columns ='Unnamed: 0')
S4_03_f=S4_03_f.apply(lambda x: pd.Series(x.dropna().values))
S4_03_f.columns = S4_03_f.columns.droplevel(0)
S4_03_f = S4_03_f.loc[:, ~S4_03_f.columns.str.contains('^Unnamed')]

S4_035_f=S4_035.pivot(index =S4_035.index, columns ='Unnamed: 0')
S4_035_f=S4_035_f.apply(lambda x: pd.Series(x.dropna().values))
S4_035_f.columns = S4_035_f.columns.droplevel(0)
S4_035_f = S4_035_f.loc[:, ~S4_035_f.columns.str.contains('^Unnamed')]

S4_04_f=S4_04.pivot(index =S4_04.index, columns ='Unnamed: 0')
S4_04_f=S4_04_f.apply(lambda x: pd.Series(x.dropna().values))
S4_04_f.columns = S4_04_f.columns.droplevel(0)
S4_04_f = S4_04_f.loc[:, ~S4_04_f.columns.str.contains('^Unnamed')]

S4_045_f=S4_045.pivot(index =S4_045.index, columns ='Unnamed: 0')
S4_045_f=S4_045_f.apply(lambda x: pd.Series(x.dropna().values))
S4_045_f.columns = S4_045_f.columns.droplevel(0)
S4_045_f = S4_045_f.loc[:, ~S4_045_f.columns.str.contains('^Unnamed')]

S4_05_f=S4_05.pivot(index =S4_05.index, columns ='Unnamed: 0')
S4_05_f=S4_05_f.apply(lambda x: pd.Series(x.dropna().values))
S4_05_f.columns = S4_05_f.columns.droplevel(0)
S4_05_f = S4_05_f.loc[:, ~S4_05_f.columns.str.contains('^Unnamed')]

S4_1_f=S4_1.pivot(index =S4_1.index, columns ='Unnamed: 0')
S4_1_f=S4_1_f.apply(lambda x: pd.Series(x.dropna().values))
S4_1_f.columns = S4_1_f.columns.droplevel(0)
S4_1_f = S4_1_f.loc[:, ~S4_1_f.columns.str.contains('^Unnamed')]

S4_2_f=S4_2.pivot(index =S4_2.index, columns ='Unnamed: 0')
S4_2_f=S4_2_f.apply(lambda x: pd.Series(x.dropna().values))
S4_2_f.columns = S4_2_f.columns.droplevel(0)
S4_2_f = S4_2_f.loc[:, ~S4_2_f.columns.str.contains('^Unnamed')]

S4_3_f=S4_3.pivot(index =S4_3.index, columns ='Unnamed: 0')
S4_3_f=S4_3_f.apply(lambda x: pd.Series(x.dropna().values))
S4_3_f.columns = S4_3_f.columns.droplevel(0)
S4_3_f = S4_3_f.loc[:, ~S4_3_f.columns.str.contains('^Unnamed')]

S4_4_f=S4_4.pivot(index =S4_4.index, columns ='Unnamed: 0')
S4_4_f=S4_4_f.apply(lambda x: pd.Series(x.dropna().values))
S4_4_f.columns = S4_4_f.columns.droplevel(0)
S4_4_f = S4_4_f.loc[:, ~S4_4_f.columns.str.contains('^Unnamed')]

S4_5_f=S4_5.pivot(index =S4_5.index, columns ='Unnamed: 0')
S4_5_f=S4_5_f.apply(lambda x: pd.Series(x.dropna().values))
S4_5_f.columns = S4_5_f.columns.droplevel(0)
S4_5_f = S4_5_f.loc[:, ~S4_5_f.columns.str.contains('^Unnamed')]

S4_6_f=S4_6.pivot(index =S4_6.index, columns ='Unnamed: 0')
S4_6_f=S4_6_f.apply(lambda x: pd.Series(x.dropna().values))
S4_6_f.columns = S4_6_f.columns.droplevel(0)
S4_6_f = S4_6_f.loc[:, ~S4_6_f.columns.str.contains('^Unnamed')]

S4_7_f=S4_7.pivot(index =S4_7.index, columns ='Unnamed: 0')
S4_7_f=S4_7_f.apply(lambda x: pd.Series(x.dropna().values))
S4_7_f.columns = S4_7_f.columns.droplevel(0)
S4_7_f = S4_7_f.loc[:, ~S4_7_f.columns.str.contains('^Unnamed')]

S4_8_f=S4_8.pivot(index =S4_8.index, columns ='Unnamed: 0')
S4_8_f=S4_8_f.apply(lambda x: pd.Series(x.dropna().values))
S4_8_f.columns = S4_8_f.columns.droplevel(0)
S4_8_f = S4_8_f.loc[:, ~S4_8_f.columns.str.contains('^Unnamed')]

S4_9_f=S4_9.pivot(index =S4_9.index, columns ='Unnamed: 0')
S4_9_f=S4_9_f.apply(lambda x: pd.Series(x.dropna().values))
S4_9_f.columns = S4_9_f.columns.droplevel(0)
S4_9_f = S4_9_f.loc[:, ~S4_9_f.columns.str.contains('^Unnamed')]

S4_10_f=S4_10.pivot(index =S4_10.index, columns ='Unnamed: 0')
S4_10_f=S4_10_f.apply(lambda x: pd.Series(x.dropna().values))
S4_10_f.columns = S4_10_f.columns.droplevel(0)
S4_10_f = S4_10_f.loc[:, ~S4_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S4_0_f,S4_005_f,S4_01_f,S4_015_f,S4_02_f,S4_025_f,S4_03_f,S4_035_f,S4_04_f,S4_045_f,S4_05_f,S4_1_f,S4_2_f,S4_3_f,S4_4_f,S4_5_f,S4_6_f,S4_7_f,S4_8_f,S4_9_f,S4_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S4.csv', header=True)