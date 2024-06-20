# -*- coding: utf-8 -*-

#the main file for creating country-level future projections

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


#--import modules
import mod_read_input
import mod_CO2eq_future








#--run the model:
NDC = mod_read_input.read_ndc()
mod_CO2eq_future.process_ndc(NDC)


#1--collect scenario configuration

#2--estimate CO2eq for future time stamps

#3--estimate non-CO2 timeline

#4--estimate LULUCF timeline

#5--estimate CO2 timeline

#6--estimate CO2eq timeline

#7--estimate TCRE dT









#--keep the warnings silent
warnings.simplefilter("ignore", OptimizeWarning)






#--END--
