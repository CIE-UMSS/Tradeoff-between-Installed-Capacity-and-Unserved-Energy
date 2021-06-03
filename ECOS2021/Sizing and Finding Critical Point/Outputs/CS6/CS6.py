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
CS6_0=pd.read_csv('CS6_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_005=pd.read_csv('CS6_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_01=pd.read_csv('CS6_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_015=pd.read_csv('CS6_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_02=pd.read_csv('CS6_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_025=pd.read_csv('CS6_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_03=pd.read_csv('CS6_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_035=pd.read_csv('CS6_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_04=pd.read_csv('CS6_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_045=pd.read_csv('CS6_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_05=pd.read_csv('CS6_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_1=pd.read_csv('CS6_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_2=pd.read_csv('CS6_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_3=pd.read_csv('CS6_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_4=pd.read_csv('CS6_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_5=pd.read_csv('CS6_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_6=pd.read_csv('CS6_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_7=pd.read_csv('CS6_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_8=pd.read_csv('CS6_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_9=pd.read_csv('CS6_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS6_10=pd.read_csv('CS6_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

CS6_0_f=CS6_0.pivot(index =CS6_005.index, columns ='Unnamed: 0')
CS6_0_f=CS6_0_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_0_f.columns = CS6_0_f.columns.droplevel(0)
CS6_0_f = CS6_0_f.loc[:, ~CS6_0_f.columns.str.contains('^Unnamed')]

CS6_005_f=CS6_005.pivot(index =CS6_005.index, columns ='Unnamed: 0')
CS6_005_f=CS6_005_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_005_f.columns = CS6_005_f.columns.droplevel(0)
CS6_005_f = CS6_005_f.loc[:, ~CS6_005_f.columns.str.contains('^Unnamed')]

CS6_01_f=CS6_01.pivot(index =CS6_01.index, columns ='Unnamed: 0')
CS6_01_f=CS6_01_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_01_f.columns = CS6_01_f.columns.droplevel(0)
CS6_01_f = CS6_01_f.loc[:, ~CS6_01_f.columns.str.contains('^Unnamed')]

CS6_015_f=CS6_015.pivot(index =CS6_015.index, columns ='Unnamed: 0')
CS6_015_f=CS6_015_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_015_f.columns = CS6_015_f.columns.droplevel(0)
CS6_015_f = CS6_015_f.loc[:, ~CS6_015_f.columns.str.contains('^Unnamed')]

CS6_02_f=CS6_02.pivot(index =CS6_02.index, columns ='Unnamed: 0')
CS6_02_f=CS6_02_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_02_f.columns = CS6_02_f.columns.droplevel(0)
CS6_02_f = CS6_02_f.loc[:, ~CS6_02_f.columns.str.contains('^Unnamed')]

CS6_025_f=CS6_025.pivot(index =CS6_025.index, columns ='Unnamed: 0')
CS6_025_f=CS6_025_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_025_f.columns = CS6_025_f.columns.droplevel(0)
CS6_025_f = CS6_025_f.loc[:, ~CS6_025_f.columns.str.contains('^Unnamed')]

CS6_03_f=CS6_03.pivot(index =CS6_03.index, columns ='Unnamed: 0')
CS6_03_f=CS6_03_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_03_f.columns = CS6_03_f.columns.droplevel(0)
CS6_03_f = CS6_03_f.loc[:, ~CS6_03_f.columns.str.contains('^Unnamed')]

CS6_035_f=CS6_035.pivot(index =CS6_035.index, columns ='Unnamed: 0')
CS6_035_f=CS6_035_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_035_f.columns = CS6_035_f.columns.droplevel(0)
CS6_035_f = CS6_035_f.loc[:, ~CS6_035_f.columns.str.contains('^Unnamed')]

CS6_04_f=CS6_04.pivot(index =CS6_04.index, columns ='Unnamed: 0')
CS6_04_f=CS6_04_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_04_f.columns = CS6_04_f.columns.droplevel(0)
CS6_04_f = CS6_04_f.loc[:, ~CS6_04_f.columns.str.contains('^Unnamed')]

CS6_045_f=CS6_045.pivot(index =CS6_045.index, columns ='Unnamed: 0')
CS6_045_f=CS6_045_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_045_f.columns = CS6_045_f.columns.droplevel(0)
CS6_045_f = CS6_045_f.loc[:, ~CS6_045_f.columns.str.contains('^Unnamed')]

CS6_05_f=CS6_05.pivot(index =CS6_05.index, columns ='Unnamed: 0')
CS6_05_f=CS6_05_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_05_f.columns = CS6_05_f.columns.droplevel(0)
CS6_05_f = CS6_05_f.loc[:, ~CS6_05_f.columns.str.contains('^Unnamed')]

CS6_1_f=CS6_1.pivot(index =CS6_1.index, columns ='Unnamed: 0')
CS6_1_f=CS6_1_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_1_f.columns = CS6_1_f.columns.droplevel(0)
CS6_1_f = CS6_1_f.loc[:, ~CS6_1_f.columns.str.contains('^Unnamed')]

CS6_2_f=CS6_2.pivot(index =CS6_2.index, columns ='Unnamed: 0')
CS6_2_f=CS6_2_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_2_f.columns = CS6_2_f.columns.droplevel(0)
CS6_2_f = CS6_2_f.loc[:, ~CS6_2_f.columns.str.contains('^Unnamed')]

CS6_3_f=CS6_3.pivot(index =CS6_3.index, columns ='Unnamed: 0')
CS6_3_f=CS6_3_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_3_f.columns = CS6_3_f.columns.droplevel(0)
CS6_3_f = CS6_3_f.loc[:, ~CS6_3_f.columns.str.contains('^Unnamed')]

CS6_4_f=CS6_4.pivot(index =CS6_4.index, columns ='Unnamed: 0')
CS6_4_f=CS6_4_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_4_f.columns = CS6_4_f.columns.droplevel(0)
CS6_4_f = CS6_4_f.loc[:, ~CS6_4_f.columns.str.contains('^Unnamed')]

CS6_5_f=CS6_5.pivot(index =CS6_5.index, columns ='Unnamed: 0')
CS6_5_f=CS6_5_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_5_f.columns = CS6_5_f.columns.droplevel(0)
CS6_5_f = CS6_5_f.loc[:, ~CS6_5_f.columns.str.contains('^Unnamed')]

CS6_6_f=CS6_6.pivot(index =CS6_6.index, columns ='Unnamed: 0')
CS6_6_f=CS6_6_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_6_f.columns = CS6_6_f.columns.droplevel(0)
CS6_6_f = CS6_6_f.loc[:, ~CS6_6_f.columns.str.contains('^Unnamed')]

CS6_7_f=CS6_7.pivot(index =CS6_7.index, columns ='Unnamed: 0')
CS6_7_f=CS6_7_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_7_f.columns = CS6_7_f.columns.droplevel(0)
CS6_7_f = CS6_7_f.loc[:, ~CS6_7_f.columns.str.contains('^Unnamed')]

CS6_8_f=CS6_8.pivot(index =CS6_8.index, columns ='Unnamed: 0')
CS6_8_f=CS6_8_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_8_f.columns = CS6_8_f.columns.droplevel(0)
CS6_8_f = CS6_8_f.loc[:, ~CS6_8_f.columns.str.contains('^Unnamed')]

CS6_9_f=CS6_9.pivot(index =CS6_9.index, columns ='Unnamed: 0')
CS6_9_f=CS6_9_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_9_f.columns = CS6_9_f.columns.droplevel(0)
CS6_9_f = CS6_9_f.loc[:, ~CS6_9_f.columns.str.contains('^Unnamed')]

CS6_10_f=CS6_10.pivot(index =CS6_10.index, columns ='Unnamed: 0')
CS6_10_f=CS6_10_f.apply(lambda x: pd.Series(x.dropna().values))
CS6_10_f.columns = CS6_10_f.columns.droplevel(0)
CS6_10_f = CS6_10_f.loc[:, ~CS6_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([CS6_0_f,CS6_005_f,CS6_01_f,CS6_015_f,CS6_02_f,CS6_025_f,CS6_03_f,CS6_035_f,CS6_04_f,CS6_045_f,CS6_05_f,CS6_1_f,CS6_2_f,CS6_3_f,CS6_4_f,CS6_5_f,CS6_6_f,CS6_7_f,CS6_8_f,CS6_9_f,CS6_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('CS6.csv', header=True)