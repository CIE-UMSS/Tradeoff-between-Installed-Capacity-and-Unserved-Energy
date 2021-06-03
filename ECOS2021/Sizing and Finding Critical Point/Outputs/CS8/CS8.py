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
CS8_0=pd.read_csv('CS8_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_005=pd.read_csv('CS8_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_01=pd.read_csv('CS8_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_015=pd.read_csv('CS8_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_02=pd.read_csv('CS8_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_025=pd.read_csv('CS8_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_03=pd.read_csv('CS8_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_035=pd.read_csv('CS8_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_04=pd.read_csv('CS8_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_045=pd.read_csv('CS8_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_05=pd.read_csv('CS8_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_1=pd.read_csv('CS8_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_2=pd.read_csv('CS8_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_3=pd.read_csv('CS8_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_4=pd.read_csv('CS8_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_5=pd.read_csv('CS8_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_6=pd.read_csv('CS8_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_7=pd.read_csv('CS8_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_8=pd.read_csv('CS8_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_9=pd.read_csv('CS8_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS8_10=pd.read_csv('CS8_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

CS8_0_f=CS8_0.pivot(index =CS8_005.index, columns ='Unnamed: 0')
CS8_0_f=CS8_0_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_0_f.columns = CS8_0_f.columns.droplevel(0)
CS8_0_f = CS8_0_f.loc[:, ~CS8_0_f.columns.str.contains('^Unnamed')]

CS8_005_f=CS8_005.pivot(index =CS8_005.index, columns ='Unnamed: 0')
CS8_005_f=CS8_005_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_005_f.columns = CS8_005_f.columns.droplevel(0)
CS8_005_f = CS8_005_f.loc[:, ~CS8_005_f.columns.str.contains('^Unnamed')]

CS8_01_f=CS8_01.pivot(index =CS8_01.index, columns ='Unnamed: 0')
CS8_01_f=CS8_01_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_01_f.columns = CS8_01_f.columns.droplevel(0)
CS8_01_f = CS8_01_f.loc[:, ~CS8_01_f.columns.str.contains('^Unnamed')]

CS8_015_f=CS8_015.pivot(index =CS8_015.index, columns ='Unnamed: 0')
CS8_015_f=CS8_015_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_015_f.columns = CS8_015_f.columns.droplevel(0)
CS8_015_f = CS8_015_f.loc[:, ~CS8_015_f.columns.str.contains('^Unnamed')]

CS8_02_f=CS8_02.pivot(index =CS8_02.index, columns ='Unnamed: 0')
CS8_02_f=CS8_02_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_02_f.columns = CS8_02_f.columns.droplevel(0)
CS8_02_f = CS8_02_f.loc[:, ~CS8_02_f.columns.str.contains('^Unnamed')]

CS8_025_f=CS8_025.pivot(index =CS8_025.index, columns ='Unnamed: 0')
CS8_025_f=CS8_025_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_025_f.columns = CS8_025_f.columns.droplevel(0)
CS8_025_f = CS8_025_f.loc[:, ~CS8_025_f.columns.str.contains('^Unnamed')]

CS8_03_f=CS8_03.pivot(index =CS8_03.index, columns ='Unnamed: 0')
CS8_03_f=CS8_03_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_03_f.columns = CS8_03_f.columns.droplevel(0)
CS8_03_f = CS8_03_f.loc[:, ~CS8_03_f.columns.str.contains('^Unnamed')]

CS8_035_f=CS8_035.pivot(index =CS8_035.index, columns ='Unnamed: 0')
CS8_035_f=CS8_035_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_035_f.columns = CS8_035_f.columns.droplevel(0)
CS8_035_f = CS8_035_f.loc[:, ~CS8_035_f.columns.str.contains('^Unnamed')]

CS8_04_f=CS8_04.pivot(index =CS8_04.index, columns ='Unnamed: 0')
CS8_04_f=CS8_04_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_04_f.columns = CS8_04_f.columns.droplevel(0)
CS8_04_f = CS8_04_f.loc[:, ~CS8_04_f.columns.str.contains('^Unnamed')]

CS8_045_f=CS8_045.pivot(index =CS8_045.index, columns ='Unnamed: 0')
CS8_045_f=CS8_045_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_045_f.columns = CS8_045_f.columns.droplevel(0)
CS8_045_f = CS8_045_f.loc[:, ~CS8_045_f.columns.str.contains('^Unnamed')]

CS8_05_f=CS8_05.pivot(index =CS8_05.index, columns ='Unnamed: 0')
CS8_05_f=CS8_05_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_05_f.columns = CS8_05_f.columns.droplevel(0)
CS8_05_f = CS8_05_f.loc[:, ~CS8_05_f.columns.str.contains('^Unnamed')]

CS8_1_f=CS8_1.pivot(index =CS8_1.index, columns ='Unnamed: 0')
CS8_1_f=CS8_1_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_1_f.columns = CS8_1_f.columns.droplevel(0)
CS8_1_f = CS8_1_f.loc[:, ~CS8_1_f.columns.str.contains('^Unnamed')]

CS8_2_f=CS8_2.pivot(index =CS8_2.index, columns ='Unnamed: 0')
CS8_2_f=CS8_2_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_2_f.columns = CS8_2_f.columns.droplevel(0)
CS8_2_f = CS8_2_f.loc[:, ~CS8_2_f.columns.str.contains('^Unnamed')]

CS8_3_f=CS8_3.pivot(index =CS8_3.index, columns ='Unnamed: 0')
CS8_3_f=CS8_3_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_3_f.columns = CS8_3_f.columns.droplevel(0)
CS8_3_f = CS8_3_f.loc[:, ~CS8_3_f.columns.str.contains('^Unnamed')]

CS8_4_f=CS8_4.pivot(index =CS8_4.index, columns ='Unnamed: 0')
CS8_4_f=CS8_4_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_4_f.columns = CS8_4_f.columns.droplevel(0)
CS8_4_f = CS8_4_f.loc[:, ~CS8_4_f.columns.str.contains('^Unnamed')]

CS8_5_f=CS8_5.pivot(index =CS8_5.index, columns ='Unnamed: 0')
CS8_5_f=CS8_5_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_5_f.columns = CS8_5_f.columns.droplevel(0)
CS8_5_f = CS8_5_f.loc[:, ~CS8_5_f.columns.str.contains('^Unnamed')]

CS8_6_f=CS8_6.pivot(index =CS8_6.index, columns ='Unnamed: 0')
CS8_6_f=CS8_6_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_6_f.columns = CS8_6_f.columns.droplevel(0)
CS8_6_f = CS8_6_f.loc[:, ~CS8_6_f.columns.str.contains('^Unnamed')]

CS8_7_f=CS8_7.pivot(index =CS8_7.index, columns ='Unnamed: 0')
CS8_7_f=CS8_7_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_7_f.columns = CS8_7_f.columns.droplevel(0)
CS8_7_f = CS8_7_f.loc[:, ~CS8_7_f.columns.str.contains('^Unnamed')]

CS8_8_f=CS8_8.pivot(index =CS8_8.index, columns ='Unnamed: 0')
CS8_8_f=CS8_8_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_8_f.columns = CS8_8_f.columns.droplevel(0)
CS8_8_f = CS8_8_f.loc[:, ~CS8_8_f.columns.str.contains('^Unnamed')]

CS8_9_f=CS8_9.pivot(index =CS8_9.index, columns ='Unnamed: 0')
CS8_9_f=CS8_9_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_9_f.columns = CS8_9_f.columns.droplevel(0)
CS8_9_f = CS8_9_f.loc[:, ~CS8_9_f.columns.str.contains('^Unnamed')]

CS8_10_f=CS8_10.pivot(index =CS8_10.index, columns ='Unnamed: 0')
CS8_10_f=CS8_10_f.apply(lambda x: pd.Series(x.dropna().values))
CS8_10_f.columns = CS8_10_f.columns.droplevel(0)
CS8_10_f = CS8_10_f.loc[:, ~CS8_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([CS8_0_f,CS8_005_f,CS8_01_f,CS8_015_f,CS8_02_f,CS8_025_f,CS8_03_f,CS8_035_f,CS8_04_f,CS8_045_f,CS8_05_f,CS8_1_f,CS8_2_f,CS8_3_f,CS8_4_f,CS8_5_f,CS8_6_f,CS8_7_f,CS8_8_f,CS8_9_f,CS8_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('CS8.csv', header=True)