README

Each folder has the input and output files of each tool.

DEMAND:

-Inputs:

-Surveys:
Demand folder has the surveys info in a python file, and it is run complementary to RAMP tool described in:
https://orbi.uliege.be/bitstream/2268/235595/2/2019%20-%20Lombardi_Balderrama_Quoilin_Colombo%20-%20RAMP%20-%20Post-print_withDOI.pdf
(*)All files related for run the RAMP tool are shown in the previous paper by Lombardi

-Temperature data for power cycle in Raqaypampa:
All meteorological data was obtained from https://www.renewables.ninja/
(Info just for clasiffy the months through the year in Raqaypampa)

-Outputs:
"Plots" folder summarizes the average, occasional and atypical demand,  through the year for each household.
(**) In every scenario folder exists a .py file for change the time step.

SIZING AND FINDING THE CRITICAL POINT:

-Inputs:

-PV energy:

All meteorological data was obtained from https://www.renewables.ninja/ for Raqaypampa
 "lat": "-18.1891201"	 "lon": "-65.3847939"
"PV_Energy_pvlib" file for estimate the available energy on PV system (Single Diode Model)
"PV_treat" for the treatment of PV data

Demands:

Hourly demand time series for Raqaypampa obtained from RAMP.

-Outputs:

Results from "Microgrids.py" tool (all files related to running the tool are described and specificated on:
https://lirias.kuleuven.be/retrieve/559686)
Every folder has a file for find the critical point (best optimization) with a geometrical novel method on each techo-economic indicator.


RE-SIZING:

-Resuls folder:
SHS's characteristics for the best optimization (critical point). Output from Microgrid.py

-Plots:
The modular time series (each appliance, average demand and loss of load) are contrasted on every scenario. 






