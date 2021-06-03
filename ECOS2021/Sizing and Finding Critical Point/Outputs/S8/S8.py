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
S8_0=pd.read_csv('S8_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_005=pd.read_csv('S8_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_01=pd.read_csv('S8_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_015=pd.read_csv('S8_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_02=pd.read_csv('S8_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_025=pd.read_csv('S8_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_03=pd.read_csv('S8_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_035=pd.read_csv('S8_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_04=pd.read_csv('S8_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_045=pd.read_csv('S8_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_05=pd.read_csv('S8_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_1=pd.read_csv('S8_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_2=pd.read_csv('S8_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_3=pd.read_csv('S8_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_4=pd.read_csv('S8_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_5=pd.read_csv('S8_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_6=pd.read_csv('S8_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_7=pd.read_csv('S8_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_8=pd.read_csv('S8_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_9=pd.read_csv('S8_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S8_10=pd.read_csv('S8_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S8_0_f=S8_0.pivot(index =S8_005.index, columns ='Unnamed: 0')
S8_0_f=S8_0_f.apply(lambda x: pd.Series(x.dropna().values))
S8_0_f.columns = S8_0_f.columns.droplevel(0)
S8_0_f = S8_0_f.loc[:, ~S8_0_f.columns.str.contains('^Unnamed')]

S8_005_f=S8_005.pivot(index =S8_005.index, columns ='Unnamed: 0')
S8_005_f=S8_005_f.apply(lambda x: pd.Series(x.dropna().values))
S8_005_f.columns = S8_005_f.columns.droplevel(0)
S8_005_f = S8_005_f.loc[:, ~S8_005_f.columns.str.contains('^Unnamed')]

S8_01_f=S8_01.pivot(index =S8_01.index, columns ='Unnamed: 0')
S8_01_f=S8_01_f.apply(lambda x: pd.Series(x.dropna().values))
S8_01_f.columns = S8_01_f.columns.droplevel(0)
S8_01_f = S8_01_f.loc[:, ~S8_01_f.columns.str.contains('^Unnamed')]

S8_015_f=S8_015.pivot(index =S8_015.index, columns ='Unnamed: 0')
S8_015_f=S8_015_f.apply(lambda x: pd.Series(x.dropna().values))
S8_015_f.columns = S8_015_f.columns.droplevel(0)
S8_015_f = S8_015_f.loc[:, ~S8_015_f.columns.str.contains('^Unnamed')]

S8_02_f=S8_02.pivot(index =S8_02.index, columns ='Unnamed: 0')
S8_02_f=S8_02_f.apply(lambda x: pd.Series(x.dropna().values))
S8_02_f.columns = S8_02_f.columns.droplevel(0)
S8_02_f = S8_02_f.loc[:, ~S8_02_f.columns.str.contains('^Unnamed')]

S8_025_f=S8_025.pivot(index =S8_025.index, columns ='Unnamed: 0')
S8_025_f=S8_025_f.apply(lambda x: pd.Series(x.dropna().values))
S8_025_f.columns = S8_025_f.columns.droplevel(0)
S8_025_f = S8_025_f.loc[:, ~S8_025_f.columns.str.contains('^Unnamed')]

S8_03_f=S8_03.pivot(index =S8_03.index, columns ='Unnamed: 0')
S8_03_f=S8_03_f.apply(lambda x: pd.Series(x.dropna().values))
S8_03_f.columns = S8_03_f.columns.droplevel(0)
S8_03_f = S8_03_f.loc[:, ~S8_03_f.columns.str.contains('^Unnamed')]

S8_035_f=S8_035.pivot(index =S8_035.index, columns ='Unnamed: 0')
S8_035_f=S8_035_f.apply(lambda x: pd.Series(x.dropna().values))
S8_035_f.columns = S8_035_f.columns.droplevel(0)
S8_035_f = S8_035_f.loc[:, ~S8_035_f.columns.str.contains('^Unnamed')]

S8_04_f=S8_04.pivot(index =S8_04.index, columns ='Unnamed: 0')
S8_04_f=S8_04_f.apply(lambda x: pd.Series(x.dropna().values))
S8_04_f.columns = S8_04_f.columns.droplevel(0)
S8_04_f = S8_04_f.loc[:, ~S8_04_f.columns.str.contains('^Unnamed')]

S8_045_f=S8_045.pivot(index =S8_045.index, columns ='Unnamed: 0')
S8_045_f=S8_045_f.apply(lambda x: pd.Series(x.dropna().values))
S8_045_f.columns = S8_045_f.columns.droplevel(0)
S8_045_f = S8_045_f.loc[:, ~S8_045_f.columns.str.contains('^Unnamed')]

S8_05_f=S8_05.pivot(index =S8_05.index, columns ='Unnamed: 0')
S8_05_f=S8_05_f.apply(lambda x: pd.Series(x.dropna().values))
S8_05_f.columns = S8_05_f.columns.droplevel(0)
S8_05_f = S8_05_f.loc[:, ~S8_05_f.columns.str.contains('^Unnamed')]

S8_1_f=S8_1.pivot(index =S8_1.index, columns ='Unnamed: 0')
S8_1_f=S8_1_f.apply(lambda x: pd.Series(x.dropna().values))
S8_1_f.columns = S8_1_f.columns.droplevel(0)
S8_1_f = S8_1_f.loc[:, ~S8_1_f.columns.str.contains('^Unnamed')]

S8_2_f=S8_2.pivot(index =S8_2.index, columns ='Unnamed: 0')
S8_2_f=S8_2_f.apply(lambda x: pd.Series(x.dropna().values))
S8_2_f.columns = S8_2_f.columns.droplevel(0)
S8_2_f = S8_2_f.loc[:, ~S8_2_f.columns.str.contains('^Unnamed')]

S8_3_f=S8_3.pivot(index =S8_3.index, columns ='Unnamed: 0')
S8_3_f=S8_3_f.apply(lambda x: pd.Series(x.dropna().values))
S8_3_f.columns = S8_3_f.columns.droplevel(0)
S8_3_f = S8_3_f.loc[:, ~S8_3_f.columns.str.contains('^Unnamed')]

S8_4_f=S8_4.pivot(index =S8_4.index, columns ='Unnamed: 0')
S8_4_f=S8_4_f.apply(lambda x: pd.Series(x.dropna().values))
S8_4_f.columns = S8_4_f.columns.droplevel(0)
S8_4_f = S8_4_f.loc[:, ~S8_4_f.columns.str.contains('^Unnamed')]

S8_5_f=S8_5.pivot(index =S8_5.index, columns ='Unnamed: 0')
S8_5_f=S8_5_f.apply(lambda x: pd.Series(x.dropna().values))
S8_5_f.columns = S8_5_f.columns.droplevel(0)
S8_5_f = S8_5_f.loc[:, ~S8_5_f.columns.str.contains('^Unnamed')]

S8_6_f=S8_6.pivot(index =S8_6.index, columns ='Unnamed: 0')
S8_6_f=S8_6_f.apply(lambda x: pd.Series(x.dropna().values))
S8_6_f.columns = S8_6_f.columns.droplevel(0)
S8_6_f = S8_6_f.loc[:, ~S8_6_f.columns.str.contains('^Unnamed')]

S8_7_f=S8_7.pivot(index =S8_7.index, columns ='Unnamed: 0')
S8_7_f=S8_7_f.apply(lambda x: pd.Series(x.dropna().values))
S8_7_f.columns = S8_7_f.columns.droplevel(0)
S8_7_f = S8_7_f.loc[:, ~S8_7_f.columns.str.contains('^Unnamed')]

S8_8_f=S8_8.pivot(index =S8_8.index, columns ='Unnamed: 0')
S8_8_f=S8_8_f.apply(lambda x: pd.Series(x.dropna().values))
S8_8_f.columns = S8_8_f.columns.droplevel(0)
S8_8_f = S8_8_f.loc[:, ~S8_8_f.columns.str.contains('^Unnamed')]

S8_9_f=S8_9.pivot(index =S8_9.index, columns ='Unnamed: 0')
S8_9_f=S8_9_f.apply(lambda x: pd.Series(x.dropna().values))
S8_9_f.columns = S8_9_f.columns.droplevel(0)
S8_9_f = S8_9_f.loc[:, ~S8_9_f.columns.str.contains('^Unnamed')]

S8_10_f=S8_10.pivot(index =S8_10.index, columns ='Unnamed: 0')
S8_10_f=S8_10_f.apply(lambda x: pd.Series(x.dropna().values))
S8_10_f.columns = S8_10_f.columns.droplevel(0)
S8_10_f = S8_10_f.loc[:, ~S8_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S8_0_f,S8_005_f,S8_01_f,S8_015_f,S8_02_f,S8_025_f,S8_03_f,S8_035_f,S8_04_f,S8_045_f,S8_05_f,S8_1_f,S8_2_f,S8_3_f,S8_4_f,S8_5_f,S8_6_f,S8_7_f,S8_8_f,S8_9_f,S8_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S8.csv', header=True)