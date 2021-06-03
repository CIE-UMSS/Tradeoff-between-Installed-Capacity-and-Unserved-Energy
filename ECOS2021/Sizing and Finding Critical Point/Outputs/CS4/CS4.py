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
CS4_0=pd.read_csv('CS4_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_005=pd.read_csv('CS4_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_01=pd.read_csv('CS4_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_015=pd.read_csv('CS4_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_02=pd.read_csv('CS4_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_025=pd.read_csv('CS4_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_03=pd.read_csv('CS4_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_035=pd.read_csv('CS4_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_04=pd.read_csv('CS4_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_045=pd.read_csv('CS4_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_05=pd.read_csv('CS4_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_1=pd.read_csv('CS4_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_2=pd.read_csv('CS4_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_3=pd.read_csv('CS4_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_4=pd.read_csv('CS4_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_5=pd.read_csv('CS4_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_6=pd.read_csv('CS4_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_7=pd.read_csv('CS4_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_8=pd.read_csv('CS4_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_9=pd.read_csv('CS4_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS4_10=pd.read_csv('CS4_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

CS4_0_f=CS4_0.pivot(index =CS4_005.index, columns ='Unnamed: 0')
CS4_0_f=CS4_0_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_0_f.columns = CS4_0_f.columns.droplevel(0)
CS4_0_f = CS4_0_f.loc[:, ~CS4_0_f.columns.str.contains('^Unnamed')]

CS4_005_f=CS4_005.pivot(index =CS4_005.index, columns ='Unnamed: 0')
CS4_005_f=CS4_005_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_005_f.columns = CS4_005_f.columns.droplevel(0)
CS4_005_f = CS4_005_f.loc[:, ~CS4_005_f.columns.str.contains('^Unnamed')]

CS4_01_f=CS4_01.pivot(index =CS4_01.index, columns ='Unnamed: 0')
CS4_01_f=CS4_01_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_01_f.columns = CS4_01_f.columns.droplevel(0)
CS4_01_f = CS4_01_f.loc[:, ~CS4_01_f.columns.str.contains('^Unnamed')]

CS4_015_f=CS4_015.pivot(index =CS4_015.index, columns ='Unnamed: 0')
CS4_015_f=CS4_015_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_015_f.columns = CS4_015_f.columns.droplevel(0)
CS4_015_f = CS4_015_f.loc[:, ~CS4_015_f.columns.str.contains('^Unnamed')]

CS4_02_f=CS4_02.pivot(index =CS4_02.index, columns ='Unnamed: 0')
CS4_02_f=CS4_02_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_02_f.columns = CS4_02_f.columns.droplevel(0)
CS4_02_f = CS4_02_f.loc[:, ~CS4_02_f.columns.str.contains('^Unnamed')]

CS4_025_f=CS4_025.pivot(index =CS4_025.index, columns ='Unnamed: 0')
CS4_025_f=CS4_025_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_025_f.columns = CS4_025_f.columns.droplevel(0)
CS4_025_f = CS4_025_f.loc[:, ~CS4_025_f.columns.str.contains('^Unnamed')]

CS4_03_f=CS4_03.pivot(index =CS4_03.index, columns ='Unnamed: 0')
CS4_03_f=CS4_03_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_03_f.columns = CS4_03_f.columns.droplevel(0)
CS4_03_f = CS4_03_f.loc[:, ~CS4_03_f.columns.str.contains('^Unnamed')]

CS4_035_f=CS4_035.pivot(index =CS4_035.index, columns ='Unnamed: 0')
CS4_035_f=CS4_035_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_035_f.columns = CS4_035_f.columns.droplevel(0)
CS4_035_f = CS4_035_f.loc[:, ~CS4_035_f.columns.str.contains('^Unnamed')]

CS4_04_f=CS4_04.pivot(index =CS4_04.index, columns ='Unnamed: 0')
CS4_04_f=CS4_04_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_04_f.columns = CS4_04_f.columns.droplevel(0)
CS4_04_f = CS4_04_f.loc[:, ~CS4_04_f.columns.str.contains('^Unnamed')]

CS4_045_f=CS4_045.pivot(index =CS4_045.index, columns ='Unnamed: 0')
CS4_045_f=CS4_045_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_045_f.columns = CS4_045_f.columns.droplevel(0)
CS4_045_f = CS4_045_f.loc[:, ~CS4_045_f.columns.str.contains('^Unnamed')]

CS4_05_f=CS4_05.pivot(index =CS4_05.index, columns ='Unnamed: 0')
CS4_05_f=CS4_05_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_05_f.columns = CS4_05_f.columns.droplevel(0)
CS4_05_f = CS4_05_f.loc[:, ~CS4_05_f.columns.str.contains('^Unnamed')]

CS4_1_f=CS4_1.pivot(index =CS4_1.index, columns ='Unnamed: 0')
CS4_1_f=CS4_1_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_1_f.columns = CS4_1_f.columns.droplevel(0)
CS4_1_f = CS4_1_f.loc[:, ~CS4_1_f.columns.str.contains('^Unnamed')]

CS4_2_f=CS4_2.pivot(index =CS4_2.index, columns ='Unnamed: 0')
CS4_2_f=CS4_2_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_2_f.columns = CS4_2_f.columns.droplevel(0)
CS4_2_f = CS4_2_f.loc[:, ~CS4_2_f.columns.str.contains('^Unnamed')]

CS4_3_f=CS4_3.pivot(index =CS4_3.index, columns ='Unnamed: 0')
CS4_3_f=CS4_3_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_3_f.columns = CS4_3_f.columns.droplevel(0)
CS4_3_f = CS4_3_f.loc[:, ~CS4_3_f.columns.str.contains('^Unnamed')]

CS4_4_f=CS4_4.pivot(index =CS4_4.index, columns ='Unnamed: 0')
CS4_4_f=CS4_4_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_4_f.columns = CS4_4_f.columns.droplevel(0)
CS4_4_f = CS4_4_f.loc[:, ~CS4_4_f.columns.str.contains('^Unnamed')]

CS4_5_f=CS4_5.pivot(index =CS4_5.index, columns ='Unnamed: 0')
CS4_5_f=CS4_5_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_5_f.columns = CS4_5_f.columns.droplevel(0)
CS4_5_f = CS4_5_f.loc[:, ~CS4_5_f.columns.str.contains('^Unnamed')]

CS4_6_f=CS4_6.pivot(index =CS4_6.index, columns ='Unnamed: 0')
CS4_6_f=CS4_6_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_6_f.columns = CS4_6_f.columns.droplevel(0)
CS4_6_f = CS4_6_f.loc[:, ~CS4_6_f.columns.str.contains('^Unnamed')]

CS4_7_f=CS4_7.pivot(index =CS4_7.index, columns ='Unnamed: 0')
CS4_7_f=CS4_7_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_7_f.columns = CS4_7_f.columns.droplevel(0)
CS4_7_f = CS4_7_f.loc[:, ~CS4_7_f.columns.str.contains('^Unnamed')]

CS4_8_f=CS4_8.pivot(index =CS4_8.index, columns ='Unnamed: 0')
CS4_8_f=CS4_8_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_8_f.columns = CS4_8_f.columns.droplevel(0)
CS4_8_f = CS4_8_f.loc[:, ~CS4_8_f.columns.str.contains('^Unnamed')]

CS4_9_f=CS4_9.pivot(index =CS4_9.index, columns ='Unnamed: 0')
CS4_9_f=CS4_9_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_9_f.columns = CS4_9_f.columns.droplevel(0)
CS4_9_f = CS4_9_f.loc[:, ~CS4_9_f.columns.str.contains('^Unnamed')]

CS4_10_f=CS4_10.pivot(index =CS4_10.index, columns ='Unnamed: 0')
CS4_10_f=CS4_10_f.apply(lambda x: pd.Series(x.dropna().values))
CS4_10_f.columns = CS4_10_f.columns.droplevel(0)
CS4_10_f = CS4_10_f.loc[:, ~CS4_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([CS4_0_f,CS4_005_f,CS4_01_f,CS4_015_f,CS4_02_f,CS4_025_f,CS4_03_f,CS4_035_f,CS4_04_f,CS4_045_f,CS4_05_f,CS4_1_f,CS4_2_f,CS4_3_f,CS4_4_f,CS4_5_f,CS4_6_f,CS4_7_f,CS4_8_f,CS4_9_f,CS4_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('CS4.csv', header=True)