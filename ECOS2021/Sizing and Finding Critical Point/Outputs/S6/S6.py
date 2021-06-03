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
S6_0=pd.read_csv('S6_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_005=pd.read_csv('S6_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_01=pd.read_csv('S6_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_015=pd.read_csv('S6_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_02=pd.read_csv('S6_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_025=pd.read_csv('S6_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_03=pd.read_csv('S6_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_035=pd.read_csv('S6_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_04=pd.read_csv('S6_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_045=pd.read_csv('S6_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_05=pd.read_csv('S6_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_1=pd.read_csv('S6_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_2=pd.read_csv('S6_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_3=pd.read_csv('S6_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_4=pd.read_csv('S6_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_5=pd.read_csv('S6_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_6=pd.read_csv('S6_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_7=pd.read_csv('S6_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_8=pd.read_csv('S6_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_9=pd.read_csv('S6_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S6_10=pd.read_csv('S6_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S6_0_f=S6_0.pivot(index =S6_005.index, columns ='Unnamed: 0')
S6_0_f=S6_0_f.apply(lambda x: pd.Series(x.dropna().values))
S6_0_f.columns = S6_0_f.columns.droplevel(0)
S6_0_f = S6_0_f.loc[:, ~S6_0_f.columns.str.contains('^Unnamed')]

S6_005_f=S6_005.pivot(index =S6_005.index, columns ='Unnamed: 0')
S6_005_f=S6_005_f.apply(lambda x: pd.Series(x.dropna().values))
S6_005_f.columns = S6_005_f.columns.droplevel(0)
S6_005_f = S6_005_f.loc[:, ~S6_005_f.columns.str.contains('^Unnamed')]

S6_01_f=S6_01.pivot(index =S6_01.index, columns ='Unnamed: 0')
S6_01_f=S6_01_f.apply(lambda x: pd.Series(x.dropna().values))
S6_01_f.columns = S6_01_f.columns.droplevel(0)
S6_01_f = S6_01_f.loc[:, ~S6_01_f.columns.str.contains('^Unnamed')]

S6_015_f=S6_015.pivot(index =S6_015.index, columns ='Unnamed: 0')
S6_015_f=S6_015_f.apply(lambda x: pd.Series(x.dropna().values))
S6_015_f.columns = S6_015_f.columns.droplevel(0)
S6_015_f = S6_015_f.loc[:, ~S6_015_f.columns.str.contains('^Unnamed')]

S6_02_f=S6_02.pivot(index =S6_02.index, columns ='Unnamed: 0')
S6_02_f=S6_02_f.apply(lambda x: pd.Series(x.dropna().values))
S6_02_f.columns = S6_02_f.columns.droplevel(0)
S6_02_f = S6_02_f.loc[:, ~S6_02_f.columns.str.contains('^Unnamed')]

S6_025_f=S6_025.pivot(index =S6_025.index, columns ='Unnamed: 0')
S6_025_f=S6_025_f.apply(lambda x: pd.Series(x.dropna().values))
S6_025_f.columns = S6_025_f.columns.droplevel(0)
S6_025_f = S6_025_f.loc[:, ~S6_025_f.columns.str.contains('^Unnamed')]

S6_03_f=S6_03.pivot(index =S6_03.index, columns ='Unnamed: 0')
S6_03_f=S6_03_f.apply(lambda x: pd.Series(x.dropna().values))
S6_03_f.columns = S6_03_f.columns.droplevel(0)
S6_03_f = S6_03_f.loc[:, ~S6_03_f.columns.str.contains('^Unnamed')]

S6_035_f=S6_035.pivot(index =S6_035.index, columns ='Unnamed: 0')
S6_035_f=S6_035_f.apply(lambda x: pd.Series(x.dropna().values))
S6_035_f.columns = S6_035_f.columns.droplevel(0)
S6_035_f = S6_035_f.loc[:, ~S6_035_f.columns.str.contains('^Unnamed')]

S6_04_f=S6_04.pivot(index =S6_04.index, columns ='Unnamed: 0')
S6_04_f=S6_04_f.apply(lambda x: pd.Series(x.dropna().values))
S6_04_f.columns = S6_04_f.columns.droplevel(0)
S6_04_f = S6_04_f.loc[:, ~S6_04_f.columns.str.contains('^Unnamed')]

S6_045_f=S6_045.pivot(index =S6_045.index, columns ='Unnamed: 0')
S6_045_f=S6_045_f.apply(lambda x: pd.Series(x.dropna().values))
S6_045_f.columns = S6_045_f.columns.droplevel(0)
S6_045_f = S6_045_f.loc[:, ~S6_045_f.columns.str.contains('^Unnamed')]

S6_05_f=S6_05.pivot(index =S6_05.index, columns ='Unnamed: 0')
S6_05_f=S6_05_f.apply(lambda x: pd.Series(x.dropna().values))
S6_05_f.columns = S6_05_f.columns.droplevel(0)
S6_05_f = S6_05_f.loc[:, ~S6_05_f.columns.str.contains('^Unnamed')]

S6_1_f=S6_1.pivot(index =S6_1.index, columns ='Unnamed: 0')
S6_1_f=S6_1_f.apply(lambda x: pd.Series(x.dropna().values))
S6_1_f.columns = S6_1_f.columns.droplevel(0)
S6_1_f = S6_1_f.loc[:, ~S6_1_f.columns.str.contains('^Unnamed')]

S6_2_f=S6_2.pivot(index =S6_2.index, columns ='Unnamed: 0')
S6_2_f=S6_2_f.apply(lambda x: pd.Series(x.dropna().values))
S6_2_f.columns = S6_2_f.columns.droplevel(0)
S6_2_f = S6_2_f.loc[:, ~S6_2_f.columns.str.contains('^Unnamed')]

S6_3_f=S6_3.pivot(index =S6_3.index, columns ='Unnamed: 0')
S6_3_f=S6_3_f.apply(lambda x: pd.Series(x.dropna().values))
S6_3_f.columns = S6_3_f.columns.droplevel(0)
S6_3_f = S6_3_f.loc[:, ~S6_3_f.columns.str.contains('^Unnamed')]

S6_4_f=S6_4.pivot(index =S6_4.index, columns ='Unnamed: 0')
S6_4_f=S6_4_f.apply(lambda x: pd.Series(x.dropna().values))
S6_4_f.columns = S6_4_f.columns.droplevel(0)
S6_4_f = S6_4_f.loc[:, ~S6_4_f.columns.str.contains('^Unnamed')]

S6_5_f=S6_5.pivot(index =S6_5.index, columns ='Unnamed: 0')
S6_5_f=S6_5_f.apply(lambda x: pd.Series(x.dropna().values))
S6_5_f.columns = S6_5_f.columns.droplevel(0)
S6_5_f = S6_5_f.loc[:, ~S6_5_f.columns.str.contains('^Unnamed')]

S6_6_f=S6_6.pivot(index =S6_6.index, columns ='Unnamed: 0')
S6_6_f=S6_6_f.apply(lambda x: pd.Series(x.dropna().values))
S6_6_f.columns = S6_6_f.columns.droplevel(0)
S6_6_f = S6_6_f.loc[:, ~S6_6_f.columns.str.contains('^Unnamed')]

S6_7_f=S6_7.pivot(index =S6_7.index, columns ='Unnamed: 0')
S6_7_f=S6_7_f.apply(lambda x: pd.Series(x.dropna().values))
S6_7_f.columns = S6_7_f.columns.droplevel(0)
S6_7_f = S6_7_f.loc[:, ~S6_7_f.columns.str.contains('^Unnamed')]

S6_8_f=S6_8.pivot(index =S6_8.index, columns ='Unnamed: 0')
S6_8_f=S6_8_f.apply(lambda x: pd.Series(x.dropna().values))
S6_8_f.columns = S6_8_f.columns.droplevel(0)
S6_8_f = S6_8_f.loc[:, ~S6_8_f.columns.str.contains('^Unnamed')]

S6_9_f=S6_9.pivot(index =S6_9.index, columns ='Unnamed: 0')
S6_9_f=S6_9_f.apply(lambda x: pd.Series(x.dropna().values))
S6_9_f.columns = S6_9_f.columns.droplevel(0)
S6_9_f = S6_9_f.loc[:, ~S6_9_f.columns.str.contains('^Unnamed')]

S6_10_f=S6_10.pivot(index =S6_10.index, columns ='Unnamed: 0')
S6_10_f=S6_10_f.apply(lambda x: pd.Series(x.dropna().values))
S6_10_f.columns = S6_10_f.columns.droplevel(0)
S6_10_f = S6_10_f.loc[:, ~S6_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S6_0_f,S6_005_f,S6_01_f,S6_015_f,S6_02_f,S6_025_f,S6_03_f,S6_035_f,S6_04_f,S6_045_f,S6_05_f,S6_1_f,S6_2_f,S6_3_f,S6_4_f,S6_5_f,S6_6_f,S6_7_f,S6_8_f,S6_9_f,S6_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S6.csv', header=True)