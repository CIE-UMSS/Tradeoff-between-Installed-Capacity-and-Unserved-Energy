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
CS1_0=pd.read_csv('CS1_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_005=pd.read_csv('CS1_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_01=pd.read_csv('CS1_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_015=pd.read_csv('CS1_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_02=pd.read_csv('CS1_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_025=pd.read_csv('CS1_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_03=pd.read_csv('CS1_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_035=pd.read_csv('CS1_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_04=pd.read_csv('CS1_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_045=pd.read_csv('CS1_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_05=pd.read_csv('CS1_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_1=pd.read_csv('CS1_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_2=pd.read_csv('CS1_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_3=pd.read_csv('CS1_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_4=pd.read_csv('CS1_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_5=pd.read_csv('CS1_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_6=pd.read_csv('CS1_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_7=pd.read_csv('CS1_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_8=pd.read_csv('CS1_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_9=pd.read_csv('CS1_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS1_10=pd.read_csv('CS1_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

CS1_0_f=CS1_0.pivot(index =CS1_005.index, columns ='Unnamed: 0')
CS1_0_f=CS1_0_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_0_f.columns = CS1_0_f.columns.droplevel(0)
CS1_0_f = CS1_0_f.loc[:, ~CS1_0_f.columns.str.contains('^Unnamed')]

CS1_005_f=CS1_005.pivot(index =CS1_005.index, columns ='Unnamed: 0')
CS1_005_f=CS1_005_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_005_f.columns = CS1_005_f.columns.droplevel(0)
CS1_005_f = CS1_005_f.loc[:, ~CS1_005_f.columns.str.contains('^Unnamed')]

CS1_01_f=CS1_01.pivot(index =CS1_01.index, columns ='Unnamed: 0')
CS1_01_f=CS1_01_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_01_f.columns = CS1_01_f.columns.droplevel(0)
CS1_01_f = CS1_01_f.loc[:, ~CS1_01_f.columns.str.contains('^Unnamed')]

CS1_015_f=CS1_015.pivot(index =CS1_015.index, columns ='Unnamed: 0')
CS1_015_f=CS1_015_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_015_f.columns = CS1_015_f.columns.droplevel(0)
CS1_015_f = CS1_015_f.loc[:, ~CS1_015_f.columns.str.contains('^Unnamed')]

CS1_02_f=CS1_02.pivot(index =CS1_02.index, columns ='Unnamed: 0')
CS1_02_f=CS1_02_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_02_f.columns = CS1_02_f.columns.droplevel(0)
CS1_02_f = CS1_02_f.loc[:, ~CS1_02_f.columns.str.contains('^Unnamed')]

CS1_025_f=CS1_025.pivot(index =CS1_025.index, columns ='Unnamed: 0')
CS1_025_f=CS1_025_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_025_f.columns = CS1_025_f.columns.droplevel(0)
CS1_025_f = CS1_025_f.loc[:, ~CS1_025_f.columns.str.contains('^Unnamed')]

CS1_03_f=CS1_03.pivot(index =CS1_03.index, columns ='Unnamed: 0')
CS1_03_f=CS1_03_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_03_f.columns = CS1_03_f.columns.droplevel(0)
CS1_03_f = CS1_03_f.loc[:, ~CS1_03_f.columns.str.contains('^Unnamed')]

CS1_035_f=CS1_035.pivot(index =CS1_035.index, columns ='Unnamed: 0')
CS1_035_f=CS1_035_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_035_f.columns = CS1_035_f.columns.droplevel(0)
CS1_035_f = CS1_035_f.loc[:, ~CS1_035_f.columns.str.contains('^Unnamed')]

CS1_04_f=CS1_04.pivot(index =CS1_04.index, columns ='Unnamed: 0')
CS1_04_f=CS1_04_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_04_f.columns = CS1_04_f.columns.droplevel(0)
CS1_04_f = CS1_04_f.loc[:, ~CS1_04_f.columns.str.contains('^Unnamed')]

CS1_045_f=CS1_045.pivot(index =CS1_045.index, columns ='Unnamed: 0')
CS1_045_f=CS1_045_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_045_f.columns = CS1_045_f.columns.droplevel(0)
CS1_045_f = CS1_045_f.loc[:, ~CS1_045_f.columns.str.contains('^Unnamed')]

CS1_05_f=CS1_05.pivot(index =CS1_05.index, columns ='Unnamed: 0')
CS1_05_f=CS1_05_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_05_f.columns = CS1_05_f.columns.droplevel(0)
CS1_05_f = CS1_05_f.loc[:, ~CS1_05_f.columns.str.contains('^Unnamed')]

CS1_1_f=CS1_1.pivot(index =CS1_1.index, columns ='Unnamed: 0')
CS1_1_f=CS1_1_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_1_f.columns = CS1_1_f.columns.droplevel(0)
CS1_1_f = CS1_1_f.loc[:, ~CS1_1_f.columns.str.contains('^Unnamed')]

CS1_2_f=CS1_2.pivot(index =CS1_2.index, columns ='Unnamed: 0')
CS1_2_f=CS1_2_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_2_f.columns = CS1_2_f.columns.droplevel(0)
CS1_2_f = CS1_2_f.loc[:, ~CS1_2_f.columns.str.contains('^Unnamed')]

CS1_3_f=CS1_3.pivot(index =CS1_3.index, columns ='Unnamed: 0')
CS1_3_f=CS1_3_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_3_f.columns = CS1_3_f.columns.droplevel(0)
CS1_3_f = CS1_3_f.loc[:, ~CS1_3_f.columns.str.contains('^Unnamed')]

CS1_4_f=CS1_4.pivot(index =CS1_4.index, columns ='Unnamed: 0')
CS1_4_f=CS1_4_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_4_f.columns = CS1_4_f.columns.droplevel(0)
CS1_4_f = CS1_4_f.loc[:, ~CS1_4_f.columns.str.contains('^Unnamed')]

CS1_5_f=CS1_5.pivot(index =CS1_5.index, columns ='Unnamed: 0')
CS1_5_f=CS1_5_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_5_f.columns = CS1_5_f.columns.droplevel(0)
CS1_5_f = CS1_5_f.loc[:, ~CS1_5_f.columns.str.contains('^Unnamed')]

CS1_6_f=CS1_6.pivot(index =CS1_6.index, columns ='Unnamed: 0')
CS1_6_f=CS1_6_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_6_f.columns = CS1_6_f.columns.droplevel(0)
CS1_6_f = CS1_6_f.loc[:, ~CS1_6_f.columns.str.contains('^Unnamed')]

CS1_7_f=CS1_7.pivot(index =CS1_7.index, columns ='Unnamed: 0')
CS1_7_f=CS1_7_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_7_f.columns = CS1_7_f.columns.droplevel(0)
CS1_7_f = CS1_7_f.loc[:, ~CS1_7_f.columns.str.contains('^Unnamed')]

CS1_8_f=CS1_8.pivot(index =CS1_8.index, columns ='Unnamed: 0')
CS1_8_f=CS1_8_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_8_f.columns = CS1_8_f.columns.droplevel(0)
CS1_8_f = CS1_8_f.loc[:, ~CS1_8_f.columns.str.contains('^Unnamed')]

CS1_9_f=CS1_9.pivot(index =CS1_9.index, columns ='Unnamed: 0')
CS1_9_f=CS1_9_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_9_f.columns = CS1_9_f.columns.droplevel(0)
CS1_9_f = CS1_9_f.loc[:, ~CS1_9_f.columns.str.contains('^Unnamed')]

CS1_10_f=CS1_10.pivot(index =CS1_10.index, columns ='Unnamed: 0')
CS1_10_f=CS1_10_f.apply(lambda x: pd.Series(x.dropna().values))
CS1_10_f.columns = CS1_10_f.columns.droplevel(0)
CS1_10_f = CS1_10_f.loc[:, ~CS1_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([CS1_0_f,CS1_005_f,CS1_01_f,CS1_015_f,CS1_02_f,CS1_025_f,CS1_03_f,CS1_035_f,CS1_04_f,CS1_045_f,CS1_05_f,CS1_1_f,CS1_2_f,CS1_3_f,CS1_4_f,CS1_5_f,CS1_6_f,CS1_7_f,CS1_8_f,CS1_9_f,CS1_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('CS1.csv', header=True)