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
S1_0=pd.read_csv('S1_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_005=pd.read_csv('S1_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_01=pd.read_csv('S1_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_015=pd.read_csv('S1_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_02=pd.read_csv('S1_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_025=pd.read_csv('S1_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_03=pd.read_csv('S1_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_035=pd.read_csv('S1_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_04=pd.read_csv('S1_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_045=pd.read_csv('S1_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_05=pd.read_csv('S1_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_1=pd.read_csv('S1_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_2=pd.read_csv('S1_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_3=pd.read_csv('S1_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_4=pd.read_csv('S1_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_5=pd.read_csv('S1_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_6=pd.read_csv('S1_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_7=pd.read_csv('S1_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_8=pd.read_csv('S1_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_9=pd.read_csv('S1_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S1_10=pd.read_csv('S1_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S1_0_f=S1_0.pivot(index =S1_005.index, columns ='Unnamed: 0')
S1_0_f=S1_0_f.apply(lambda x: pd.Series(x.dropna().values))
S1_0_f.columns = S1_0_f.columns.droplevel(0)
S1_0_f = S1_0_f.loc[:, ~S1_0_f.columns.str.contains('^Unnamed')]

S1_005_f=S1_005.pivot(index =S1_005.index, columns ='Unnamed: 0')
S1_005_f=S1_005_f.apply(lambda x: pd.Series(x.dropna().values))
S1_005_f.columns = S1_005_f.columns.droplevel(0)
S1_005_f = S1_005_f.loc[:, ~S1_005_f.columns.str.contains('^Unnamed')]

S1_01_f=S1_01.pivot(index =S1_01.index, columns ='Unnamed: 0')
S1_01_f=S1_01_f.apply(lambda x: pd.Series(x.dropna().values))
S1_01_f.columns = S1_01_f.columns.droplevel(0)
S1_01_f = S1_01_f.loc[:, ~S1_01_f.columns.str.contains('^Unnamed')]

S1_015_f=S1_015.pivot(index =S1_015.index, columns ='Unnamed: 0')
S1_015_f=S1_015_f.apply(lambda x: pd.Series(x.dropna().values))
S1_015_f.columns = S1_015_f.columns.droplevel(0)
S1_015_f = S1_015_f.loc[:, ~S1_015_f.columns.str.contains('^Unnamed')]

S1_02_f=S1_02.pivot(index =S1_02.index, columns ='Unnamed: 0')
S1_02_f=S1_02_f.apply(lambda x: pd.Series(x.dropna().values))
S1_02_f.columns = S1_02_f.columns.droplevel(0)
S1_02_f = S1_02_f.loc[:, ~S1_02_f.columns.str.contains('^Unnamed')]

S1_025_f=S1_025.pivot(index =S1_025.index, columns ='Unnamed: 0')
S1_025_f=S1_025_f.apply(lambda x: pd.Series(x.dropna().values))
S1_025_f.columns = S1_025_f.columns.droplevel(0)
S1_025_f = S1_025_f.loc[:, ~S1_025_f.columns.str.contains('^Unnamed')]

S1_03_f=S1_03.pivot(index =S1_03.index, columns ='Unnamed: 0')
S1_03_f=S1_03_f.apply(lambda x: pd.Series(x.dropna().values))
S1_03_f.columns = S1_03_f.columns.droplevel(0)
S1_03_f = S1_03_f.loc[:, ~S1_03_f.columns.str.contains('^Unnamed')]

S1_035_f=S1_035.pivot(index =S1_035.index, columns ='Unnamed: 0')
S1_035_f=S1_035_f.apply(lambda x: pd.Series(x.dropna().values))
S1_035_f.columns = S1_035_f.columns.droplevel(0)
S1_035_f = S1_035_f.loc[:, ~S1_035_f.columns.str.contains('^Unnamed')]

S1_04_f=S1_04.pivot(index =S1_04.index, columns ='Unnamed: 0')
S1_04_f=S1_04_f.apply(lambda x: pd.Series(x.dropna().values))
S1_04_f.columns = S1_04_f.columns.droplevel(0)
S1_04_f = S1_04_f.loc[:, ~S1_04_f.columns.str.contains('^Unnamed')]

S1_045_f=S1_045.pivot(index =S1_045.index, columns ='Unnamed: 0')
S1_045_f=S1_045_f.apply(lambda x: pd.Series(x.dropna().values))
S1_045_f.columns = S1_045_f.columns.droplevel(0)
S1_045_f = S1_045_f.loc[:, ~S1_045_f.columns.str.contains('^Unnamed')]

S1_05_f=S1_05.pivot(index =S1_05.index, columns ='Unnamed: 0')
S1_05_f=S1_05_f.apply(lambda x: pd.Series(x.dropna().values))
S1_05_f.columns = S1_05_f.columns.droplevel(0)
S1_05_f = S1_05_f.loc[:, ~S1_05_f.columns.str.contains('^Unnamed')]

S1_1_f=S1_1.pivot(index =S1_1.index, columns ='Unnamed: 0')
S1_1_f=S1_1_f.apply(lambda x: pd.Series(x.dropna().values))
S1_1_f.columns = S1_1_f.columns.droplevel(0)
S1_1_f = S1_1_f.loc[:, ~S1_1_f.columns.str.contains('^Unnamed')]

S1_2_f=S1_2.pivot(index =S1_2.index, columns ='Unnamed: 0')
S1_2_f=S1_2_f.apply(lambda x: pd.Series(x.dropna().values))
S1_2_f.columns = S1_2_f.columns.droplevel(0)
S1_2_f = S1_2_f.loc[:, ~S1_2_f.columns.str.contains('^Unnamed')]

S1_3_f=S1_3.pivot(index =S1_3.index, columns ='Unnamed: 0')
S1_3_f=S1_3_f.apply(lambda x: pd.Series(x.dropna().values))
S1_3_f.columns = S1_3_f.columns.droplevel(0)
S1_3_f = S1_3_f.loc[:, ~S1_3_f.columns.str.contains('^Unnamed')]

S1_4_f=S1_4.pivot(index =S1_4.index, columns ='Unnamed: 0')
S1_4_f=S1_4_f.apply(lambda x: pd.Series(x.dropna().values))
S1_4_f.columns = S1_4_f.columns.droplevel(0)
S1_4_f = S1_4_f.loc[:, ~S1_4_f.columns.str.contains('^Unnamed')]

S1_5_f=S1_5.pivot(index =S1_5.index, columns ='Unnamed: 0')
S1_5_f=S1_5_f.apply(lambda x: pd.Series(x.dropna().values))
S1_5_f.columns = S1_5_f.columns.droplevel(0)
S1_5_f = S1_5_f.loc[:, ~S1_5_f.columns.str.contains('^Unnamed')]

S1_6_f=S1_6.pivot(index =S1_6.index, columns ='Unnamed: 0')
S1_6_f=S1_6_f.apply(lambda x: pd.Series(x.dropna().values))
S1_6_f.columns = S1_6_f.columns.droplevel(0)
S1_6_f = S1_6_f.loc[:, ~S1_6_f.columns.str.contains('^Unnamed')]

S1_7_f=S1_7.pivot(index =S1_7.index, columns ='Unnamed: 0')
S1_7_f=S1_7_f.apply(lambda x: pd.Series(x.dropna().values))
S1_7_f.columns = S1_7_f.columns.droplevel(0)
S1_7_f = S1_7_f.loc[:, ~S1_7_f.columns.str.contains('^Unnamed')]

S1_8_f=S1_8.pivot(index =S1_8.index, columns ='Unnamed: 0')
S1_8_f=S1_8_f.apply(lambda x: pd.Series(x.dropna().values))
S1_8_f.columns = S1_8_f.columns.droplevel(0)
S1_8_f = S1_8_f.loc[:, ~S1_8_f.columns.str.contains('^Unnamed')]

S1_9_f=S1_9.pivot(index =S1_9.index, columns ='Unnamed: 0')
S1_9_f=S1_9_f.apply(lambda x: pd.Series(x.dropna().values))
S1_9_f.columns = S1_9_f.columns.droplevel(0)
S1_9_f = S1_9_f.loc[:, ~S1_9_f.columns.str.contains('^Unnamed')]

S1_10_f=S1_10.pivot(index =S1_10.index, columns ='Unnamed: 0')
S1_10_f=S1_10_f.apply(lambda x: pd.Series(x.dropna().values))
S1_10_f.columns = S1_10_f.columns.droplevel(0)
S1_10_f = S1_10_f.loc[:, ~S1_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S1_0_f,S1_005_f,S1_01_f,S1_015_f,S1_02_f,S1_025_f,S1_03_f,S1_035_f,S1_04_f,S1_045_f,S1_05_f,S1_1_f,S1_2_f,S1_3_f,S1_4_f,S1_5_f,S1_6_f,S1_7_f,S1_8_f,S1_9_f,S1_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S1.csv', header=True)