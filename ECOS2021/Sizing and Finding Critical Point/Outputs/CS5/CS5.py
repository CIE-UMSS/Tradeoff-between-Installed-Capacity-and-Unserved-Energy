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
CS5_0=pd.read_csv('CS5_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_005=pd.read_csv('CS5_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_01=pd.read_csv('CS5_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_015=pd.read_csv('CS5_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_02=pd.read_csv('CS5_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_025=pd.read_csv('CS5_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_03=pd.read_csv('CS5_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_035=pd.read_csv('CS5_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_04=pd.read_csv('CS5_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_045=pd.read_csv('CS5_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_05=pd.read_csv('CS5_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_1=pd.read_csv('CS5_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_2=pd.read_csv('CS5_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_3=pd.read_csv('CS5_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_4=pd.read_csv('CS5_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_5=pd.read_csv('CS5_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_6=pd.read_csv('CS5_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_7=pd.read_csv('CS5_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_8=pd.read_csv('CS5_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_9=pd.read_csv('CS5_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS5_10=pd.read_csv('CS5_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

CS5_0_f=CS5_0.pivot(index =CS5_005.index, columns ='Unnamed: 0')
CS5_0_f=CS5_0_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_0_f.columns = CS5_0_f.columns.droplevel(0)
CS5_0_f = CS5_0_f.loc[:, ~CS5_0_f.columns.str.contains('^Unnamed')]

CS5_005_f=CS5_005.pivot(index =CS5_005.index, columns ='Unnamed: 0')
CS5_005_f=CS5_005_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_005_f.columns = CS5_005_f.columns.droplevel(0)
CS5_005_f = CS5_005_f.loc[:, ~CS5_005_f.columns.str.contains('^Unnamed')]

CS5_01_f=CS5_01.pivot(index =CS5_01.index, columns ='Unnamed: 0')
CS5_01_f=CS5_01_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_01_f.columns = CS5_01_f.columns.droplevel(0)
CS5_01_f = CS5_01_f.loc[:, ~CS5_01_f.columns.str.contains('^Unnamed')]

CS5_015_f=CS5_015.pivot(index =CS5_015.index, columns ='Unnamed: 0')
CS5_015_f=CS5_015_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_015_f.columns = CS5_015_f.columns.droplevel(0)
CS5_015_f = CS5_015_f.loc[:, ~CS5_015_f.columns.str.contains('^Unnamed')]

CS5_02_f=CS5_02.pivot(index =CS5_02.index, columns ='Unnamed: 0')
CS5_02_f=CS5_02_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_02_f.columns = CS5_02_f.columns.droplevel(0)
CS5_02_f = CS5_02_f.loc[:, ~CS5_02_f.columns.str.contains('^Unnamed')]

CS5_025_f=CS5_025.pivot(index =CS5_025.index, columns ='Unnamed: 0')
CS5_025_f=CS5_025_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_025_f.columns = CS5_025_f.columns.droplevel(0)
CS5_025_f = CS5_025_f.loc[:, ~CS5_025_f.columns.str.contains('^Unnamed')]

CS5_03_f=CS5_03.pivot(index =CS5_03.index, columns ='Unnamed: 0')
CS5_03_f=CS5_03_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_03_f.columns = CS5_03_f.columns.droplevel(0)
CS5_03_f = CS5_03_f.loc[:, ~CS5_03_f.columns.str.contains('^Unnamed')]

CS5_035_f=CS5_035.pivot(index =CS5_035.index, columns ='Unnamed: 0')
CS5_035_f=CS5_035_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_035_f.columns = CS5_035_f.columns.droplevel(0)
CS5_035_f = CS5_035_f.loc[:, ~CS5_035_f.columns.str.contains('^Unnamed')]

CS5_04_f=CS5_04.pivot(index =CS5_04.index, columns ='Unnamed: 0')
CS5_04_f=CS5_04_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_04_f.columns = CS5_04_f.columns.droplevel(0)
CS5_04_f = CS5_04_f.loc[:, ~CS5_04_f.columns.str.contains('^Unnamed')]

CS5_045_f=CS5_045.pivot(index =CS5_045.index, columns ='Unnamed: 0')
CS5_045_f=CS5_045_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_045_f.columns = CS5_045_f.columns.droplevel(0)
CS5_045_f = CS5_045_f.loc[:, ~CS5_045_f.columns.str.contains('^Unnamed')]

CS5_05_f=CS5_05.pivot(index =CS5_05.index, columns ='Unnamed: 0')
CS5_05_f=CS5_05_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_05_f.columns = CS5_05_f.columns.droplevel(0)
CS5_05_f = CS5_05_f.loc[:, ~CS5_05_f.columns.str.contains('^Unnamed')]

CS5_1_f=CS5_1.pivot(index =CS5_1.index, columns ='Unnamed: 0')
CS5_1_f=CS5_1_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_1_f.columns = CS5_1_f.columns.droplevel(0)
CS5_1_f = CS5_1_f.loc[:, ~CS5_1_f.columns.str.contains('^Unnamed')]

CS5_2_f=CS5_2.pivot(index =CS5_2.index, columns ='Unnamed: 0')
CS5_2_f=CS5_2_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_2_f.columns = CS5_2_f.columns.droplevel(0)
CS5_2_f = CS5_2_f.loc[:, ~CS5_2_f.columns.str.contains('^Unnamed')]

CS5_3_f=CS5_3.pivot(index =CS5_3.index, columns ='Unnamed: 0')
CS5_3_f=CS5_3_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_3_f.columns = CS5_3_f.columns.droplevel(0)
CS5_3_f = CS5_3_f.loc[:, ~CS5_3_f.columns.str.contains('^Unnamed')]

CS5_4_f=CS5_4.pivot(index =CS5_4.index, columns ='Unnamed: 0')
CS5_4_f=CS5_4_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_4_f.columns = CS5_4_f.columns.droplevel(0)
CS5_4_f = CS5_4_f.loc[:, ~CS5_4_f.columns.str.contains('^Unnamed')]

CS5_5_f=CS5_5.pivot(index =CS5_5.index, columns ='Unnamed: 0')
CS5_5_f=CS5_5_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_5_f.columns = CS5_5_f.columns.droplevel(0)
CS5_5_f = CS5_5_f.loc[:, ~CS5_5_f.columns.str.contains('^Unnamed')]

CS5_6_f=CS5_6.pivot(index =CS5_6.index, columns ='Unnamed: 0')
CS5_6_f=CS5_6_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_6_f.columns = CS5_6_f.columns.droplevel(0)
CS5_6_f = CS5_6_f.loc[:, ~CS5_6_f.columns.str.contains('^Unnamed')]

CS5_7_f=CS5_7.pivot(index =CS5_7.index, columns ='Unnamed: 0')
CS5_7_f=CS5_7_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_7_f.columns = CS5_7_f.columns.droplevel(0)
CS5_7_f = CS5_7_f.loc[:, ~CS5_7_f.columns.str.contains('^Unnamed')]

CS5_8_f=CS5_8.pivot(index =CS5_8.index, columns ='Unnamed: 0')
CS5_8_f=CS5_8_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_8_f.columns = CS5_8_f.columns.droplevel(0)
CS5_8_f = CS5_8_f.loc[:, ~CS5_8_f.columns.str.contains('^Unnamed')]

CS5_9_f=CS5_9.pivot(index =CS5_9.index, columns ='Unnamed: 0')
CS5_9_f=CS5_9_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_9_f.columns = CS5_9_f.columns.droplevel(0)
CS5_9_f = CS5_9_f.loc[:, ~CS5_9_f.columns.str.contains('^Unnamed')]

CS5_10_f=CS5_10.pivot(index =CS5_10.index, columns ='Unnamed: 0')
CS5_10_f=CS5_10_f.apply(lambda x: pd.Series(x.dropna().values))
CS5_10_f.columns = CS5_10_f.columns.droplevel(0)
CS5_10_f = CS5_10_f.loc[:, ~CS5_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([CS5_0_f,CS5_005_f,CS5_01_f,CS5_015_f,CS5_02_f,CS5_025_f,CS5_03_f,CS5_035_f,CS5_04_f,CS5_045_f,CS5_05_f,CS5_1_f,CS5_2_f,CS5_3_f,CS5_4_f,CS5_5_f,CS5_6_f,CS5_7_f,CS5_8_f,CS5_9_f,CS5_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('CS5.csv', header=True)