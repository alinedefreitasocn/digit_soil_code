
import numpy as np
import pandas as pd

params = {
                'endtime': 24000000,
                'step_time': 240000,
                'temp_init': 20,
                'initSOC': 100,
                'initDOC': 0.5,
                'initMIC': 0.5,
                'initEnz': 0.01,
                'inputSOC': 0.0005,
                'inputDOC': 0.0005,
                'r_death': 0.0002,
                'r_enz_prod': 0.000005,
                'r_enz_loss': 0.001,
                'MICtoSOC': 0.5,
                'cue_0': 0.63,
                'cue_slope': -0.016,
                'v_max': 100000000,
                'v_max_uptake': 100000000,
                'km_0': 500,
                'km_uptake': 0.1,
                'km_slope': 5,
                'km_uptake_slope': 0.01,
                'Ea': 47,
                'Ea_uptake': 47,
                'gas_const': 0.008314
            }
temp = np.arange(20, 25.5, 0.5)
# temperature varying
def temperature_regulating(params, temp):
    """
    Input: params: initial parameters as a dictionary
    temp: temperatura array varying from 20 to 25

    returns dataframe with temperature as index
    """
    df = {}
    df['km'] = params['km_slope'] * temp + params['km_0']
    df['v_max_uptake'] = params['v_max_uptake'] * np.exp(-params['Ea_uptake']/(params['gas_const'] *(temp + 273)))
    df['km_uptake'] = params['km_uptake_slope'] * temp + params['km_uptake']
    df['cue'] = params['cue_slope'] * temp + params['cue_0']
    df = pd.DataFrame(df, index=temp)
    return df


# First step of MIC
eprod = params['r_enz_prod'] * params['initMIC']
# microbial biomass death
death = params['r_death'] * params['initMIC']
# assimilation as Michaelis-Menten function
assim = params['v_max_uptake'] * params['initMIC'] * (params['initDOC']/(params['km_uptake'] + params['initDOC']))


# at first step
# with CUE constant

d_mic = assim * df['cue'][20.5] - death - eprod

# second step
eprod = params['r_enz_prod'] * d_mic[20.5]
# microbial biomass death
death = params['r_death'] * d_mic[20.5]
# assimilation as Michaelis-Menten function
assim = params['v_max_uptake'] * d_mic[20.5] * (params['initDOC']/(params['km_uptake'] + params['initDOC']))
