"""
PLAN B
A python class just in case my model is not working at 
all and I still
need to show some of my best results to the team
"""

"""
WARMING SOIL MODEL
===================
by Aline Lemos de Freitas


Based on Allison et al, 2010 create a warming soil model

Create dt as range from 0 to 30 years (in hours)

The model starts by setting the soil organic carbon (SOC),
dissolved organic carbon (DOC), microbial biomass, and enzyme pools
to their initial values. Microbial biomass changes
by the amount of DOC assimilated, times the carbon use
(or microbial growth) efficiency, minus
biomass death and enzyme production
"""
import numpy as np
import pandas as pd

# modeling the parameters that are regulated by the temperature
def temperature_regulating(params, temp):
    """
    Input: params: initial parameters as a dictionary
    temp: temperatura array varying from 20 to 25

    returns dataframe with temperature as index
    """
    df = {}
    df['km'] = params['km_slope'] * temp + params['km_0']
    df['v_max_uptake'] = params['v_max_uptake_0'] * \
        np.exp(-params['Ea_uptake']/(params['gas_const'] *(temp + 273)))

    df['km_uptake'] = params['km_uptake_slope'] * temp + params['km_uptake_0']
    df['cue'] = params['cue_slope'] * temp + params['cue_0']
    df = pd.DataFrame(df, index=temp)
    return df

def dynamics(df):
    """ 
    Adds a column to df with the assimilation values

    input:
    ----------
    df: DataFrame with initial temperature regulated parameters

    returns:
    ----------
    None. Add new column to input DataFrame
    """
    df['assim'] = df['v_max_uptake'] * mic * (doc/(df['km_uptake'] + doc))







