#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""

@author: Alejandro Soto
"""


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

HI_Radio = HI.Appliance(HI,1,7,1,280,0.3,110)
HI_Radio.windows([420,708],[0,0])

#tv
HI_TV = HI.Appliance(HI,1,60,3,300,0.38,114)
HI_TV.windows([1140,1440],[651,1139],0.35,[300,650])

#phone charger
HI_Phone_charger = HI.Appliance(HI,2,5,3,250,0.4,95)
HI_Phone_charger.windows([1190,1440],[0,420],0.35,[421,1189])

#water_heater
HI_Water_heater = HI.Appliance(HI,1,150,1,60,0.05,30)
HI_Water_heater.windows([0,1440],[0,0])

#fridge
HI_Fridge = HI.Appliance(HI,1,200,1,1440,0,30,'yes',3)
HI_Fridge.windows([0,1440],[0,0])
HI_Fridge.specific_cycle_1(200,20,5,10)
HI_Fridge.specific_cycle_2(200,15,5,15)
HI_Fridge.specific_cycle_3(200,10,5,20)
HI_Fridge.cycle_behaviour([0,0],[0,0],[0,420],[1050,1440],[421,1049],[0,0])

#freezer
HI_Freezer = HI.Appliance(HI,1,200,1,1440,0,30,'yes',3)
HI_Freezer.windows([0,1440],[0,0])
HI_Freezer.specific_cycle_1(200,20,5,10)
HI_Freezer.specific_cycle_2(200,15,5,15)
HI_Freezer.specific_cycle_3(200,10,5,20)
HI_Freezer.cycle_behaviour([0,0],[0,0],[0,0],[0,0],[0,0],[0,1440])

#welder 
HI_Welder = HI.Appliance(HI,1,5500,1,60,0.5,30,occasional_use = 0.3)
HI_Welder.windows([360,1080],[0,0])

#grinder
HI_Grinder = HI.Appliance(HI,1,750,1,480,0.125,60,occasional_use = 0.3)
HI_Grinder.windows([360,1080],[0,0])

#dryer
HI_Dryer = HI.Appliance(HI,1,750,1,60,0.5,30,occasional_use = 0.3)
HI_Dryer.windows([360,1080],[0,0])

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


