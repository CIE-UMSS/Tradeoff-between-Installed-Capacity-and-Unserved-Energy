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
S10_0=pd.read_csv('S10_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_005=pd.read_csv('S10_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_01=pd.read_csv('S10_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_015=pd.read_csv('S10_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_02=pd.read_csv('S10_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_025=pd.read_csv('S10_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_03=pd.read_csv('S10_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_035=pd.read_csv('S10_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_04=pd.read_csv('S10_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_045=pd.read_csv('S10_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_05=pd.read_csv('S10_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_1=pd.read_csv('S10_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_2=pd.read_csv('S10_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_3=pd.read_csv('S10_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_4=pd.read_csv('S10_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_5=pd.read_csv('S10_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_6=pd.read_csv('S10_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_7=pd.read_csv('S10_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_8=pd.read_csv('S10_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_9=pd.read_csv('S10_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S10_10=pd.read_csv('S10_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S10_0_f=S10_0.pivot(index =S10_005.index, columns ='Unnamed: 0')
S10_0_f=S10_0_f.apply(lambda x: pd.Series(x.dropna().values))
S10_0_f.columns = S10_0_f.columns.droplevel(0)
S10_0_f = S10_0_f.loc[:, ~S10_0_f.columns.str.contains('^Unnamed')]

S10_005_f=S10_005.pivot(index =S10_005.index, columns ='Unnamed: 0')
S10_005_f=S10_005_f.apply(lambda x: pd.Series(x.dropna().values))
S10_005_f.columns = S10_005_f.columns.droplevel(0)
S10_005_f = S10_005_f.loc[:, ~S10_005_f.columns.str.contains('^Unnamed')]

S10_01_f=S10_01.pivot(index =S10_01.index, columns ='Unnamed: 0')
S10_01_f=S10_01_f.apply(lambda x: pd.Series(x.dropna().values))
S10_01_f.columns = S10_01_f.columns.droplevel(0)
S10_01_f = S10_01_f.loc[:, ~S10_01_f.columns.str.contains('^Unnamed')]

S10_015_f=S10_015.pivot(index =S10_015.index, columns ='Unnamed: 0')
S10_015_f=S10_015_f.apply(lambda x: pd.Series(x.dropna().values))
S10_015_f.columns = S10_015_f.columns.droplevel(0)
S10_015_f = S10_015_f.loc[:, ~S10_015_f.columns.str.contains('^Unnamed')]

S10_02_f=S10_02.pivot(index =S10_02.index, columns ='Unnamed: 0')
S10_02_f=S10_02_f.apply(lambda x: pd.Series(x.dropna().values))
S10_02_f.columns = S10_02_f.columns.droplevel(0)
S10_02_f = S10_02_f.loc[:, ~S10_02_f.columns.str.contains('^Unnamed')]

S10_025_f=S10_025.pivot(index =S10_025.index, columns ='Unnamed: 0')
S10_025_f=S10_025_f.apply(lambda x: pd.Series(x.dropna().values))
S10_025_f.columns = S10_025_f.columns.droplevel(0)
S10_025_f = S10_025_f.loc[:, ~S10_025_f.columns.str.contains('^Unnamed')]

S10_03_f=S10_03.pivot(index =S10_03.index, columns ='Unnamed: 0')
S10_03_f=S10_03_f.apply(lambda x: pd.Series(x.dropna().values))
S10_03_f.columns = S10_03_f.columns.droplevel(0)
S10_03_f = S10_03_f.loc[:, ~S10_03_f.columns.str.contains('^Unnamed')]

S10_035_f=S10_035.pivot(index =S10_035.index, columns ='Unnamed: 0')
S10_035_f=S10_035_f.apply(lambda x: pd.Series(x.dropna().values))
S10_035_f.columns = S10_035_f.columns.droplevel(0)
S10_035_f = S10_035_f.loc[:, ~S10_035_f.columns.str.contains('^Unnamed')]

S10_04_f=S10_04.pivot(index =S10_04.index, columns ='Unnamed: 0')
S10_04_f=S10_04_f.apply(lambda x: pd.Series(x.dropna().values))
S10_04_f.columns = S10_04_f.columns.droplevel(0)
S10_04_f = S10_04_f.loc[:, ~S10_04_f.columns.str.contains('^Unnamed')]

S10_045_f=S10_045.pivot(index =S10_045.index, columns ='Unnamed: 0')
S10_045_f=S10_045_f.apply(lambda x: pd.Series(x.dropna().values))
S10_045_f.columns = S10_045_f.columns.droplevel(0)
S10_045_f = S10_045_f.loc[:, ~S10_045_f.columns.str.contains('^Unnamed')]

S10_05_f=S10_05.pivot(index =S10_05.index, columns ='Unnamed: 0')
S10_05_f=S10_05_f.apply(lambda x: pd.Series(x.dropna().values))
S10_05_f.columns = S10_05_f.columns.droplevel(0)
S10_05_f = S10_05_f.loc[:, ~S10_05_f.columns.str.contains('^Unnamed')]

S10_1_f=S10_1.pivot(index =S10_1.index, columns ='Unnamed: 0')
S10_1_f=S10_1_f.apply(lambda x: pd.Series(x.dropna().values))
S10_1_f.columns = S10_1_f.columns.droplevel(0)
S10_1_f = S10_1_f.loc[:, ~S10_1_f.columns.str.contains('^Unnamed')]

S10_2_f=S10_2.pivot(index =S10_2.index, columns ='Unnamed: 0')
S10_2_f=S10_2_f.apply(lambda x: pd.Series(x.dropna().values))
S10_2_f.columns = S10_2_f.columns.droplevel(0)
S10_2_f = S10_2_f.loc[:, ~S10_2_f.columns.str.contains('^Unnamed')]

S10_3_f=S10_3.pivot(index =S10_3.index, columns ='Unnamed: 0')
S10_3_f=S10_3_f.apply(lambda x: pd.Series(x.dropna().values))
S10_3_f.columns = S10_3_f.columns.droplevel(0)
S10_3_f = S10_3_f.loc[:, ~S10_3_f.columns.str.contains('^Unnamed')]

S10_4_f=S10_4.pivot(index =S10_4.index, columns ='Unnamed: 0')
S10_4_f=S10_4_f.apply(lambda x: pd.Series(x.dropna().values))
S10_4_f.columns = S10_4_f.columns.droplevel(0)
S10_4_f = S10_4_f.loc[:, ~S10_4_f.columns.str.contains('^Unnamed')]

S10_5_f=S10_5.pivot(index =S10_5.index, columns ='Unnamed: 0')
S10_5_f=S10_5_f.apply(lambda x: pd.Series(x.dropna().values))
S10_5_f.columns = S10_5_f.columns.droplevel(0)
S10_5_f = S10_5_f.loc[:, ~S10_5_f.columns.str.contains('^Unnamed')]

S10_6_f=S10_6.pivot(index =S10_6.index, columns ='Unnamed: 0')
S10_6_f=S10_6_f.apply(lambda x: pd.Series(x.dropna().values))
S10_6_f.columns = S10_6_f.columns.droplevel(0)
S10_6_f = S10_6_f.loc[:, ~S10_6_f.columns.str.contains('^Unnamed')]

S10_7_f=S10_7.pivot(index =S10_7.index, columns ='Unnamed: 0')
S10_7_f=S10_7_f.apply(lambda x: pd.Series(x.dropna().values))
S10_7_f.columns = S10_7_f.columns.droplevel(0)
S10_7_f = S10_7_f.loc[:, ~S10_7_f.columns.str.contains('^Unnamed')]

S10_8_f=S10_8.pivot(index =S10_8.index, columns ='Unnamed: 0')
S10_8_f=S10_8_f.apply(lambda x: pd.Series(x.dropna().values))
S10_8_f.columns = S10_8_f.columns.droplevel(0)
S10_8_f = S10_8_f.loc[:, ~S10_8_f.columns.str.contains('^Unnamed')]

S10_9_f=S10_9.pivot(index =S10_9.index, columns ='Unnamed: 0')
S10_9_f=S10_9_f.apply(lambda x: pd.Series(x.dropna().values))
S10_9_f.columns = S10_9_f.columns.droplevel(0)
S10_9_f = S10_9_f.loc[:, ~S10_9_f.columns.str.contains('^Unnamed')]

S10_10_f=S10_10.pivot(index =S10_10.index, columns ='Unnamed: 0')
S10_10_f=S10_10_f.apply(lambda x: pd.Series(x.dropna().values))
S10_10_f.columns = S10_10_f.columns.droplevel(0)
S10_10_f = S10_10_f.loc[:, ~S10_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S10_0_f,S10_005_f,S10_01_f,S10_015_f,S10_02_f,S10_025_f,S10_03_f,S10_035_f,S10_04_f,S10_045_f,S10_05_f,S10_1_f,S10_2_f,S10_3_f,S10_4_f,S10_5_f,S10_6_f,S10_7_f,S10_8_f,S10_9_f,S10_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S10.csv', header=True)