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
S15_0=pd.read_csv('S15_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_005=pd.read_csv('S15_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_01=pd.read_csv('S15_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_015=pd.read_csv('S15_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_02=pd.read_csv('S15_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_025=pd.read_csv('S15_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_03=pd.read_csv('S15_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_035=pd.read_csv('S15_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_04=pd.read_csv('S15_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_045=pd.read_csv('S15_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_05=pd.read_csv('S15_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_1=pd.read_csv('S15_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_2=pd.read_csv('S15_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_3=pd.read_csv('S15_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_4=pd.read_csv('S15_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_5=pd.read_csv('S15_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_6=pd.read_csv('S15_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_7=pd.read_csv('S15_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_8=pd.read_csv('S15_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_9=pd.read_csv('S15_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S15_10=pd.read_csv('S15_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S15_0_f=S15_0.pivot(index =S15_005.index, columns ='Unnamed: 0')
S15_0_f=S15_0_f.apply(lambda x: pd.Series(x.dropna().values))
S15_0_f.columns = S15_0_f.columns.droplevel(0)
S15_0_f = S15_0_f.loc[:, ~S15_0_f.columns.str.contains('^Unnamed')]

S15_005_f=S15_005.pivot(index =S15_005.index, columns ='Unnamed: 0')
S15_005_f=S15_005_f.apply(lambda x: pd.Series(x.dropna().values))
S15_005_f.columns = S15_005_f.columns.droplevel(0)
S15_005_f = S15_005_f.loc[:, ~S15_005_f.columns.str.contains('^Unnamed')]

S15_01_f=S15_01.pivot(index =S15_01.index, columns ='Unnamed: 0')
S15_01_f=S15_01_f.apply(lambda x: pd.Series(x.dropna().values))
S15_01_f.columns = S15_01_f.columns.droplevel(0)
S15_01_f = S15_01_f.loc[:, ~S15_01_f.columns.str.contains('^Unnamed')]

S15_015_f=S15_015.pivot(index =S15_015.index, columns ='Unnamed: 0')
S15_015_f=S15_015_f.apply(lambda x: pd.Series(x.dropna().values))
S15_015_f.columns = S15_015_f.columns.droplevel(0)
S15_015_f = S15_015_f.loc[:, ~S15_015_f.columns.str.contains('^Unnamed')]

S15_02_f=S15_02.pivot(index =S15_02.index, columns ='Unnamed: 0')
S15_02_f=S15_02_f.apply(lambda x: pd.Series(x.dropna().values))
S15_02_f.columns = S15_02_f.columns.droplevel(0)
S15_02_f = S15_02_f.loc[:, ~S15_02_f.columns.str.contains('^Unnamed')]

S15_025_f=S15_025.pivot(index =S15_025.index, columns ='Unnamed: 0')
S15_025_f=S15_025_f.apply(lambda x: pd.Series(x.dropna().values))
S15_025_f.columns = S15_025_f.columns.droplevel(0)
S15_025_f = S15_025_f.loc[:, ~S15_025_f.columns.str.contains('^Unnamed')]

S15_03_f=S15_03.pivot(index =S15_03.index, columns ='Unnamed: 0')
S15_03_f=S15_03_f.apply(lambda x: pd.Series(x.dropna().values))
S15_03_f.columns = S15_03_f.columns.droplevel(0)
S15_03_f = S15_03_f.loc[:, ~S15_03_f.columns.str.contains('^Unnamed')]

S15_035_f=S15_035.pivot(index =S15_035.index, columns ='Unnamed: 0')
S15_035_f=S15_035_f.apply(lambda x: pd.Series(x.dropna().values))
S15_035_f.columns = S15_035_f.columns.droplevel(0)
S15_035_f = S15_035_f.loc[:, ~S15_035_f.columns.str.contains('^Unnamed')]

S15_04_f=S15_04.pivot(index =S15_04.index, columns ='Unnamed: 0')
S15_04_f=S15_04_f.apply(lambda x: pd.Series(x.dropna().values))
S15_04_f.columns = S15_04_f.columns.droplevel(0)
S15_04_f = S15_04_f.loc[:, ~S15_04_f.columns.str.contains('^Unnamed')]

S15_045_f=S15_045.pivot(index =S15_045.index, columns ='Unnamed: 0')
S15_045_f=S15_045_f.apply(lambda x: pd.Series(x.dropna().values))
S15_045_f.columns = S15_045_f.columns.droplevel(0)
S15_045_f = S15_045_f.loc[:, ~S15_045_f.columns.str.contains('^Unnamed')]

S15_05_f=S15_05.pivot(index =S15_05.index, columns ='Unnamed: 0')
S15_05_f=S15_05_f.apply(lambda x: pd.Series(x.dropna().values))
S15_05_f.columns = S15_05_f.columns.droplevel(0)
S15_05_f = S15_05_f.loc[:, ~S15_05_f.columns.str.contains('^Unnamed')]

S15_1_f=S15_1.pivot(index =S15_1.index, columns ='Unnamed: 0')
S15_1_f=S15_1_f.apply(lambda x: pd.Series(x.dropna().values))
S15_1_f.columns = S15_1_f.columns.droplevel(0)
S15_1_f = S15_1_f.loc[:, ~S15_1_f.columns.str.contains('^Unnamed')]

S15_2_f=S15_2.pivot(index =S15_2.index, columns ='Unnamed: 0')
S15_2_f=S15_2_f.apply(lambda x: pd.Series(x.dropna().values))
S15_2_f.columns = S15_2_f.columns.droplevel(0)
S15_2_f = S15_2_f.loc[:, ~S15_2_f.columns.str.contains('^Unnamed')]

S15_3_f=S15_3.pivot(index =S15_3.index, columns ='Unnamed: 0')
S15_3_f=S15_3_f.apply(lambda x: pd.Series(x.dropna().values))
S15_3_f.columns = S15_3_f.columns.droplevel(0)
S15_3_f = S15_3_f.loc[:, ~S15_3_f.columns.str.contains('^Unnamed')]

S15_4_f=S15_4.pivot(index =S15_4.index, columns ='Unnamed: 0')
S15_4_f=S15_4_f.apply(lambda x: pd.Series(x.dropna().values))
S15_4_f.columns = S15_4_f.columns.droplevel(0)
S15_4_f = S15_4_f.loc[:, ~S15_4_f.columns.str.contains('^Unnamed')]

S15_5_f=S15_5.pivot(index =S15_5.index, columns ='Unnamed: 0')
S15_5_f=S15_5_f.apply(lambda x: pd.Series(x.dropna().values))
S15_5_f.columns = S15_5_f.columns.droplevel(0)
S15_5_f = S15_5_f.loc[:, ~S15_5_f.columns.str.contains('^Unnamed')]

S15_6_f=S15_6.pivot(index =S15_6.index, columns ='Unnamed: 0')
S15_6_f=S15_6_f.apply(lambda x: pd.Series(x.dropna().values))
S15_6_f.columns = S15_6_f.columns.droplevel(0)
S15_6_f = S15_6_f.loc[:, ~S15_6_f.columns.str.contains('^Unnamed')]

S15_7_f=S15_7.pivot(index =S15_7.index, columns ='Unnamed: 0')
S15_7_f=S15_7_f.apply(lambda x: pd.Series(x.dropna().values))
S15_7_f.columns = S15_7_f.columns.droplevel(0)
S15_7_f = S15_7_f.loc[:, ~S15_7_f.columns.str.contains('^Unnamed')]

S15_8_f=S15_8.pivot(index =S15_8.index, columns ='Unnamed: 0')
S15_8_f=S15_8_f.apply(lambda x: pd.Series(x.dropna().values))
S15_8_f.columns = S15_8_f.columns.droplevel(0)
S15_8_f = S15_8_f.loc[:, ~S15_8_f.columns.str.contains('^Unnamed')]

S15_9_f=S15_9.pivot(index =S15_9.index, columns ='Unnamed: 0')
S15_9_f=S15_9_f.apply(lambda x: pd.Series(x.dropna().values))
S15_9_f.columns = S15_9_f.columns.droplevel(0)
S15_9_f = S15_9_f.loc[:, ~S15_9_f.columns.str.contains('^Unnamed')]

S15_10_f=S15_10.pivot(index =S15_10.index, columns ='Unnamed: 0')
S15_10_f=S15_10_f.apply(lambda x: pd.Series(x.dropna().values))
S15_10_f.columns = S15_10_f.columns.droplevel(0)
S15_10_f = S15_10_f.loc[:, ~S15_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S15_0_f,S15_005_f,S15_01_f,S15_015_f,S15_02_f,S15_025_f,S15_03_f,S15_035_f,S15_04_f,S15_045_f,S15_05_f,S15_1_f,S15_2_f,S15_3_f,S15_4_f,S15_5_f,S15_6_f,S15_7_f,S15_8_f,S15_9_f,S15_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S15.csv', header=True)