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

def read_ndc():
    
    #--read the NDC file
    NDC = pd.read_excel("D:/NDC-work/Approach_v2_June2024/NDCdata_As12Jun2024_Upd12Jun2024_v2.xlsx")
    NDC.drop(columns=['Categories'],inplace=True)
    NDC = NDC.T
    header_col = NDC.iloc[0]
    NDC = NDC[1:]
    NDC.columns = header_col

    return NDC
    



#--END--
