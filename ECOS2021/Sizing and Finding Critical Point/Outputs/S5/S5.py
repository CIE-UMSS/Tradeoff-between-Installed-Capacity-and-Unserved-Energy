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
S5_0=pd.read_csv('S5_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_005=pd.read_csv('S5_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_01=pd.read_csv('S5_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_015=pd.read_csv('S5_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_02=pd.read_csv('S5_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_025=pd.read_csv('S5_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_03=pd.read_csv('S5_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_035=pd.read_csv('S5_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_04=pd.read_csv('S5_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_045=pd.read_csv('S5_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_05=pd.read_csv('S5_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_1=pd.read_csv('S5_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_2=pd.read_csv('S5_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_3=pd.read_csv('S5_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_4=pd.read_csv('S5_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_5=pd.read_csv('S5_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_6=pd.read_csv('S5_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_7=pd.read_csv('S5_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_8=pd.read_csv('S5_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_9=pd.read_csv('S5_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S5_10=pd.read_csv('S5_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S5_0_f=S5_0.pivot(index =S5_005.index, columns ='Unnamed: 0')
S5_0_f=S5_0_f.apply(lambda x: pd.Series(x.dropna().values))
S5_0_f.columns = S5_0_f.columns.droplevel(0)
S5_0_f = S5_0_f.loc[:, ~S5_0_f.columns.str.contains('^Unnamed')]

S5_005_f=S5_005.pivot(index =S5_005.index, columns ='Unnamed: 0')
S5_005_f=S5_005_f.apply(lambda x: pd.Series(x.dropna().values))
S5_005_f.columns = S5_005_f.columns.droplevel(0)
S5_005_f = S5_005_f.loc[:, ~S5_005_f.columns.str.contains('^Unnamed')]

S5_01_f=S5_01.pivot(index =S5_01.index, columns ='Unnamed: 0')
S5_01_f=S5_01_f.apply(lambda x: pd.Series(x.dropna().values))
S5_01_f.columns = S5_01_f.columns.droplevel(0)
S5_01_f = S5_01_f.loc[:, ~S5_01_f.columns.str.contains('^Unnamed')]

S5_015_f=S5_015.pivot(index =S5_015.index, columns ='Unnamed: 0')
S5_015_f=S5_015_f.apply(lambda x: pd.Series(x.dropna().values))
S5_015_f.columns = S5_015_f.columns.droplevel(0)
S5_015_f = S5_015_f.loc[:, ~S5_015_f.columns.str.contains('^Unnamed')]

S5_02_f=S5_02.pivot(index =S5_02.index, columns ='Unnamed: 0')
S5_02_f=S5_02_f.apply(lambda x: pd.Series(x.dropna().values))
S5_02_f.columns = S5_02_f.columns.droplevel(0)
S5_02_f = S5_02_f.loc[:, ~S5_02_f.columns.str.contains('^Unnamed')]

S5_025_f=S5_025.pivot(index =S5_025.index, columns ='Unnamed: 0')
S5_025_f=S5_025_f.apply(lambda x: pd.Series(x.dropna().values))
S5_025_f.columns = S5_025_f.columns.droplevel(0)
S5_025_f = S5_025_f.loc[:, ~S5_025_f.columns.str.contains('^Unnamed')]

S5_03_f=S5_03.pivot(index =S5_03.index, columns ='Unnamed: 0')
S5_03_f=S5_03_f.apply(lambda x: pd.Series(x.dropna().values))
S5_03_f.columns = S5_03_f.columns.droplevel(0)
S5_03_f = S5_03_f.loc[:, ~S5_03_f.columns.str.contains('^Unnamed')]

S5_035_f=S5_035.pivot(index =S5_035.index, columns ='Unnamed: 0')
S5_035_f=S5_035_f.apply(lambda x: pd.Series(x.dropna().values))
S5_035_f.columns = S5_035_f.columns.droplevel(0)
S5_035_f = S5_035_f.loc[:, ~S5_035_f.columns.str.contains('^Unnamed')]

S5_04_f=S5_04.pivot(index =S5_04.index, columns ='Unnamed: 0')
S5_04_f=S5_04_f.apply(lambda x: pd.Series(x.dropna().values))
S5_04_f.columns = S5_04_f.columns.droplevel(0)
S5_04_f = S5_04_f.loc[:, ~S5_04_f.columns.str.contains('^Unnamed')]

S5_045_f=S5_045.pivot(index =S5_045.index, columns ='Unnamed: 0')
S5_045_f=S5_045_f.apply(lambda x: pd.Series(x.dropna().values))
S5_045_f.columns = S5_045_f.columns.droplevel(0)
S5_045_f = S5_045_f.loc[:, ~S5_045_f.columns.str.contains('^Unnamed')]

S5_05_f=S5_05.pivot(index =S5_05.index, columns ='Unnamed: 0')
S5_05_f=S5_05_f.apply(lambda x: pd.Series(x.dropna().values))
S5_05_f.columns = S5_05_f.columns.droplevel(0)
S5_05_f = S5_05_f.loc[:, ~S5_05_f.columns.str.contains('^Unnamed')]

S5_1_f=S5_1.pivot(index =S5_1.index, columns ='Unnamed: 0')
S5_1_f=S5_1_f.apply(lambda x: pd.Series(x.dropna().values))
S5_1_f.columns = S5_1_f.columns.droplevel(0)
S5_1_f = S5_1_f.loc[:, ~S5_1_f.columns.str.contains('^Unnamed')]

S5_2_f=S5_2.pivot(index =S5_2.index, columns ='Unnamed: 0')
S5_2_f=S5_2_f.apply(lambda x: pd.Series(x.dropna().values))
S5_2_f.columns = S5_2_f.columns.droplevel(0)
S5_2_f = S5_2_f.loc[:, ~S5_2_f.columns.str.contains('^Unnamed')]

S5_3_f=S5_3.pivot(index =S5_3.index, columns ='Unnamed: 0')
S5_3_f=S5_3_f.apply(lambda x: pd.Series(x.dropna().values))
S5_3_f.columns = S5_3_f.columns.droplevel(0)
S5_3_f = S5_3_f.loc[:, ~S5_3_f.columns.str.contains('^Unnamed')]

S5_4_f=S5_4.pivot(index =S5_4.index, columns ='Unnamed: 0')
S5_4_f=S5_4_f.apply(lambda x: pd.Series(x.dropna().values))
S5_4_f.columns = S5_4_f.columns.droplevel(0)
S5_4_f = S5_4_f.loc[:, ~S5_4_f.columns.str.contains('^Unnamed')]

S5_5_f=S5_5.pivot(index =S5_5.index, columns ='Unnamed: 0')
S5_5_f=S5_5_f.apply(lambda x: pd.Series(x.dropna().values))
S5_5_f.columns = S5_5_f.columns.droplevel(0)
S5_5_f = S5_5_f.loc[:, ~S5_5_f.columns.str.contains('^Unnamed')]

S5_6_f=S5_6.pivot(index =S5_6.index, columns ='Unnamed: 0')
S5_6_f=S5_6_f.apply(lambda x: pd.Series(x.dropna().values))
S5_6_f.columns = S5_6_f.columns.droplevel(0)
S5_6_f = S5_6_f.loc[:, ~S5_6_f.columns.str.contains('^Unnamed')]

S5_7_f=S5_7.pivot(index =S5_7.index, columns ='Unnamed: 0')
S5_7_f=S5_7_f.apply(lambda x: pd.Series(x.dropna().values))
S5_7_f.columns = S5_7_f.columns.droplevel(0)
S5_7_f = S5_7_f.loc[:, ~S5_7_f.columns.str.contains('^Unnamed')]

S5_8_f=S5_8.pivot(index =S5_8.index, columns ='Unnamed: 0')
S5_8_f=S5_8_f.apply(lambda x: pd.Series(x.dropna().values))
S5_8_f.columns = S5_8_f.columns.droplevel(0)
S5_8_f = S5_8_f.loc[:, ~S5_8_f.columns.str.contains('^Unnamed')]

S5_9_f=S5_9.pivot(index =S5_9.index, columns ='Unnamed: 0')
S5_9_f=S5_9_f.apply(lambda x: pd.Series(x.dropna().values))
S5_9_f.columns = S5_9_f.columns.droplevel(0)
S5_9_f = S5_9_f.loc[:, ~S5_9_f.columns.str.contains('^Unnamed')]

S5_10_f=S5_10.pivot(index =S5_10.index, columns ='Unnamed: 0')
S5_10_f=S5_10_f.apply(lambda x: pd.Series(x.dropna().values))
S5_10_f.columns = S5_10_f.columns.droplevel(0)
S5_10_f = S5_10_f.loc[:, ~S5_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S5_0_f,S5_005_f,S5_01_f,S5_015_f,S5_02_f,S5_025_f,S5_03_f,S5_035_f,S5_04_f,S5_045_f,S5_05_f,S5_1_f,S5_2_f,S5_3_f,S5_4_f,S5_5_f,S5_6_f,S5_7_f,S5_8_f,S5_9_f,S5_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S5.csv', header=True)