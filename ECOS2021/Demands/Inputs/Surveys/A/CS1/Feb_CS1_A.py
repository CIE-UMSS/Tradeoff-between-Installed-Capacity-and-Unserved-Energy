#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Jan 31 14:33:07 2020

@author: alejandrosoto
Script for 2 class of household in Raqaypampa.

"""


# -*- coding: utf-8 -*-
"""

@author: Alejandro Soto
"""

'''
First array = Intensive cycle
Second array = INtermediate cycle
Thrird array = Standard cycle

Hot months: [0,0],[0,0],[0,1400],[0,0],[0,0],[0,0] Aug
Warm months: [0,0],[0,0],[480,1200],[0,0],[0,299],[1201,1440] feb,march,apr,jun,july,nov,dec
Cold months: [0,0],[0,0],[301,1200],[0,0],[0,299],[1201,1440] Jan,sep
Rainny months: [0,0],[0,0],[480,1200],[0,0],[0,299],[1201,1440] oct 


Feb-Oct: Schools*
Mixer IN the HI just on the January
2 Freezer in the HI runs on the spring (Oct-Dec)
'''

from core import User, np
User_list = []
#User classes definition

HI = User("high income",1)
User_list.append(HI)


LI = User("low income",0)
User_list.append(LI)





#High-Income
#indoor bulb
HI_indoor_bulb = HI.Appliance(HI,3,7,1,320,0.6,190)
HI_indoor_bulb.windows([1080,1440],[0,0])
#outdoor bulb

HI_outdoor_bulb = HI.Appliance(HI,1,13,1,340,0.1,300)
HI_outdoor_bulb.windows([1100,1440],[0,0])

HI_Radio = HI.Appliance(HI,1,7,1,305,0.3,110)
HI_Radio.windows([420,1050],[0,0])
#phone charger
HI_Phone_charger = HI.Appliance(HI,2,5,3,250,0.4,95)
HI_Phone_charger.windows([1190,1440],[0,420],0.35,[421,1189])

#water_heater
HI_Water_heater = HI.Appliance(HI,1,150,1,60,0.05,30)
HI_Water_heater.windows([0,1440],[0,0])


#Lower Income
#indoor bulb
LI_indoor_bulb = LI.Appliance(LI,3,7,2,287,0.4,124)
LI_indoor_bulb.windows([1153,1440],[0,300],0.5)

#outdoor bulb
LI_outdoor_bulb = LI.Appliance(LI,1,13,1,243,0.3,71)
LI_outdoor_bulb.windows([1197,1440],[0,0])

#radio
LI_Radio = LI.Appliance(LI,1,7,2,160,0.3,49)
LI_Radio.windows([480,840],[841,1200],0.5)

#TV
LI_TV = LI.Appliance(LI,1,100,3,250,0.3,74)
LI_TV.windows([1170,1420],[551,1169],0.3,[300,550])

#phone charger
LI_Phone_charger = LI.Appliance(LI,2,5,3,200,0.4,82)
LI_Phone_charger.windows([1020,1440],[0,420],0.3,[720,1019])


