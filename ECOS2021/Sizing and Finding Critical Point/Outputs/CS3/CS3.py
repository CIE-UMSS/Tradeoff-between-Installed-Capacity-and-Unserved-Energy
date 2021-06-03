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
CS3_0=pd.read_csv('CS3_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_005=pd.read_csv('CS3_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_01=pd.read_csv('CS3_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_015=pd.read_csv('CS3_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_02=pd.read_csv('CS3_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_025=pd.read_csv('CS3_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_03=pd.read_csv('CS3_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_035=pd.read_csv('CS3_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_04=pd.read_csv('CS3_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_045=pd.read_csv('CS3_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_05=pd.read_csv('CS3_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_1=pd.read_csv('CS3_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_2=pd.read_csv('CS3_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_3=pd.read_csv('CS3_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_4=pd.read_csv('CS3_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_5=pd.read_csv('CS3_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_6=pd.read_csv('CS3_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_7=pd.read_csv('CS3_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_8=pd.read_csv('CS3_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_9=pd.read_csv('CS3_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS3_10=pd.read_csv('CS3_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

CS3_0_f=CS3_0.pivot(index =CS3_005.index, columns ='Unnamed: 0')
CS3_0_f=CS3_0_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_0_f.columns = CS3_0_f.columns.droplevel(0)
CS3_0_f = CS3_0_f.loc[:, ~CS3_0_f.columns.str.contains('^Unnamed')]

CS3_005_f=CS3_005.pivot(index =CS3_005.index, columns ='Unnamed: 0')
CS3_005_f=CS3_005_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_005_f.columns = CS3_005_f.columns.droplevel(0)
CS3_005_f = CS3_005_f.loc[:, ~CS3_005_f.columns.str.contains('^Unnamed')]

CS3_01_f=CS3_01.pivot(index =CS3_01.index, columns ='Unnamed: 0')
CS3_01_f=CS3_01_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_01_f.columns = CS3_01_f.columns.droplevel(0)
CS3_01_f = CS3_01_f.loc[:, ~CS3_01_f.columns.str.contains('^Unnamed')]

CS3_015_f=CS3_015.pivot(index =CS3_015.index, columns ='Unnamed: 0')
CS3_015_f=CS3_015_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_015_f.columns = CS3_015_f.columns.droplevel(0)
CS3_015_f = CS3_015_f.loc[:, ~CS3_015_f.columns.str.contains('^Unnamed')]

CS3_02_f=CS3_02.pivot(index =CS3_02.index, columns ='Unnamed: 0')
CS3_02_f=CS3_02_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_02_f.columns = CS3_02_f.columns.droplevel(0)
CS3_02_f = CS3_02_f.loc[:, ~CS3_02_f.columns.str.contains('^Unnamed')]

CS3_025_f=CS3_025.pivot(index =CS3_025.index, columns ='Unnamed: 0')
CS3_025_f=CS3_025_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_025_f.columns = CS3_025_f.columns.droplevel(0)
CS3_025_f = CS3_025_f.loc[:, ~CS3_025_f.columns.str.contains('^Unnamed')]

CS3_03_f=CS3_03.pivot(index =CS3_03.index, columns ='Unnamed: 0')
CS3_03_f=CS3_03_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_03_f.columns = CS3_03_f.columns.droplevel(0)
CS3_03_f = CS3_03_f.loc[:, ~CS3_03_f.columns.str.contains('^Unnamed')]

CS3_035_f=CS3_035.pivot(index =CS3_035.index, columns ='Unnamed: 0')
CS3_035_f=CS3_035_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_035_f.columns = CS3_035_f.columns.droplevel(0)
CS3_035_f = CS3_035_f.loc[:, ~CS3_035_f.columns.str.contains('^Unnamed')]

CS3_04_f=CS3_04.pivot(index =CS3_04.index, columns ='Unnamed: 0')
CS3_04_f=CS3_04_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_04_f.columns = CS3_04_f.columns.droplevel(0)
CS3_04_f = CS3_04_f.loc[:, ~CS3_04_f.columns.str.contains('^Unnamed')]

CS3_045_f=CS3_045.pivot(index =CS3_045.index, columns ='Unnamed: 0')
CS3_045_f=CS3_045_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_045_f.columns = CS3_045_f.columns.droplevel(0)
CS3_045_f = CS3_045_f.loc[:, ~CS3_045_f.columns.str.contains('^Unnamed')]

CS3_05_f=CS3_05.pivot(index =CS3_05.index, columns ='Unnamed: 0')
CS3_05_f=CS3_05_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_05_f.columns = CS3_05_f.columns.droplevel(0)
CS3_05_f = CS3_05_f.loc[:, ~CS3_05_f.columns.str.contains('^Unnamed')]

CS3_1_f=CS3_1.pivot(index =CS3_1.index, columns ='Unnamed: 0')
CS3_1_f=CS3_1_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_1_f.columns = CS3_1_f.columns.droplevel(0)
CS3_1_f = CS3_1_f.loc[:, ~CS3_1_f.columns.str.contains('^Unnamed')]

CS3_2_f=CS3_2.pivot(index =CS3_2.index, columns ='Unnamed: 0')
CS3_2_f=CS3_2_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_2_f.columns = CS3_2_f.columns.droplevel(0)
CS3_2_f = CS3_2_f.loc[:, ~CS3_2_f.columns.str.contains('^Unnamed')]

CS3_3_f=CS3_3.pivot(index =CS3_3.index, columns ='Unnamed: 0')
CS3_3_f=CS3_3_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_3_f.columns = CS3_3_f.columns.droplevel(0)
CS3_3_f = CS3_3_f.loc[:, ~CS3_3_f.columns.str.contains('^Unnamed')]

CS3_4_f=CS3_4.pivot(index =CS3_4.index, columns ='Unnamed: 0')
CS3_4_f=CS3_4_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_4_f.columns = CS3_4_f.columns.droplevel(0)
CS3_4_f = CS3_4_f.loc[:, ~CS3_4_f.columns.str.contains('^Unnamed')]

CS3_5_f=CS3_5.pivot(index =CS3_5.index, columns ='Unnamed: 0')
CS3_5_f=CS3_5_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_5_f.columns = CS3_5_f.columns.droplevel(0)
CS3_5_f = CS3_5_f.loc[:, ~CS3_5_f.columns.str.contains('^Unnamed')]

CS3_6_f=CS3_6.pivot(index =CS3_6.index, columns ='Unnamed: 0')
CS3_6_f=CS3_6_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_6_f.columns = CS3_6_f.columns.droplevel(0)
CS3_6_f = CS3_6_f.loc[:, ~CS3_6_f.columns.str.contains('^Unnamed')]

CS3_7_f=CS3_7.pivot(index =CS3_7.index, columns ='Unnamed: 0')
CS3_7_f=CS3_7_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_7_f.columns = CS3_7_f.columns.droplevel(0)
CS3_7_f = CS3_7_f.loc[:, ~CS3_7_f.columns.str.contains('^Unnamed')]

CS3_8_f=CS3_8.pivot(index =CS3_8.index, columns ='Unnamed: 0')
CS3_8_f=CS3_8_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_8_f.columns = CS3_8_f.columns.droplevel(0)
CS3_8_f = CS3_8_f.loc[:, ~CS3_8_f.columns.str.contains('^Unnamed')]

CS3_9_f=CS3_9.pivot(index =CS3_9.index, columns ='Unnamed: 0')
CS3_9_f=CS3_9_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_9_f.columns = CS3_9_f.columns.droplevel(0)
CS3_9_f = CS3_9_f.loc[:, ~CS3_9_f.columns.str.contains('^Unnamed')]

CS3_10_f=CS3_10.pivot(index =CS3_10.index, columns ='Unnamed: 0')
CS3_10_f=CS3_10_f.apply(lambda x: pd.Series(x.dropna().values))
CS3_10_f.columns = CS3_10_f.columns.droplevel(0)
CS3_10_f = CS3_10_f.loc[:, ~CS3_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([CS3_0_f,CS3_005_f,CS3_01_f,CS3_015_f,CS3_02_f,CS3_025_f,CS3_03_f,CS3_035_f,CS3_04_f,CS3_045_f,CS3_05_f,CS3_1_f,CS3_2_f,CS3_3_f,CS3_4_f,CS3_5_f,CS3_6_f,CS3_7_f,CS3_8_f,CS3_9_f,CS3_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('CS3.csv', header=True)