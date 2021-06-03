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
S12_0=pd.read_csv('S12_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_005=pd.read_csv('S12_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_01=pd.read_csv('S12_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_015=pd.read_csv('S12_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_02=pd.read_csv('S12_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_025=pd.read_csv('S12_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_03=pd.read_csv('S12_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_035=pd.read_csv('S12_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_04=pd.read_csv('S12_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_045=pd.read_csv('S12_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_05=pd.read_csv('S12_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_1=pd.read_csv('S12_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_2=pd.read_csv('S12_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_3=pd.read_csv('S12_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_4=pd.read_csv('S12_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_5=pd.read_csv('S12_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_6=pd.read_csv('S12_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_7=pd.read_csv('S12_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_8=pd.read_csv('S12_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_9=pd.read_csv('S12_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S12_10=pd.read_csv('S12_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S12_0_f=S12_0.pivot(index =S12_005.index, columns ='Unnamed: 0')
S12_0_f=S12_0_f.apply(lambda x: pd.Series(x.dropna().values))
S12_0_f.columns = S12_0_f.columns.droplevel(0)
S12_0_f = S12_0_f.loc[:, ~S12_0_f.columns.str.contains('^Unnamed')]

S12_005_f=S12_005.pivot(index =S12_005.index, columns ='Unnamed: 0')
S12_005_f=S12_005_f.apply(lambda x: pd.Series(x.dropna().values))
S12_005_f.columns = S12_005_f.columns.droplevel(0)
S12_005_f = S12_005_f.loc[:, ~S12_005_f.columns.str.contains('^Unnamed')]

S12_01_f=S12_01.pivot(index =S12_01.index, columns ='Unnamed: 0')
S12_01_f=S12_01_f.apply(lambda x: pd.Series(x.dropna().values))
S12_01_f.columns = S12_01_f.columns.droplevel(0)
S12_01_f = S12_01_f.loc[:, ~S12_01_f.columns.str.contains('^Unnamed')]

S12_015_f=S12_015.pivot(index =S12_015.index, columns ='Unnamed: 0')
S12_015_f=S12_015_f.apply(lambda x: pd.Series(x.dropna().values))
S12_015_f.columns = S12_015_f.columns.droplevel(0)
S12_015_f = S12_015_f.loc[:, ~S12_015_f.columns.str.contains('^Unnamed')]

S12_02_f=S12_02.pivot(index =S12_02.index, columns ='Unnamed: 0')
S12_02_f=S12_02_f.apply(lambda x: pd.Series(x.dropna().values))
S12_02_f.columns = S12_02_f.columns.droplevel(0)
S12_02_f = S12_02_f.loc[:, ~S12_02_f.columns.str.contains('^Unnamed')]

S12_025_f=S12_025.pivot(index =S12_025.index, columns ='Unnamed: 0')
S12_025_f=S12_025_f.apply(lambda x: pd.Series(x.dropna().values))
S12_025_f.columns = S12_025_f.columns.droplevel(0)
S12_025_f = S12_025_f.loc[:, ~S12_025_f.columns.str.contains('^Unnamed')]

S12_03_f=S12_03.pivot(index =S12_03.index, columns ='Unnamed: 0')
S12_03_f=S12_03_f.apply(lambda x: pd.Series(x.dropna().values))
S12_03_f.columns = S12_03_f.columns.droplevel(0)
S12_03_f = S12_03_f.loc[:, ~S12_03_f.columns.str.contains('^Unnamed')]

S12_035_f=S12_035.pivot(index =S12_035.index, columns ='Unnamed: 0')
S12_035_f=S12_035_f.apply(lambda x: pd.Series(x.dropna().values))
S12_035_f.columns = S12_035_f.columns.droplevel(0)
S12_035_f = S12_035_f.loc[:, ~S12_035_f.columns.str.contains('^Unnamed')]

S12_04_f=S12_04.pivot(index =S12_04.index, columns ='Unnamed: 0')
S12_04_f=S12_04_f.apply(lambda x: pd.Series(x.dropna().values))
S12_04_f.columns = S12_04_f.columns.droplevel(0)
S12_04_f = S12_04_f.loc[:, ~S12_04_f.columns.str.contains('^Unnamed')]

S12_045_f=S12_045.pivot(index =S12_045.index, columns ='Unnamed: 0')
S12_045_f=S12_045_f.apply(lambda x: pd.Series(x.dropna().values))
S12_045_f.columns = S12_045_f.columns.droplevel(0)
S12_045_f = S12_045_f.loc[:, ~S12_045_f.columns.str.contains('^Unnamed')]

S12_05_f=S12_05.pivot(index =S12_05.index, columns ='Unnamed: 0')
S12_05_f=S12_05_f.apply(lambda x: pd.Series(x.dropna().values))
S12_05_f.columns = S12_05_f.columns.droplevel(0)
S12_05_f = S12_05_f.loc[:, ~S12_05_f.columns.str.contains('^Unnamed')]

S12_1_f=S12_1.pivot(index =S12_1.index, columns ='Unnamed: 0')
S12_1_f=S12_1_f.apply(lambda x: pd.Series(x.dropna().values))
S12_1_f.columns = S12_1_f.columns.droplevel(0)
S12_1_f = S12_1_f.loc[:, ~S12_1_f.columns.str.contains('^Unnamed')]

S12_2_f=S12_2.pivot(index =S12_2.index, columns ='Unnamed: 0')
S12_2_f=S12_2_f.apply(lambda x: pd.Series(x.dropna().values))
S12_2_f.columns = S12_2_f.columns.droplevel(0)
S12_2_f = S12_2_f.loc[:, ~S12_2_f.columns.str.contains('^Unnamed')]

S12_3_f=S12_3.pivot(index =S12_3.index, columns ='Unnamed: 0')
S12_3_f=S12_3_f.apply(lambda x: pd.Series(x.dropna().values))
S12_3_f.columns = S12_3_f.columns.droplevel(0)
S12_3_f = S12_3_f.loc[:, ~S12_3_f.columns.str.contains('^Unnamed')]

S12_4_f=S12_4.pivot(index =S12_4.index, columns ='Unnamed: 0')
S12_4_f=S12_4_f.apply(lambda x: pd.Series(x.dropna().values))
S12_4_f.columns = S12_4_f.columns.droplevel(0)
S12_4_f = S12_4_f.loc[:, ~S12_4_f.columns.str.contains('^Unnamed')]

S12_5_f=S12_5.pivot(index =S12_5.index, columns ='Unnamed: 0')
S12_5_f=S12_5_f.apply(lambda x: pd.Series(x.dropna().values))
S12_5_f.columns = S12_5_f.columns.droplevel(0)
S12_5_f = S12_5_f.loc[:, ~S12_5_f.columns.str.contains('^Unnamed')]

S12_6_f=S12_6.pivot(index =S12_6.index, columns ='Unnamed: 0')
S12_6_f=S12_6_f.apply(lambda x: pd.Series(x.dropna().values))
S12_6_f.columns = S12_6_f.columns.droplevel(0)
S12_6_f = S12_6_f.loc[:, ~S12_6_f.columns.str.contains('^Unnamed')]

S12_7_f=S12_7.pivot(index =S12_7.index, columns ='Unnamed: 0')
S12_7_f=S12_7_f.apply(lambda x: pd.Series(x.dropna().values))
S12_7_f.columns = S12_7_f.columns.droplevel(0)
S12_7_f = S12_7_f.loc[:, ~S12_7_f.columns.str.contains('^Unnamed')]

S12_8_f=S12_8.pivot(index =S12_8.index, columns ='Unnamed: 0')
S12_8_f=S12_8_f.apply(lambda x: pd.Series(x.dropna().values))
S12_8_f.columns = S12_8_f.columns.droplevel(0)
S12_8_f = S12_8_f.loc[:, ~S12_8_f.columns.str.contains('^Unnamed')]

S12_9_f=S12_9.pivot(index =S12_9.index, columns ='Unnamed: 0')
S12_9_f=S12_9_f.apply(lambda x: pd.Series(x.dropna().values))
S12_9_f.columns = S12_9_f.columns.droplevel(0)
S12_9_f = S12_9_f.loc[:, ~S12_9_f.columns.str.contains('^Unnamed')]

S12_10_f=S12_10.pivot(index =S12_10.index, columns ='Unnamed: 0')
S12_10_f=S12_10_f.apply(lambda x: pd.Series(x.dropna().values))
S12_10_f.columns = S12_10_f.columns.droplevel(0)
S12_10_f = S12_10_f.loc[:, ~S12_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S12_0_f,S12_005_f,S12_01_f,S12_015_f,S12_02_f,S12_025_f,S12_03_f,S12_035_f,S12_04_f,S12_045_f,S12_05_f,S12_1_f,S12_2_f,S12_3_f,S12_4_f,S12_5_f,S12_6_f,S12_7_f,S12_8_f,S12_9_f,S12_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S12.csv', header=True)