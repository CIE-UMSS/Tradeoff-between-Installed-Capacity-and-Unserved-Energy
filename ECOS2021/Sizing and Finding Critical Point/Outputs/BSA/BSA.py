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
BSA_0=pd.read_csv('BSA_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_005=pd.read_csv('BSA_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_01=pd.read_csv('BSA_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_015=pd.read_csv('BSA_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_02=pd.read_csv('BSA_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_025=pd.read_csv('BSA_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_03=pd.read_csv('BSA_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_035=pd.read_csv('BSA_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_04=pd.read_csv('BSA_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_045=pd.read_csv('BSA_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_05=pd.read_csv('BSA_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_1=pd.read_csv('BSA_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_2=pd.read_csv('BSA_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_3=pd.read_csv('BSA_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_4=pd.read_csv('BSA_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_5=pd.read_csv('BSA_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_6=pd.read_csv('BSA_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_7=pd.read_csv('BSA_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_8=pd.read_csv('BSA_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_9=pd.read_csv('BSA_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSA_10=pd.read_csv('BSA_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

BSA_0_f=BSA_0.pivot(index =BSA_005.index, columns ='Unnamed: 0')
BSA_0_f=BSA_0_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_0_f.columns = BSA_0_f.columns.droplevel(0)
BSA_0_f = BSA_0_f.loc[:, ~BSA_0_f.columns.str.contains('^Unnamed')]

BSA_005_f=BSA_005.pivot(index =BSA_005.index, columns ='Unnamed: 0')
BSA_005_f=BSA_005_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_005_f.columns = BSA_005_f.columns.droplevel(0)
BSA_005_f = BSA_005_f.loc[:, ~BSA_005_f.columns.str.contains('^Unnamed')]

BSA_01_f=BSA_01.pivot(index =BSA_01.index, columns ='Unnamed: 0')
BSA_01_f=BSA_01_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_01_f.columns = BSA_01_f.columns.droplevel(0)
BSA_01_f = BSA_01_f.loc[:, ~BSA_01_f.columns.str.contains('^Unnamed')]

BSA_015_f=BSA_015.pivot(index =BSA_015.index, columns ='Unnamed: 0')
BSA_015_f=BSA_015_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_015_f.columns = BSA_015_f.columns.droplevel(0)
BSA_015_f = BSA_015_f.loc[:, ~BSA_015_f.columns.str.contains('^Unnamed')]

BSA_02_f=BSA_02.pivot(index =BSA_02.index, columns ='Unnamed: 0')
BSA_02_f=BSA_02_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_02_f.columns = BSA_02_f.columns.droplevel(0)
BSA_02_f = BSA_02_f.loc[:, ~BSA_02_f.columns.str.contains('^Unnamed')]

BSA_025_f=BSA_025.pivot(index =BSA_025.index, columns ='Unnamed: 0')
BSA_025_f=BSA_025_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_025_f.columns = BSA_025_f.columns.droplevel(0)
BSA_025_f = BSA_025_f.loc[:, ~BSA_025_f.columns.str.contains('^Unnamed')]

BSA_03_f=BSA_03.pivot(index =BSA_03.index, columns ='Unnamed: 0')
BSA_03_f=BSA_03_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_03_f.columns = BSA_03_f.columns.droplevel(0)
BSA_03_f = BSA_03_f.loc[:, ~BSA_03_f.columns.str.contains('^Unnamed')]

BSA_035_f=BSA_035.pivot(index =BSA_035.index, columns ='Unnamed: 0')
BSA_035_f=BSA_035_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_035_f.columns = BSA_035_f.columns.droplevel(0)
BSA_035_f = BSA_035_f.loc[:, ~BSA_035_f.columns.str.contains('^Unnamed')]

BSA_04_f=BSA_04.pivot(index =BSA_04.index, columns ='Unnamed: 0')
BSA_04_f=BSA_04_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_04_f.columns = BSA_04_f.columns.droplevel(0)
BSA_04_f = BSA_04_f.loc[:, ~BSA_04_f.columns.str.contains('^Unnamed')]

BSA_045_f=BSA_045.pivot(index =BSA_045.index, columns ='Unnamed: 0')
BSA_045_f=BSA_045_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_045_f.columns = BSA_045_f.columns.droplevel(0)
BSA_045_f = BSA_045_f.loc[:, ~BSA_045_f.columns.str.contains('^Unnamed')]

BSA_05_f=BSA_05.pivot(index =BSA_05.index, columns ='Unnamed: 0')
BSA_05_f=BSA_05_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_05_f.columns = BSA_05_f.columns.droplevel(0)
BSA_05_f = BSA_05_f.loc[:, ~BSA_05_f.columns.str.contains('^Unnamed')]

BSA_1_f=BSA_1.pivot(index =BSA_1.index, columns ='Unnamed: 0')
BSA_1_f=BSA_1_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_1_f.columns = BSA_1_f.columns.droplevel(0)
BSA_1_f = BSA_1_f.loc[:, ~BSA_1_f.columns.str.contains('^Unnamed')]

BSA_2_f=BSA_2.pivot(index =BSA_2.index, columns ='Unnamed: 0')
BSA_2_f=BSA_2_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_2_f.columns = BSA_2_f.columns.droplevel(0)
BSA_2_f = BSA_2_f.loc[:, ~BSA_2_f.columns.str.contains('^Unnamed')]

BSA_3_f=BSA_3.pivot(index =BSA_3.index, columns ='Unnamed: 0')
BSA_3_f=BSA_3_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_3_f.columns = BSA_3_f.columns.droplevel(0)
BSA_3_f = BSA_3_f.loc[:, ~BSA_3_f.columns.str.contains('^Unnamed')]

BSA_4_f=BSA_4.pivot(index =BSA_4.index, columns ='Unnamed: 0')
BSA_4_f=BSA_4_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_4_f.columns = BSA_4_f.columns.droplevel(0)
BSA_4_f = BSA_4_f.loc[:, ~BSA_4_f.columns.str.contains('^Unnamed')]

BSA_5_f=BSA_5.pivot(index =BSA_5.index, columns ='Unnamed: 0')
BSA_5_f=BSA_5_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_5_f.columns = BSA_5_f.columns.droplevel(0)
BSA_5_f = BSA_5_f.loc[:, ~BSA_5_f.columns.str.contains('^Unnamed')]

BSA_6_f=BSA_6.pivot(index =BSA_6.index, columns ='Unnamed: 0')
BSA_6_f=BSA_6_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_6_f.columns = BSA_6_f.columns.droplevel(0)
BSA_6_f = BSA_6_f.loc[:, ~BSA_6_f.columns.str.contains('^Unnamed')]

BSA_7_f=BSA_7.pivot(index =BSA_7.index, columns ='Unnamed: 0')
BSA_7_f=BSA_7_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_7_f.columns = BSA_7_f.columns.droplevel(0)
BSA_7_f = BSA_7_f.loc[:, ~BSA_7_f.columns.str.contains('^Unnamed')]

BSA_8_f=BSA_8.pivot(index =BSA_8.index, columns ='Unnamed: 0')
BSA_8_f=BSA_8_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_8_f.columns = BSA_8_f.columns.droplevel(0)
BSA_8_f = BSA_8_f.loc[:, ~BSA_8_f.columns.str.contains('^Unnamed')]

BSA_9_f=BSA_9.pivot(index =BSA_9.index, columns ='Unnamed: 0')
BSA_9_f=BSA_9_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_9_f.columns = BSA_9_f.columns.droplevel(0)
BSA_9_f = BSA_9_f.loc[:, ~BSA_9_f.columns.str.contains('^Unnamed')]

BSA_10_f=BSA_10.pivot(index =BSA_10.index, columns ='Unnamed: 0')
BSA_10_f=BSA_10_f.apply(lambda x: pd.Series(x.dropna().values))
BSA_10_f.columns = BSA_10_f.columns.droplevel(0)
BSA_10_f = BSA_10_f.loc[:, ~BSA_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([BSA_0_f,BSA_005_f,BSA_01_f,BSA_015_f,BSA_02_f,BSA_025_f,BSA_03_f,BSA_035_f,BSA_04_f,BSA_045_f,BSA_05_f,BSA_1_f,BSA_2_f,BSA_3_f,BSA_4_f,BSA_5_f,BSA_6_f,BSA_7_f,BSA_8_f,BSA_9_f,BSA_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('BSA.csv', header=True)