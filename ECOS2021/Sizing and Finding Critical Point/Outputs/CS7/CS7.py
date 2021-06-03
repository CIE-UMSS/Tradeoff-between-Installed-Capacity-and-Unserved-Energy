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
CS7_0=pd.read_csv('CS7_0.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_005=pd.read_csv('CS7_005.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_01=pd.read_csv('CS7_01.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_015=pd.read_csv('CS7_015.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_02=pd.read_csv('CS7_02.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_025=pd.read_csv('CS7_025.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_03=pd.read_csv('CS7_03.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_035=pd.read_csv('CS7_035.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_04=pd.read_csv('CS7_04.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_045=pd.read_csv('CS7_045.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_05=pd.read_csv('CS7_05.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_1=pd.read_csv('CS7_1.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_2=pd.read_csv('CS7_2.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_3=pd.read_csv('CS7_3.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_4=pd.read_csv('CS7_4.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_5=pd.read_csv('CS7_5.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_6=pd.read_csv('CS7_6.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_7=pd.read_csv('CS7_7.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_8=pd.read_csv('CS7_8.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_9=pd.read_csv('CS7_9.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)
CS7_10=pd.read_csv('CS7_10.csv', sep=',', decimal=',', encoding='latin1', error_bad_lines=False)

CS7_0_f=CS7_0.pivot(index =CS7_005.index, columns ='Unnamed: 0')
CS7_0_f=CS7_0_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_0_f.columns = CS7_0_f.columns.droplevel(0)
CS7_0_f = CS7_0_f.loc[:, ~CS7_0_f.columns.str.contains('^Unnamed')]

CS7_005_f=CS7_005.pivot(index =CS7_005.index, columns ='Unnamed: 0')
CS7_005_f=CS7_005_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_005_f.columns = CS7_005_f.columns.droplevel(0)
CS7_005_f = CS7_005_f.loc[:, ~CS7_005_f.columns.str.contains('^Unnamed')]

CS7_01_f=CS7_01.pivot(index =CS7_01.index, columns ='Unnamed: 0')
CS7_01_f=CS7_01_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_01_f.columns = CS7_01_f.columns.droplevel(0)
CS7_01_f = CS7_01_f.loc[:, ~CS7_01_f.columns.str.contains('^Unnamed')]

CS7_015_f=CS7_015.pivot(index =CS7_015.index, columns ='Unnamed: 0')
CS7_015_f=CS7_015_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_015_f.columns = CS7_015_f.columns.droplevel(0)
CS7_015_f = CS7_015_f.loc[:, ~CS7_015_f.columns.str.contains('^Unnamed')]

CS7_02_f=CS7_02.pivot(index =CS7_02.index, columns ='Unnamed: 0')
CS7_02_f=CS7_02_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_02_f.columns = CS7_02_f.columns.droplevel(0)
CS7_02_f = CS7_02_f.loc[:, ~CS7_02_f.columns.str.contains('^Unnamed')]

CS7_025_f=CS7_025.pivot(index =CS7_025.index, columns ='Unnamed: 0')
CS7_025_f=CS7_025_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_025_f.columns = CS7_025_f.columns.droplevel(0)
CS7_025_f = CS7_025_f.loc[:, ~CS7_025_f.columns.str.contains('^Unnamed')]

CS7_03_f=CS7_03.pivot(index =CS7_03.index, columns ='Unnamed: 0')
CS7_03_f=CS7_03_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_03_f.columns = CS7_03_f.columns.droplevel(0)
CS7_03_f = CS7_03_f.loc[:, ~CS7_03_f.columns.str.contains('^Unnamed')]

CS7_035_f=CS7_035.pivot(index =CS7_035.index, columns ='Unnamed: 0')
CS7_035_f=CS7_035_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_035_f.columns = CS7_035_f.columns.droplevel(0)
CS7_035_f = CS7_035_f.loc[:, ~CS7_035_f.columns.str.contains('^Unnamed')]

CS7_04_f=CS7_04.pivot(index =CS7_04.index, columns ='Unnamed: 0')
CS7_04_f=CS7_04_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_04_f.columns = CS7_04_f.columns.droplevel(0)
CS7_04_f = CS7_04_f.loc[:, ~CS7_04_f.columns.str.contains('^Unnamed')]

CS7_045_f=CS7_045.pivot(index =CS7_045.index, columns ='Unnamed: 0')
CS7_045_f=CS7_045_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_045_f.columns = CS7_045_f.columns.droplevel(0)
CS7_045_f = CS7_045_f.loc[:, ~CS7_045_f.columns.str.contains('^Unnamed')]

CS7_05_f=CS7_05.pivot(index =CS7_05.index, columns ='Unnamed: 0')
CS7_05_f=CS7_05_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_05_f.columns = CS7_05_f.columns.droplevel(0)
CS7_05_f = CS7_05_f.loc[:, ~CS7_05_f.columns.str.contains('^Unnamed')]

CS7_1_f=CS7_1.pivot(index =CS7_1.index, columns ='Unnamed: 0')
CS7_1_f=CS7_1_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_1_f.columns = CS7_1_f.columns.droplevel(0)
CS7_1_f = CS7_1_f.loc[:, ~CS7_1_f.columns.str.contains('^Unnamed')]

CS7_2_f=CS7_2.pivot(index =CS7_2.index, columns ='Unnamed: 0')
CS7_2_f=CS7_2_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_2_f.columns = CS7_2_f.columns.droplevel(0)
CS7_2_f = CS7_2_f.loc[:, ~CS7_2_f.columns.str.contains('^Unnamed')]

CS7_3_f=CS7_3.pivot(index =CS7_3.index, columns ='Unnamed: 0')
CS7_3_f=CS7_3_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_3_f.columns = CS7_3_f.columns.droplevel(0)
CS7_3_f = CS7_3_f.loc[:, ~CS7_3_f.columns.str.contains('^Unnamed')]

CS7_4_f=CS7_4.pivot(index =CS7_4.index, columns ='Unnamed: 0')
CS7_4_f=CS7_4_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_4_f.columns = CS7_4_f.columns.droplevel(0)
CS7_4_f = CS7_4_f.loc[:, ~CS7_4_f.columns.str.contains('^Unnamed')]

CS7_5_f=CS7_5.pivot(index =CS7_5.index, columns ='Unnamed: 0')
CS7_5_f=CS7_5_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_5_f.columns = CS7_5_f.columns.droplevel(0)
CS7_5_f = CS7_5_f.loc[:, ~CS7_5_f.columns.str.contains('^Unnamed')]

CS7_6_f=CS7_6.pivot(index =CS7_6.index, columns ='Unnamed: 0')
CS7_6_f=CS7_6_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_6_f.columns = CS7_6_f.columns.droplevel(0)
CS7_6_f = CS7_6_f.loc[:, ~CS7_6_f.columns.str.contains('^Unnamed')]

CS7_7_f=CS7_7.pivot(index =CS7_7.index, columns ='Unnamed: 0')
CS7_7_f=CS7_7_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_7_f.columns = CS7_7_f.columns.droplevel(0)
CS7_7_f = CS7_7_f.loc[:, ~CS7_7_f.columns.str.contains('^Unnamed')]

CS7_8_f=CS7_8.pivot(index =CS7_8.index, columns ='Unnamed: 0')
CS7_8_f=CS7_8_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_8_f.columns = CS7_8_f.columns.droplevel(0)
CS7_8_f = CS7_8_f.loc[:, ~CS7_8_f.columns.str.contains('^Unnamed')]

CS7_9_f=CS7_9.pivot(index =CS7_9.index, columns ='Unnamed: 0')
CS7_9_f=CS7_9_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_9_f.columns = CS7_9_f.columns.droplevel(0)
CS7_9_f = CS7_9_f.loc[:, ~CS7_9_f.columns.str.contains('^Unnamed')]

CS7_10_f=CS7_10.pivot(index =CS7_10.index, columns ='Unnamed: 0')
CS7_10_f=CS7_10_f.apply(lambda x: pd.Series(x.dropna().values))
CS7_10_f.columns = CS7_10_f.columns.droplevel(0)
CS7_10_f = CS7_10_f.loc[:, ~CS7_10_f.columns.str.contains('^Unnamed')]


p=pd.concat([CS7_0_f,CS7_005_f,CS7_01_f,CS7_015_f,CS7_02_f,CS7_025_f,CS7_03_f,CS7_035_f,CS7_04_f,CS7_045_f,CS7_05_f,CS7_1_f,CS7_2_f,CS7_3_f,CS7_4_f,CS7_5_f,CS7_6_f,CS7_7_f,CS7_8_f,CS7_9_f,CS7_10_f])
p.reset_index(drop=True, inplace=True)
p['LLC']=[0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p.to_csv ('CS7.csv', header=True)