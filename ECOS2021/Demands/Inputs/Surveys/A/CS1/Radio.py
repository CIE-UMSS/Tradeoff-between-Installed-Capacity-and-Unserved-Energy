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


'''

Base scenario (BSA): Indoor bulb (3), outdoor bulb (1), radio (1), tv (1), phone charger (2), Water Heater (1), Mixer (1)
Base scenario (B): Indoor bulb (3), outdoor bulb (1), radio (1), tv (1), phone charger (2)

A
Scenario 1: BSA + Fridge (1) + Freezer* (1).
Scenario 2: BSA + Fridge (1).
Scenario 3: BSA + Fridge (1)*.
Scenario 4: BSA + Freezer (1).
Scenario 5: BSA + Wheler (1).
Scerario 6: BSA + Grinder (1).
Scanerio 7: Add + Dryer (1),
Scenario 9: All

B
Scenario 8: BSB + Water Heater** (1).
Scenario 10: BSA + Pump Water (1).
Scenario 11: BSA + DVD (1).
Scenario 12: BSA + Blender (1).
Scenario 13: BSA + Iron (1).
Scerario 14: BSA + Mill (1).

* With seasonal variation
** Occasional use

Cold Months: May-Aug Std Cycle 8:00-18:00 Above 10 degrees
Warm Months: Jan-Apr Std Cycle 0:00-23:59 Above 10 degrees 
Hot Nonths: Sep-Dec  Std Cycle 0:00-10:00; 15:01-23:59 Above 10 degrees 
                    Int Cycle 10:01-15:00
'''

#A
#indoor bulb
#1
HI_Radio = HI.Appliance(HI,1,7,1,305,0.3,110)
HI_Radio.windows([420,1050],[0,0])
#2
HI_Radio = HI.Appliance(HI,1,7,1,330,0.3,110)
HI_Radio.windows([420,1050],[0,0])

HI_Radio = HI.Appliance(HI,1,7,1,355,0.3,110)
HI_Radio.windows([420,1050],[0,0])
'''
HI_Radio = HI.Appliance(HI,1,7,1,280,0.3,110)
HI_Radio.windows([420,708],[0,0])
'''


#B
#indoor bulb
LI_indoor_bulb = LI.Appliance(LI,3,7,2,287,0.4,124)
LI_indoor_bulb.windows([1153,1440],[0,300],0.5)

#outdoor bulb
LI_outdoor_bulb = LI.Appliance(LI,1,13,1,243,0.3,71)
LI_outdoor_bulb.windows([1197,1440],[0,0])

#radio
LI_Radio = LI.Appliance(LI,1,7,2,160,0.3,49)
LI_Radio.windows([480,840],[841,1200],0.5)

#radio
LI_Radio = LI.Appliance(LI,1,7,1,160,0.3,49)
LI_Radio.windows([420,1050],[0,0])

#TV
LI_TV = LI.Appliance(LI,1,100,3,250,0.3,74)
LI_TV.windows([1170,1420],[551,1169],0.3,[300,550])

#phone charger
LI_Phone_charger = LI.Appliance(LI,2,5,3,200,0.4,82)
LI_Phone_charger.windows([1020,1440],[0,420],0.3,[720,1019])


