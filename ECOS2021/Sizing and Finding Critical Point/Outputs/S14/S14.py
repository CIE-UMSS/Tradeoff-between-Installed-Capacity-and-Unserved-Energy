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
S14_0=pd.read_csv('S14_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_005=pd.read_csv('S14_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_01=pd.read_csv('S14_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_015=pd.read_csv('S14_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_02=pd.read_csv('S14_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_025=pd.read_csv('S14_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_03=pd.read_csv('S14_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_035=pd.read_csv('S14_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_04=pd.read_csv('S14_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_045=pd.read_csv('S14_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_05=pd.read_csv('S14_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_1=pd.read_csv('S14_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_2=pd.read_csv('S14_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_3=pd.read_csv('S14_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_4=pd.read_csv('S14_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_5=pd.read_csv('S14_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_6=pd.read_csv('S14_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_7=pd.read_csv('S14_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_8=pd.read_csv('S14_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_9=pd.read_csv('S14_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S14_10=pd.read_csv('S14_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S14_0_f=S14_0.pivot(index =S14_005.index, columns ='Unnamed: 0')
S14_0_f=S14_0_f.apply(lambda x: pd.Series(x.dropna().values))
S14_0_f.columns = S14_0_f.columns.droplevel(0)
S14_0_f = S14_0_f.loc[:, ~S14_0_f.columns.str.contains('^Unnamed')]

S14_005_f=S14_005.pivot(index =S14_005.index, columns ='Unnamed: 0')
S14_005_f=S14_005_f.apply(lambda x: pd.Series(x.dropna().values))
S14_005_f.columns = S14_005_f.columns.droplevel(0)
S14_005_f = S14_005_f.loc[:, ~S14_005_f.columns.str.contains('^Unnamed')]

S14_01_f=S14_01.pivot(index =S14_01.index, columns ='Unnamed: 0')
S14_01_f=S14_01_f.apply(lambda x: pd.Series(x.dropna().values))
S14_01_f.columns = S14_01_f.columns.droplevel(0)
S14_01_f = S14_01_f.loc[:, ~S14_01_f.columns.str.contains('^Unnamed')]

S14_015_f=S14_015.pivot(index =S14_015.index, columns ='Unnamed: 0')
S14_015_f=S14_015_f.apply(lambda x: pd.Series(x.dropna().values))
S14_015_f.columns = S14_015_f.columns.droplevel(0)
S14_015_f = S14_015_f.loc[:, ~S14_015_f.columns.str.contains('^Unnamed')]

S14_02_f=S14_02.pivot(index =S14_02.index, columns ='Unnamed: 0')
S14_02_f=S14_02_f.apply(lambda x: pd.Series(x.dropna().values))
S14_02_f.columns = S14_02_f.columns.droplevel(0)
S14_02_f = S14_02_f.loc[:, ~S14_02_f.columns.str.contains('^Unnamed')]

S14_025_f=S14_025.pivot(index =S14_025.index, columns ='Unnamed: 0')
S14_025_f=S14_025_f.apply(lambda x: pd.Series(x.dropna().values))
S14_025_f.columns = S14_025_f.columns.droplevel(0)
S14_025_f = S14_025_f.loc[:, ~S14_025_f.columns.str.contains('^Unnamed')]

S14_03_f=S14_03.pivot(index =S14_03.index, columns ='Unnamed: 0')
S14_03_f=S14_03_f.apply(lambda x: pd.Series(x.dropna().values))
S14_03_f.columns = S14_03_f.columns.droplevel(0)
S14_03_f = S14_03_f.loc[:, ~S14_03_f.columns.str.contains('^Unnamed')]

S14_035_f=S14_035.pivot(index =S14_035.index, columns ='Unnamed: 0')
S14_035_f=S14_035_f.apply(lambda x: pd.Series(x.dropna().values))
S14_035_f.columns = S14_035_f.columns.droplevel(0)
S14_035_f = S14_035_f.loc[:, ~S14_035_f.columns.str.contains('^Unnamed')]

S14_04_f=S14_04.pivot(index =S14_04.index, columns ='Unnamed: 0')
S14_04_f=S14_04_f.apply(lambda x: pd.Series(x.dropna().values))
S14_04_f.columns = S14_04_f.columns.droplevel(0)
S14_04_f = S14_04_f.loc[:, ~S14_04_f.columns.str.contains('^Unnamed')]

S14_045_f=S14_045.pivot(index =S14_045.index, columns ='Unnamed: 0')
S14_045_f=S14_045_f.apply(lambda x: pd.Series(x.dropna().values))
S14_045_f.columns = S14_045_f.columns.droplevel(0)
S14_045_f = S14_045_f.loc[:, ~S14_045_f.columns.str.contains('^Unnamed')]

S14_05_f=S14_05.pivot(index =S14_05.index, columns ='Unnamed: 0')
S14_05_f=S14_05_f.apply(lambda x: pd.Series(x.dropna().values))
S14_05_f.columns = S14_05_f.columns.droplevel(0)
S14_05_f = S14_05_f.loc[:, ~S14_05_f.columns.str.contains('^Unnamed')]

S14_1_f=S14_1.pivot(index =S14_1.index, columns ='Unnamed: 0')
S14_1_f=S14_1_f.apply(lambda x: pd.Series(x.dropna().values))
S14_1_f.columns = S14_1_f.columns.droplevel(0)
S14_1_f = S14_1_f.loc[:, ~S14_1_f.columns.str.contains('^Unnamed')]

S14_2_f=S14_2.pivot(index =S14_2.index, columns ='Unnamed: 0')
S14_2_f=S14_2_f.apply(lambda x: pd.Series(x.dropna().values))
S14_2_f.columns = S14_2_f.columns.droplevel(0)
S14_2_f = S14_2_f.loc[:, ~S14_2_f.columns.str.contains('^Unnamed')]

S14_3_f=S14_3.pivot(index =S14_3.index, columns ='Unnamed: 0')
S14_3_f=S14_3_f.apply(lambda x: pd.Series(x.dropna().values))
S14_3_f.columns = S14_3_f.columns.droplevel(0)
S14_3_f = S14_3_f.loc[:, ~S14_3_f.columns.str.contains('^Unnamed')]

S14_4_f=S14_4.pivot(index =S14_4.index, columns ='Unnamed: 0')
S14_4_f=S14_4_f.apply(lambda x: pd.Series(x.dropna().values))
S14_4_f.columns = S14_4_f.columns.droplevel(0)
S14_4_f = S14_4_f.loc[:, ~S14_4_f.columns.str.contains('^Unnamed')]

S14_5_f=S14_5.pivot(index =S14_5.index, columns ='Unnamed: 0')
S14_5_f=S14_5_f.apply(lambda x: pd.Series(x.dropna().values))
S14_5_f.columns = S14_5_f.columns.droplevel(0)
S14_5_f = S14_5_f.loc[:, ~S14_5_f.columns.str.contains('^Unnamed')]

S14_6_f=S14_6.pivot(index =S14_6.index, columns ='Unnamed: 0')
S14_6_f=S14_6_f.apply(lambda x: pd.Series(x.dropna().values))
S14_6_f.columns = S14_6_f.columns.droplevel(0)
S14_6_f = S14_6_f.loc[:, ~S14_6_f.columns.str.contains('^Unnamed')]

S14_7_f=S14_7.pivot(index =S14_7.index, columns ='Unnamed: 0')
S14_7_f=S14_7_f.apply(lambda x: pd.Series(x.dropna().values))
S14_7_f.columns = S14_7_f.columns.droplevel(0)
S14_7_f = S14_7_f.loc[:, ~S14_7_f.columns.str.contains('^Unnamed')]

S14_8_f=S14_8.pivot(index =S14_8.index, columns ='Unnamed: 0')
S14_8_f=S14_8_f.apply(lambda x: pd.Series(x.dropna().values))
S14_8_f.columns = S14_8_f.columns.droplevel(0)
S14_8_f = S14_8_f.loc[:, ~S14_8_f.columns.str.contains('^Unnamed')]

S14_9_f=S14_9.pivot(index =S14_9.index, columns ='Unnamed: 0')
S14_9_f=S14_9_f.apply(lambda x: pd.Series(x.dropna().values))
S14_9_f.columns = S14_9_f.columns.droplevel(0)
S14_9_f = S14_9_f.loc[:, ~S14_9_f.columns.str.contains('^Unnamed')]

S14_10_f=S14_10.pivot(index =S14_10.index, columns ='Unnamed: 0')
S14_10_f=S14_10_f.apply(lambda x: pd.Series(x.dropna().values))
S14_10_f.columns = S14_10_f.columns.droplevel(0)
S14_10_f = S14_10_f.loc[:, ~S14_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S14_0_f,S14_005_f,S14_01_f,S14_015_f,S14_02_f,S14_025_f,S14_03_f,S14_035_f,S14_04_f,S14_045_f,S14_05_f,S14_1_f,S14_2_f,S14_3_f,S14_4_f,S14_5_f,S14_6_f,S14_7_f,S14_8_f,S14_9_f,S14_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S14.csv', header=True)