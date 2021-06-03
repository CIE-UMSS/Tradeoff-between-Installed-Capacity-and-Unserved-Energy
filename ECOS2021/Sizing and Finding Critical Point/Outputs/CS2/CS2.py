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
CS2_0=pd.read_csv('CS2_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_005=pd.read_csv('CS2_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_01=pd.read_csv('CS2_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_015=pd.read_csv('CS2_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_02=pd.read_csv('CS2_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_025=pd.read_csv('CS2_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_03=pd.read_csv('CS2_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_035=pd.read_csv('CS2_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_04=pd.read_csv('CS2_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_045=pd.read_csv('CS2_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_05=pd.read_csv('CS2_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_1=pd.read_csv('CS2_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_2=pd.read_csv('CS2_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_3=pd.read_csv('CS2_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_4=pd.read_csv('CS2_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_5=pd.read_csv('CS2_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_6=pd.read_csv('CS2_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_7=pd.read_csv('CS2_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_8=pd.read_csv('CS2_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_9=pd.read_csv('CS2_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS2_10=pd.read_csv('CS2_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

CS2_0_f=CS2_0.pivot(index =CS2_005.index, columns ='Unnamed: 0')
CS2_0_f=CS2_0_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_0_f.columns = CS2_0_f.columns.droplevel(0)
CS2_0_f = CS2_0_f.loc[:, ~CS2_0_f.columns.str.contains('^Unnamed')]

CS2_005_f=CS2_005.pivot(index =CS2_005.index, columns ='Unnamed: 0')
CS2_005_f=CS2_005_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_005_f.columns = CS2_005_f.columns.droplevel(0)
CS2_005_f = CS2_005_f.loc[:, ~CS2_005_f.columns.str.contains('^Unnamed')]

CS2_01_f=CS2_01.pivot(index =CS2_01.index, columns ='Unnamed: 0')
CS2_01_f=CS2_01_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_01_f.columns = CS2_01_f.columns.droplevel(0)
CS2_01_f = CS2_01_f.loc[:, ~CS2_01_f.columns.str.contains('^Unnamed')]

CS2_015_f=CS2_015.pivot(index =CS2_015.index, columns ='Unnamed: 0')
CS2_015_f=CS2_015_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_015_f.columns = CS2_015_f.columns.droplevel(0)
CS2_015_f = CS2_015_f.loc[:, ~CS2_015_f.columns.str.contains('^Unnamed')]

CS2_02_f=CS2_02.pivot(index =CS2_02.index, columns ='Unnamed: 0')
CS2_02_f=CS2_02_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_02_f.columns = CS2_02_f.columns.droplevel(0)
CS2_02_f = CS2_02_f.loc[:, ~CS2_02_f.columns.str.contains('^Unnamed')]

CS2_025_f=CS2_025.pivot(index =CS2_025.index, columns ='Unnamed: 0')
CS2_025_f=CS2_025_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_025_f.columns = CS2_025_f.columns.droplevel(0)
CS2_025_f = CS2_025_f.loc[:, ~CS2_025_f.columns.str.contains('^Unnamed')]

CS2_03_f=CS2_03.pivot(index =CS2_03.index, columns ='Unnamed: 0')
CS2_03_f=CS2_03_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_03_f.columns = CS2_03_f.columns.droplevel(0)
CS2_03_f = CS2_03_f.loc[:, ~CS2_03_f.columns.str.contains('^Unnamed')]

CS2_035_f=CS2_035.pivot(index =CS2_035.index, columns ='Unnamed: 0')
CS2_035_f=CS2_035_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_035_f.columns = CS2_035_f.columns.droplevel(0)
CS2_035_f = CS2_035_f.loc[:, ~CS2_035_f.columns.str.contains('^Unnamed')]

CS2_04_f=CS2_04.pivot(index =CS2_04.index, columns ='Unnamed: 0')
CS2_04_f=CS2_04_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_04_f.columns = CS2_04_f.columns.droplevel(0)
CS2_04_f = CS2_04_f.loc[:, ~CS2_04_f.columns.str.contains('^Unnamed')]

CS2_045_f=CS2_045.pivot(index =CS2_045.index, columns ='Unnamed: 0')
CS2_045_f=CS2_045_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_045_f.columns = CS2_045_f.columns.droplevel(0)
CS2_045_f = CS2_045_f.loc[:, ~CS2_045_f.columns.str.contains('^Unnamed')]

CS2_05_f=CS2_05.pivot(index =CS2_05.index, columns ='Unnamed: 0')
CS2_05_f=CS2_05_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_05_f.columns = CS2_05_f.columns.droplevel(0)
CS2_05_f = CS2_05_f.loc[:, ~CS2_05_f.columns.str.contains('^Unnamed')]

CS2_1_f=CS2_1.pivot(index =CS2_1.index, columns ='Unnamed: 0')
CS2_1_f=CS2_1_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_1_f.columns = CS2_1_f.columns.droplevel(0)
CS2_1_f = CS2_1_f.loc[:, ~CS2_1_f.columns.str.contains('^Unnamed')]

CS2_2_f=CS2_2.pivot(index =CS2_2.index, columns ='Unnamed: 0')
CS2_2_f=CS2_2_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_2_f.columns = CS2_2_f.columns.droplevel(0)
CS2_2_f = CS2_2_f.loc[:, ~CS2_2_f.columns.str.contains('^Unnamed')]

CS2_3_f=CS2_3.pivot(index =CS2_3.index, columns ='Unnamed: 0')
CS2_3_f=CS2_3_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_3_f.columns = CS2_3_f.columns.droplevel(0)
CS2_3_f = CS2_3_f.loc[:, ~CS2_3_f.columns.str.contains('^Unnamed')]

CS2_4_f=CS2_4.pivot(index =CS2_4.index, columns ='Unnamed: 0')
CS2_4_f=CS2_4_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_4_f.columns = CS2_4_f.columns.droplevel(0)
CS2_4_f = CS2_4_f.loc[:, ~CS2_4_f.columns.str.contains('^Unnamed')]

CS2_5_f=CS2_5.pivot(index =CS2_5.index, columns ='Unnamed: 0')
CS2_5_f=CS2_5_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_5_f.columns = CS2_5_f.columns.droplevel(0)
CS2_5_f = CS2_5_f.loc[:, ~CS2_5_f.columns.str.contains('^Unnamed')]

CS2_6_f=CS2_6.pivot(index =CS2_6.index, columns ='Unnamed: 0')
CS2_6_f=CS2_6_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_6_f.columns = CS2_6_f.columns.droplevel(0)
CS2_6_f = CS2_6_f.loc[:, ~CS2_6_f.columns.str.contains('^Unnamed')]

CS2_7_f=CS2_7.pivot(index =CS2_7.index, columns ='Unnamed: 0')
CS2_7_f=CS2_7_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_7_f.columns = CS2_7_f.columns.droplevel(0)
CS2_7_f = CS2_7_f.loc[:, ~CS2_7_f.columns.str.contains('^Unnamed')]

CS2_8_f=CS2_8.pivot(index =CS2_8.index, columns ='Unnamed: 0')
CS2_8_f=CS2_8_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_8_f.columns = CS2_8_f.columns.droplevel(0)
CS2_8_f = CS2_8_f.loc[:, ~CS2_8_f.columns.str.contains('^Unnamed')]

CS2_9_f=CS2_9.pivot(index =CS2_9.index, columns ='Unnamed: 0')
CS2_9_f=CS2_9_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_9_f.columns = CS2_9_f.columns.droplevel(0)
CS2_9_f = CS2_9_f.loc[:, ~CS2_9_f.columns.str.contains('^Unnamed')]

CS2_10_f=CS2_10.pivot(index =CS2_10.index, columns ='Unnamed: 0')
CS2_10_f=CS2_10_f.apply(lambda x: pd.Series(x.dropna().values))
CS2_10_f.columns = CS2_10_f.columns.droplevel(0)
CS2_10_f = CS2_10_f.loc[:, ~CS2_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([CS2_0_f,CS2_005_f,CS2_01_f,CS2_015_f,CS2_02_f,CS2_025_f,CS2_03_f,CS2_035_f,CS2_04_f,CS2_045_f,CS2_05_f,CS2_1_f,CS2_2_f,CS2_3_f,CS2_4_f,CS2_5_f,CS2_6_f,CS2_7_f,CS2_8_f,CS2_9_f,CS2_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('CS2.csv', header=True)