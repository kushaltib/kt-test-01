# -*- coding: utf-8 -*-

#--import python packages
import warnings
import sys
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.optimize import minimize, curve_fit, OptimizeWarning
import pathlib
import argparse
#

#--keep the warnings silent
warnings.simplefilter("ignore", OptimizeWarning)

def process_ndc(ndc_file,country_list=None):

    NDC = ndc_file
    
    #initialize empty arrays/list of countries:
    country_percent = []
    country_emissions = []
    country_co2eq_net_abs = []
    country_co2eq_net_int = []
    country_co2eq_excl_abs = []
    country_co2eq_excl_int = []
    country_co2_net_abs = []
    country_co2_net_int = []
    country_co2_excl_abs = []
    country_co2_excl_int = []
    country_no_target = []
  
    
    #choose the list of countries on which operation is to be carried out
    if country_list is None:
        country_list = NDC.index

    
    #generate a parsed country groupings based on target definitions    
    for country in country_list:
        if NDC.loc[country,'Target']=='Yes':
            if NDC.loc[country,'Target_applies_to']=='CO2' and NDC.loc[country,'Target_scope']=='Total-net' and NDC.loc[country,'Target_type']=='absolute':
                country_co2_net_abs.append(country)
            if NDC.loc[country,'Target_applies_to']=='CO2' and NDC.loc[country,'Target_scope']=='Total-net' and NDC.loc[country,'Target_type']=='intensity':
                country_co2_net_int.append(country)
            if NDC.loc[country,'Target_applies_to']=='CO2' and NDC.loc[country,'Target_scope']=='Total-excl' and NDC.loc[country,'Target_type']=='absolute':
                country_co2_excl_abs.append(country)
            if NDC.loc[country,'Target_applies_to']=='CO2' and NDC.loc[country,'Target_scope']=='Total-excl' and NDC.loc[country,'Target_type']=='intensity':
                country_co2_excl_int.append(country)

            if NDC.loc[country,'Target_applies_to']=='CO2eq' and NDC.loc[country,'Target_scope']=='Total-net' and NDC.loc[country,'Target_type']=='absolute':
                country_co2eq_net_abs.append(country)
            if NDC.loc[country,'Target_applies_to']=='CO2eq' and NDC.loc[country,'Target_scope']=='Total-net' and NDC.loc[country,'Target_type']=='intensity':
                country_co2eq_net_int.append(country)
            if NDC.loc[country,'Target_applies_to']=='CO2eq' and NDC.loc[country,'Target_scope']=='Total-excl' and NDC.loc[country,'Target_type']=='absolute':
                country_co2eq_excl_abs.append(country)
            if NDC.loc[country,'Target_applies_to']=='CO2eq' and NDC.loc[country,'Target_scope']=='Total-excl' and NDC.loc[country,'Target_type']=='intensity':
                country_co2eq_excl_int.append(country)

    cou_num = len(country_co2eq_net_abs)+len(country_co2eq_net_int)+len(country_co2eq_excl_abs)+len(country_co2eq_excl_int)+ \
              len(country_co2_net_abs)+len(country_co2_net_int)+len(country_co2_excl_abs)+len(country_co2_excl_int)
    
    print(country_co2eq_net_abs)

    print("Total countries in the list is: ",len(country_list),"\n",
          "Total countries in the NDC file is: ",len(NDC.index),"\n",
          "Total countries evaluated: ",cou_num,"\n",
           )
    


#--END--


