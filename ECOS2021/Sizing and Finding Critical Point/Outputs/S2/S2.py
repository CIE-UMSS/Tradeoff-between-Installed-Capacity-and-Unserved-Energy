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
S2_0=pd.read_csv('S2_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_005=pd.read_csv('S2_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_01=pd.read_csv('S2_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_015=pd.read_csv('S2_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_02=pd.read_csv('S2_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_025=pd.read_csv('S2_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_03=pd.read_csv('S2_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_035=pd.read_csv('S2_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_04=pd.read_csv('S2_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_045=pd.read_csv('S2_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_05=pd.read_csv('S2_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_1=pd.read_csv('S2_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_2=pd.read_csv('S2_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_3=pd.read_csv('S2_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_4=pd.read_csv('S2_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_5=pd.read_csv('S2_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_6=pd.read_csv('S2_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_7=pd.read_csv('S2_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_8=pd.read_csv('S2_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_9=pd.read_csv('S2_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S2_10=pd.read_csv('S2_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S2_0_f=S2_0.pivot(index =S2_005.index, columns ='Unnamed: 0')
S2_0_f=S2_0_f.apply(lambda x: pd.Series(x.dropna().values))
S2_0_f.columns = S2_0_f.columns.droplevel(0)
S2_0_f = S2_0_f.loc[:, ~S2_0_f.columns.str.contains('^Unnamed')]

S2_005_f=S2_005.pivot(index =S2_005.index, columns ='Unnamed: 0')
S2_005_f=S2_005_f.apply(lambda x: pd.Series(x.dropna().values))
S2_005_f.columns = S2_005_f.columns.droplevel(0)
S2_005_f = S2_005_f.loc[:, ~S2_005_f.columns.str.contains('^Unnamed')]

S2_01_f=S2_01.pivot(index =S2_01.index, columns ='Unnamed: 0')
S2_01_f=S2_01_f.apply(lambda x: pd.Series(x.dropna().values))
S2_01_f.columns = S2_01_f.columns.droplevel(0)
S2_01_f = S2_01_f.loc[:, ~S2_01_f.columns.str.contains('^Unnamed')]

S2_015_f=S2_015.pivot(index =S2_015.index, columns ='Unnamed: 0')
S2_015_f=S2_015_f.apply(lambda x: pd.Series(x.dropna().values))
S2_015_f.columns = S2_015_f.columns.droplevel(0)
S2_015_f = S2_015_f.loc[:, ~S2_015_f.columns.str.contains('^Unnamed')]

S2_02_f=S2_02.pivot(index =S2_02.index, columns ='Unnamed: 0')
S2_02_f=S2_02_f.apply(lambda x: pd.Series(x.dropna().values))
S2_02_f.columns = S2_02_f.columns.droplevel(0)
S2_02_f = S2_02_f.loc[:, ~S2_02_f.columns.str.contains('^Unnamed')]

S2_025_f=S2_025.pivot(index =S2_025.index, columns ='Unnamed: 0')
S2_025_f=S2_025_f.apply(lambda x: pd.Series(x.dropna().values))
S2_025_f.columns = S2_025_f.columns.droplevel(0)
S2_025_f = S2_025_f.loc[:, ~S2_025_f.columns.str.contains('^Unnamed')]

S2_03_f=S2_03.pivot(index =S2_03.index, columns ='Unnamed: 0')
S2_03_f=S2_03_f.apply(lambda x: pd.Series(x.dropna().values))
S2_03_f.columns = S2_03_f.columns.droplevel(0)
S2_03_f = S2_03_f.loc[:, ~S2_03_f.columns.str.contains('^Unnamed')]

S2_035_f=S2_035.pivot(index =S2_035.index, columns ='Unnamed: 0')
S2_035_f=S2_035_f.apply(lambda x: pd.Series(x.dropna().values))
S2_035_f.columns = S2_035_f.columns.droplevel(0)
S2_035_f = S2_035_f.loc[:, ~S2_035_f.columns.str.contains('^Unnamed')]

S2_04_f=S2_04.pivot(index =S2_04.index, columns ='Unnamed: 0')
S2_04_f=S2_04_f.apply(lambda x: pd.Series(x.dropna().values))
S2_04_f.columns = S2_04_f.columns.droplevel(0)
S2_04_f = S2_04_f.loc[:, ~S2_04_f.columns.str.contains('^Unnamed')]

S2_045_f=S2_045.pivot(index =S2_045.index, columns ='Unnamed: 0')
S2_045_f=S2_045_f.apply(lambda x: pd.Series(x.dropna().values))
S2_045_f.columns = S2_045_f.columns.droplevel(0)
S2_045_f = S2_045_f.loc[:, ~S2_045_f.columns.str.contains('^Unnamed')]

S2_05_f=S2_05.pivot(index =S2_05.index, columns ='Unnamed: 0')
S2_05_f=S2_05_f.apply(lambda x: pd.Series(x.dropna().values))
S2_05_f.columns = S2_05_f.columns.droplevel(0)
S2_05_f = S2_05_f.loc[:, ~S2_05_f.columns.str.contains('^Unnamed')]

S2_1_f=S2_1.pivot(index =S2_1.index, columns ='Unnamed: 0')
S2_1_f=S2_1_f.apply(lambda x: pd.Series(x.dropna().values))
S2_1_f.columns = S2_1_f.columns.droplevel(0)
S2_1_f = S2_1_f.loc[:, ~S2_1_f.columns.str.contains('^Unnamed')]

S2_2_f=S2_2.pivot(index =S2_2.index, columns ='Unnamed: 0')
S2_2_f=S2_2_f.apply(lambda x: pd.Series(x.dropna().values))
S2_2_f.columns = S2_2_f.columns.droplevel(0)
S2_2_f = S2_2_f.loc[:, ~S2_2_f.columns.str.contains('^Unnamed')]

S2_3_f=S2_3.pivot(index =S2_3.index, columns ='Unnamed: 0')
S2_3_f=S2_3_f.apply(lambda x: pd.Series(x.dropna().values))
S2_3_f.columns = S2_3_f.columns.droplevel(0)
S2_3_f = S2_3_f.loc[:, ~S2_3_f.columns.str.contains('^Unnamed')]

S2_4_f=S2_4.pivot(index =S2_4.index, columns ='Unnamed: 0')
S2_4_f=S2_4_f.apply(lambda x: pd.Series(x.dropna().values))
S2_4_f.columns = S2_4_f.columns.droplevel(0)
S2_4_f = S2_4_f.loc[:, ~S2_4_f.columns.str.contains('^Unnamed')]

S2_5_f=S2_5.pivot(index =S2_5.index, columns ='Unnamed: 0')
S2_5_f=S2_5_f.apply(lambda x: pd.Series(x.dropna().values))
S2_5_f.columns = S2_5_f.columns.droplevel(0)
S2_5_f = S2_5_f.loc[:, ~S2_5_f.columns.str.contains('^Unnamed')]

S2_6_f=S2_6.pivot(index =S2_6.index, columns ='Unnamed: 0')
S2_6_f=S2_6_f.apply(lambda x: pd.Series(x.dropna().values))
S2_6_f.columns = S2_6_f.columns.droplevel(0)
S2_6_f = S2_6_f.loc[:, ~S2_6_f.columns.str.contains('^Unnamed')]

S2_7_f=S2_7.pivot(index =S2_7.index, columns ='Unnamed: 0')
S2_7_f=S2_7_f.apply(lambda x: pd.Series(x.dropna().values))
S2_7_f.columns = S2_7_f.columns.droplevel(0)
S2_7_f = S2_7_f.loc[:, ~S2_7_f.columns.str.contains('^Unnamed')]

S2_8_f=S2_8.pivot(index =S2_8.index, columns ='Unnamed: 0')
S2_8_f=S2_8_f.apply(lambda x: pd.Series(x.dropna().values))
S2_8_f.columns = S2_8_f.columns.droplevel(0)
S2_8_f = S2_8_f.loc[:, ~S2_8_f.columns.str.contains('^Unnamed')]

S2_9_f=S2_9.pivot(index =S2_9.index, columns ='Unnamed: 0')
S2_9_f=S2_9_f.apply(lambda x: pd.Series(x.dropna().values))
S2_9_f.columns = S2_9_f.columns.droplevel(0)
S2_9_f = S2_9_f.loc[:, ~S2_9_f.columns.str.contains('^Unnamed')]

S2_10_f=S2_10.pivot(index =S2_10.index, columns ='Unnamed: 0')
S2_10_f=S2_10_f.apply(lambda x: pd.Series(x.dropna().values))
S2_10_f.columns = S2_10_f.columns.droplevel(0)
S2_10_f = S2_10_f.loc[:, ~S2_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S2_0_f,S2_005_f,S2_01_f,S2_015_f,S2_02_f,S2_025_f,S2_03_f,S2_035_f,S2_04_f,S2_045_f,S2_05_f,S2_1_f,S2_2_f,S2_3_f,S2_4_f,S2_5_f,S2_6_f,S2_7_f,S2_8_f,S2_9_f,S2_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S2.csv', header=True)