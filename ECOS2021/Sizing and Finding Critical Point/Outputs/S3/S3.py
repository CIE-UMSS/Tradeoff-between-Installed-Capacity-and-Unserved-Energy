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
S3_0=pd.read_csv('S3_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_005=pd.read_csv('S3_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_01=pd.read_csv('S3_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_015=pd.read_csv('S3_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_02=pd.read_csv('S3_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_025=pd.read_csv('S3_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_03=pd.read_csv('S3_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_035=pd.read_csv('S3_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_04=pd.read_csv('S3_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_045=pd.read_csv('S3_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_05=pd.read_csv('S3_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_1=pd.read_csv('S3_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_2=pd.read_csv('S3_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_3=pd.read_csv('S3_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_4=pd.read_csv('S3_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_5=pd.read_csv('S3_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_6=pd.read_csv('S3_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_7=pd.read_csv('S3_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_8=pd.read_csv('S3_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_9=pd.read_csv('S3_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
S3_10=pd.read_csv('S3_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

S3_0_f=S3_0.pivot(index =S3_005.index, columns ='Unnamed: 0')
S3_0_f=S3_0_f.apply(lambda x: pd.Series(x.dropna().values))
S3_0_f.columns = S3_0_f.columns.droplevel(0)
S3_0_f = S3_0_f.loc[:, ~S3_0_f.columns.str.contains('^Unnamed')]

S3_005_f=S3_005.pivot(index =S3_005.index, columns ='Unnamed: 0')
S3_005_f=S3_005_f.apply(lambda x: pd.Series(x.dropna().values))
S3_005_f.columns = S3_005_f.columns.droplevel(0)
S3_005_f = S3_005_f.loc[:, ~S3_005_f.columns.str.contains('^Unnamed')]

S3_01_f=S3_01.pivot(index =S3_01.index, columns ='Unnamed: 0')
S3_01_f=S3_01_f.apply(lambda x: pd.Series(x.dropna().values))
S3_01_f.columns = S3_01_f.columns.droplevel(0)
S3_01_f = S3_01_f.loc[:, ~S3_01_f.columns.str.contains('^Unnamed')]

S3_015_f=S3_015.pivot(index =S3_015.index, columns ='Unnamed: 0')
S3_015_f=S3_015_f.apply(lambda x: pd.Series(x.dropna().values))
S3_015_f.columns = S3_015_f.columns.droplevel(0)
S3_015_f = S3_015_f.loc[:, ~S3_015_f.columns.str.contains('^Unnamed')]

S3_02_f=S3_02.pivot(index =S3_02.index, columns ='Unnamed: 0')
S3_02_f=S3_02_f.apply(lambda x: pd.Series(x.dropna().values))
S3_02_f.columns = S3_02_f.columns.droplevel(0)
S3_02_f = S3_02_f.loc[:, ~S3_02_f.columns.str.contains('^Unnamed')]

S3_025_f=S3_025.pivot(index =S3_025.index, columns ='Unnamed: 0')
S3_025_f=S3_025_f.apply(lambda x: pd.Series(x.dropna().values))
S3_025_f.columns = S3_025_f.columns.droplevel(0)
S3_025_f = S3_025_f.loc[:, ~S3_025_f.columns.str.contains('^Unnamed')]

S3_03_f=S3_03.pivot(index =S3_03.index, columns ='Unnamed: 0')
S3_03_f=S3_03_f.apply(lambda x: pd.Series(x.dropna().values))
S3_03_f.columns = S3_03_f.columns.droplevel(0)
S3_03_f = S3_03_f.loc[:, ~S3_03_f.columns.str.contains('^Unnamed')]

S3_035_f=S3_035.pivot(index =S3_035.index, columns ='Unnamed: 0')
S3_035_f=S3_035_f.apply(lambda x: pd.Series(x.dropna().values))
S3_035_f.columns = S3_035_f.columns.droplevel(0)
S3_035_f = S3_035_f.loc[:, ~S3_035_f.columns.str.contains('^Unnamed')]

S3_04_f=S3_04.pivot(index =S3_04.index, columns ='Unnamed: 0')
S3_04_f=S3_04_f.apply(lambda x: pd.Series(x.dropna().values))
S3_04_f.columns = S3_04_f.columns.droplevel(0)
S3_04_f = S3_04_f.loc[:, ~S3_04_f.columns.str.contains('^Unnamed')]

S3_045_f=S3_045.pivot(index =S3_045.index, columns ='Unnamed: 0')
S3_045_f=S3_045_f.apply(lambda x: pd.Series(x.dropna().values))
S3_045_f.columns = S3_045_f.columns.droplevel(0)
S3_045_f = S3_045_f.loc[:, ~S3_045_f.columns.str.contains('^Unnamed')]

S3_05_f=S3_05.pivot(index =S3_05.index, columns ='Unnamed: 0')
S3_05_f=S3_05_f.apply(lambda x: pd.Series(x.dropna().values))
S3_05_f.columns = S3_05_f.columns.droplevel(0)
S3_05_f = S3_05_f.loc[:, ~S3_05_f.columns.str.contains('^Unnamed')]

S3_1_f=S3_1.pivot(index =S3_1.index, columns ='Unnamed: 0')
S3_1_f=S3_1_f.apply(lambda x: pd.Series(x.dropna().values))
S3_1_f.columns = S3_1_f.columns.droplevel(0)
S3_1_f = S3_1_f.loc[:, ~S3_1_f.columns.str.contains('^Unnamed')]

S3_2_f=S3_2.pivot(index =S3_2.index, columns ='Unnamed: 0')
S3_2_f=S3_2_f.apply(lambda x: pd.Series(x.dropna().values))
S3_2_f.columns = S3_2_f.columns.droplevel(0)
S3_2_f = S3_2_f.loc[:, ~S3_2_f.columns.str.contains('^Unnamed')]

S3_3_f=S3_3.pivot(index =S3_3.index, columns ='Unnamed: 0')
S3_3_f=S3_3_f.apply(lambda x: pd.Series(x.dropna().values))
S3_3_f.columns = S3_3_f.columns.droplevel(0)
S3_3_f = S3_3_f.loc[:, ~S3_3_f.columns.str.contains('^Unnamed')]

S3_4_f=S3_4.pivot(index =S3_4.index, columns ='Unnamed: 0')
S3_4_f=S3_4_f.apply(lambda x: pd.Series(x.dropna().values))
S3_4_f.columns = S3_4_f.columns.droplevel(0)
S3_4_f = S3_4_f.loc[:, ~S3_4_f.columns.str.contains('^Unnamed')]

S3_5_f=S3_5.pivot(index =S3_5.index, columns ='Unnamed: 0')
S3_5_f=S3_5_f.apply(lambda x: pd.Series(x.dropna().values))
S3_5_f.columns = S3_5_f.columns.droplevel(0)
S3_5_f = S3_5_f.loc[:, ~S3_5_f.columns.str.contains('^Unnamed')]

S3_6_f=S3_6.pivot(index =S3_6.index, columns ='Unnamed: 0')
S3_6_f=S3_6_f.apply(lambda x: pd.Series(x.dropna().values))
S3_6_f.columns = S3_6_f.columns.droplevel(0)
S3_6_f = S3_6_f.loc[:, ~S3_6_f.columns.str.contains('^Unnamed')]

S3_7_f=S3_7.pivot(index =S3_7.index, columns ='Unnamed: 0')
S3_7_f=S3_7_f.apply(lambda x: pd.Series(x.dropna().values))
S3_7_f.columns = S3_7_f.columns.droplevel(0)
S3_7_f = S3_7_f.loc[:, ~S3_7_f.columns.str.contains('^Unnamed')]

S3_8_f=S3_8.pivot(index =S3_8.index, columns ='Unnamed: 0')
S3_8_f=S3_8_f.apply(lambda x: pd.Series(x.dropna().values))
S3_8_f.columns = S3_8_f.columns.droplevel(0)
S3_8_f = S3_8_f.loc[:, ~S3_8_f.columns.str.contains('^Unnamed')]

S3_9_f=S3_9.pivot(index =S3_9.index, columns ='Unnamed: 0')
S3_9_f=S3_9_f.apply(lambda x: pd.Series(x.dropna().values))
S3_9_f.columns = S3_9_f.columns.droplevel(0)
S3_9_f = S3_9_f.loc[:, ~S3_9_f.columns.str.contains('^Unnamed')]

S3_10_f=S3_10.pivot(index =S3_10.index, columns ='Unnamed: 0')
S3_10_f=S3_10_f.apply(lambda x: pd.Series(x.dropna().values))
S3_10_f.columns = S3_10_f.columns.droplevel(0)
S3_10_f = S3_10_f.loc[:, ~S3_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([S3_0_f,S3_005_f,S3_01_f,S3_015_f,S3_02_f,S3_025_f,S3_03_f,S3_035_f,S3_04_f,S3_045_f,S3_05_f,S3_1_f,S3_2_f,S3_3_f,S3_4_f,S3_5_f,S3_6_f,S3_7_f,S3_8_f,S3_9_f,S3_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('S3.csv', header=True)