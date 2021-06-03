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
BSB_0=pd.read_csv('BSB_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_005=pd.read_csv('BSB_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_01=pd.read_csv('BSB_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_015=pd.read_csv('BSB_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_02=pd.read_csv('BSB_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_025=pd.read_csv('BSB_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_03=pd.read_csv('BSB_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_035=pd.read_csv('BSB_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_04=pd.read_csv('BSB_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_045=pd.read_csv('BSB_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_05=pd.read_csv('BSB_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_1=pd.read_csv('BSB_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_2=pd.read_csv('BSB_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_3=pd.read_csv('BSB_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_4=pd.read_csv('BSB_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_5=pd.read_csv('BSB_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_6=pd.read_csv('BSB_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_7=pd.read_csv('BSB_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_8=pd.read_csv('BSB_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_9=pd.read_csv('BSB_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
BSB_10=pd.read_csv('BSB_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

BSB_0_f=BSB_0.pivot(index =BSB_005.index, columns ='Unnamed: 0')
BSB_0_f=BSB_0_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_0_f.columns = BSB_0_f.columns.droplevel(0)
BSB_0_f = BSB_0_f.loc[:, ~BSB_0_f.columns.str.contains('^Unnamed')]

BSB_005_f=BSB_005.pivot(index =BSB_005.index, columns ='Unnamed: 0')
BSB_005_f=BSB_005_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_005_f.columns = BSB_005_f.columns.droplevel(0)
BSB_005_f = BSB_005_f.loc[:, ~BSB_005_f.columns.str.contains('^Unnamed')]

BSB_01_f=BSB_01.pivot(index =BSB_01.index, columns ='Unnamed: 0')
BSB_01_f=BSB_01_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_01_f.columns = BSB_01_f.columns.droplevel(0)
BSB_01_f = BSB_01_f.loc[:, ~BSB_01_f.columns.str.contains('^Unnamed')]

BSB_015_f=BSB_015.pivot(index =BSB_015.index, columns ='Unnamed: 0')
BSB_015_f=BSB_015_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_015_f.columns = BSB_015_f.columns.droplevel(0)
BSB_015_f = BSB_015_f.loc[:, ~BSB_015_f.columns.str.contains('^Unnamed')]

BSB_02_f=BSB_02.pivot(index =BSB_02.index, columns ='Unnamed: 0')
BSB_02_f=BSB_02_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_02_f.columns = BSB_02_f.columns.droplevel(0)
BSB_02_f = BSB_02_f.loc[:, ~BSB_02_f.columns.str.contains('^Unnamed')]

BSB_025_f=BSB_025.pivot(index =BSB_025.index, columns ='Unnamed: 0')
BSB_025_f=BSB_025_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_025_f.columns = BSB_025_f.columns.droplevel(0)
BSB_025_f = BSB_025_f.loc[:, ~BSB_025_f.columns.str.contains('^Unnamed')]

BSB_03_f=BSB_03.pivot(index =BSB_03.index, columns ='Unnamed: 0')
BSB_03_f=BSB_03_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_03_f.columns = BSB_03_f.columns.droplevel(0)
BSB_03_f = BSB_03_f.loc[:, ~BSB_03_f.columns.str.contains('^Unnamed')]

BSB_035_f=BSB_035.pivot(index =BSB_035.index, columns ='Unnamed: 0')
BSB_035_f=BSB_035_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_035_f.columns = BSB_035_f.columns.droplevel(0)
BSB_035_f = BSB_035_f.loc[:, ~BSB_035_f.columns.str.contains('^Unnamed')]

BSB_04_f=BSB_04.pivot(index =BSB_04.index, columns ='Unnamed: 0')
BSB_04_f=BSB_04_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_04_f.columns = BSB_04_f.columns.droplevel(0)
BSB_04_f = BSB_04_f.loc[:, ~BSB_04_f.columns.str.contains('^Unnamed')]

BSB_045_f=BSB_045.pivot(index =BSB_045.index, columns ='Unnamed: 0')
BSB_045_f=BSB_045_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_045_f.columns = BSB_045_f.columns.droplevel(0)
BSB_045_f = BSB_045_f.loc[:, ~BSB_045_f.columns.str.contains('^Unnamed')]

BSB_05_f=BSB_05.pivot(index =BSB_05.index, columns ='Unnamed: 0')
BSB_05_f=BSB_05_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_05_f.columns = BSB_05_f.columns.droplevel(0)
BSB_05_f = BSB_05_f.loc[:, ~BSB_05_f.columns.str.contains('^Unnamed')]

BSB_1_f=BSB_1.pivot(index =BSB_1.index, columns ='Unnamed: 0')
BSB_1_f=BSB_1_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_1_f.columns = BSB_1_f.columns.droplevel(0)
BSB_1_f = BSB_1_f.loc[:, ~BSB_1_f.columns.str.contains('^Unnamed')]

BSB_2_f=BSB_2.pivot(index =BSB_2.index, columns ='Unnamed: 0')
BSB_2_f=BSB_2_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_2_f.columns = BSB_2_f.columns.droplevel(0)
BSB_2_f = BSB_2_f.loc[:, ~BSB_2_f.columns.str.contains('^Unnamed')]

BSB_3_f=BSB_3.pivot(index =BSB_3.index, columns ='Unnamed: 0')
BSB_3_f=BSB_3_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_3_f.columns = BSB_3_f.columns.droplevel(0)
BSB_3_f = BSB_3_f.loc[:, ~BSB_3_f.columns.str.contains('^Unnamed')]

BSB_4_f=BSB_4.pivot(index =BSB_4.index, columns ='Unnamed: 0')
BSB_4_f=BSB_4_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_4_f.columns = BSB_4_f.columns.droplevel(0)
BSB_4_f = BSB_4_f.loc[:, ~BSB_4_f.columns.str.contains('^Unnamed')]

BSB_5_f=BSB_5.pivot(index =BSB_5.index, columns ='Unnamed: 0')
BSB_5_f=BSB_5_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_5_f.columns = BSB_5_f.columns.droplevel(0)
BSB_5_f = BSB_5_f.loc[:, ~BSB_5_f.columns.str.contains('^Unnamed')]

BSB_6_f=BSB_6.pivot(index =BSB_6.index, columns ='Unnamed: 0')
BSB_6_f=BSB_6_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_6_f.columns = BSB_6_f.columns.droplevel(0)
BSB_6_f = BSB_6_f.loc[:, ~BSB_6_f.columns.str.contains('^Unnamed')]

BSB_7_f=BSB_7.pivot(index =BSB_7.index, columns ='Unnamed: 0')
BSB_7_f=BSB_7_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_7_f.columns = BSB_7_f.columns.droplevel(0)
BSB_7_f = BSB_7_f.loc[:, ~BSB_7_f.columns.str.contains('^Unnamed')]

BSB_8_f=BSB_8.pivot(index =BSB_8.index, columns ='Unnamed: 0')
BSB_8_f=BSB_8_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_8_f.columns = BSB_8_f.columns.droplevel(0)
BSB_8_f = BSB_8_f.loc[:, ~BSB_8_f.columns.str.contains('^Unnamed')]

BSB_9_f=BSB_9.pivot(index =BSB_9.index, columns ='Unnamed: 0')
BSB_9_f=BSB_9_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_9_f.columns = BSB_9_f.columns.droplevel(0)
BSB_9_f = BSB_9_f.loc[:, ~BSB_9_f.columns.str.contains('^Unnamed')]

BSB_10_f=BSB_10.pivot(index =BSB_10.index, columns ='Unnamed: 0')
BSB_10_f=BSB_10_f.apply(lambda x: pd.Series(x.dropna().values))
BSB_10_f.columns = BSB_10_f.columns.droplevel(0)
BSB_10_f = BSB_10_f.loc[:, ~BSB_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([BSB_0_f,BSB_005_f,BSB_01_f,BSB_015_f,BSB_02_f,BSB_025_f,BSB_03_f,BSB_035_f,BSB_04_f,BSB_045_f,BSB_05_f,BSB_1_f,BSB_2_f,BSB_3_f,BSB_4_f,BSB_5_f,BSB_6_f,BSB_7_f,BSB_8_f,BSB_9_f,BSB_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('BSB.csv', header=True)