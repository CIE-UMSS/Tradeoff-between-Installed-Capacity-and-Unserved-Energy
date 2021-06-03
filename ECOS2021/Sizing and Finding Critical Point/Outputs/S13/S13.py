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
S13_0=pd.read_csv('S13_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_005=pd.read_csv('S13_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_01=pd.read_csv('S13_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_015=pd.read_csv('S13_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_02=pd.read_csv('S13_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_025=pd.read_csv('S13_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_03=pd.read_csv('S13_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_035=pd.read_csv('S13_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_04=pd.read_csv('S13_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_045=pd.read_csv('S13_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_05=pd.read_csv('S13_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_1=pd.read_csv('S13_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_2=pd.read_csv('S13_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_3=pd.read_csv('S13_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_4=pd.read_csv('S13_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_5=pd.read_csv('S13_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_6=pd.read_csv('S13_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_7=pd.read_csv('S13_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_8=pd.read_csv('S13_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_9=pd.read_csv('S13_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S13_10=pd.read_csv('S13_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S13_0_f=S13_0.pivot(index =S13_005.index, columns ='Unnamed: 0')
S13_0_f=S13_0_f.apply(lambda x: pd.Series(x.dropna().values))
S13_0_f.columns = S13_0_f.columns.droplevel(0)
S13_0_f = S13_0_f.loc[:, ~S13_0_f.columns.str.contains('^Unnamed')]

S13_005_f=S13_005.pivot(index =S13_005.index, columns ='Unnamed: 0')
S13_005_f=S13_005_f.apply(lambda x: pd.Series(x.dropna().values))
S13_005_f.columns = S13_005_f.columns.droplevel(0)
S13_005_f = S13_005_f.loc[:, ~S13_005_f.columns.str.contains('^Unnamed')]

S13_01_f=S13_01.pivot(index =S13_01.index, columns ='Unnamed: 0')
S13_01_f=S13_01_f.apply(lambda x: pd.Series(x.dropna().values))
S13_01_f.columns = S13_01_f.columns.droplevel(0)
S13_01_f = S13_01_f.loc[:, ~S13_01_f.columns.str.contains('^Unnamed')]

S13_015_f=S13_015.pivot(index =S13_015.index, columns ='Unnamed: 0')
S13_015_f=S13_015_f.apply(lambda x: pd.Series(x.dropna().values))
S13_015_f.columns = S13_015_f.columns.droplevel(0)
S13_015_f = S13_015_f.loc[:, ~S13_015_f.columns.str.contains('^Unnamed')]

S13_02_f=S13_02.pivot(index =S13_02.index, columns ='Unnamed: 0')
S13_02_f=S13_02_f.apply(lambda x: pd.Series(x.dropna().values))
S13_02_f.columns = S13_02_f.columns.droplevel(0)
S13_02_f = S13_02_f.loc[:, ~S13_02_f.columns.str.contains('^Unnamed')]

S13_025_f=S13_025.pivot(index =S13_025.index, columns ='Unnamed: 0')
S13_025_f=S13_025_f.apply(lambda x: pd.Series(x.dropna().values))
S13_025_f.columns = S13_025_f.columns.droplevel(0)
S13_025_f = S13_025_f.loc[:, ~S13_025_f.columns.str.contains('^Unnamed')]

S13_03_f=S13_03.pivot(index =S13_03.index, columns ='Unnamed: 0')
S13_03_f=S13_03_f.apply(lambda x: pd.Series(x.dropna().values))
S13_03_f.columns = S13_03_f.columns.droplevel(0)
S13_03_f = S13_03_f.loc[:, ~S13_03_f.columns.str.contains('^Unnamed')]

S13_035_f=S13_035.pivot(index =S13_035.index, columns ='Unnamed: 0')
S13_035_f=S13_035_f.apply(lambda x: pd.Series(x.dropna().values))
S13_035_f.columns = S13_035_f.columns.droplevel(0)
S13_035_f = S13_035_f.loc[:, ~S13_035_f.columns.str.contains('^Unnamed')]

S13_04_f=S13_04.pivot(index =S13_04.index, columns ='Unnamed: 0')
S13_04_f=S13_04_f.apply(lambda x: pd.Series(x.dropna().values))
S13_04_f.columns = S13_04_f.columns.droplevel(0)
S13_04_f = S13_04_f.loc[:, ~S13_04_f.columns.str.contains('^Unnamed')]

S13_045_f=S13_045.pivot(index =S13_045.index, columns ='Unnamed: 0')
S13_045_f=S13_045_f.apply(lambda x: pd.Series(x.dropna().values))
S13_045_f.columns = S13_045_f.columns.droplevel(0)
S13_045_f = S13_045_f.loc[:, ~S13_045_f.columns.str.contains('^Unnamed')]

S13_05_f=S13_05.pivot(index =S13_05.index, columns ='Unnamed: 0')
S13_05_f=S13_05_f.apply(lambda x: pd.Series(x.dropna().values))
S13_05_f.columns = S13_05_f.columns.droplevel(0)
S13_05_f = S13_05_f.loc[:, ~S13_05_f.columns.str.contains('^Unnamed')]

S13_1_f=S13_1.pivot(index =S13_1.index, columns ='Unnamed: 0')
S13_1_f=S13_1_f.apply(lambda x: pd.Series(x.dropna().values))
S13_1_f.columns = S13_1_f.columns.droplevel(0)
S13_1_f = S13_1_f.loc[:, ~S13_1_f.columns.str.contains('^Unnamed')]

S13_2_f=S13_2.pivot(index =S13_2.index, columns ='Unnamed: 0')
S13_2_f=S13_2_f.apply(lambda x: pd.Series(x.dropna().values))
S13_2_f.columns = S13_2_f.columns.droplevel(0)
S13_2_f = S13_2_f.loc[:, ~S13_2_f.columns.str.contains('^Unnamed')]

S13_3_f=S13_3.pivot(index =S13_3.index, columns ='Unnamed: 0')
S13_3_f=S13_3_f.apply(lambda x: pd.Series(x.dropna().values))
S13_3_f.columns = S13_3_f.columns.droplevel(0)
S13_3_f = S13_3_f.loc[:, ~S13_3_f.columns.str.contains('^Unnamed')]

S13_4_f=S13_4.pivot(index =S13_4.index, columns ='Unnamed: 0')
S13_4_f=S13_4_f.apply(lambda x: pd.Series(x.dropna().values))
S13_4_f.columns = S13_4_f.columns.droplevel(0)
S13_4_f = S13_4_f.loc[:, ~S13_4_f.columns.str.contains('^Unnamed')]

S13_5_f=S13_5.pivot(index =S13_5.index, columns ='Unnamed: 0')
S13_5_f=S13_5_f.apply(lambda x: pd.Series(x.dropna().values))
S13_5_f.columns = S13_5_f.columns.droplevel(0)
S13_5_f = S13_5_f.loc[:, ~S13_5_f.columns.str.contains('^Unnamed')]

S13_6_f=S13_6.pivot(index =S13_6.index, columns ='Unnamed: 0')
S13_6_f=S13_6_f.apply(lambda x: pd.Series(x.dropna().values))
S13_6_f.columns = S13_6_f.columns.droplevel(0)
S13_6_f = S13_6_f.loc[:, ~S13_6_f.columns.str.contains('^Unnamed')]

S13_7_f=S13_7.pivot(index =S13_7.index, columns ='Unnamed: 0')
S13_7_f=S13_7_f.apply(lambda x: pd.Series(x.dropna().values))
S13_7_f.columns = S13_7_f.columns.droplevel(0)
S13_7_f = S13_7_f.loc[:, ~S13_7_f.columns.str.contains('^Unnamed')]

S13_8_f=S13_8.pivot(index =S13_8.index, columns ='Unnamed: 0')
S13_8_f=S13_8_f.apply(lambda x: pd.Series(x.dropna().values))
S13_8_f.columns = S13_8_f.columns.droplevel(0)
S13_8_f = S13_8_f.loc[:, ~S13_8_f.columns.str.contains('^Unnamed')]

S13_9_f=S13_9.pivot(index =S13_9.index, columns ='Unnamed: 0')
S13_9_f=S13_9_f.apply(lambda x: pd.Series(x.dropna().values))
S13_9_f.columns = S13_9_f.columns.droplevel(0)
S13_9_f = S13_9_f.loc[:, ~S13_9_f.columns.str.contains('^Unnamed')]

S13_10_f=S13_10.pivot(index =S13_10.index, columns ='Unnamed: 0')
S13_10_f=S13_10_f.apply(lambda x: pd.Series(x.dropna().values))
S13_10_f.columns = S13_10_f.columns.droplevel(0)
S13_10_f = S13_10_f.loc[:, ~S13_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S13_0_f,S13_005_f,S13_01_f,S13_015_f,S13_02_f,S13_025_f,S13_03_f,S13_035_f,S13_04_f,S13_045_f,S13_05_f,S13_1_f,S13_2_f,S13_3_f,S13_4_f,S13_5_f,S13_6_f,S13_7_f,S13_8_f,S13_9_f,S13_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S13.csv', header=True)