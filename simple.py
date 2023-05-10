
import numpy as np
import pandas as pd

params = {
                'endtime': 262800,
                'step_time': 8760,
                'temp_init': 20,
                'initSOC': 111.876,
                'initDOC': 0.00144928,
                'initMIC': 2.19159,
                'initEnz': 0.0109579,
                'inputSOC': 0.0005,
                'inputDOC': 0.0005,
                'r_death': 0.0002,
                'r_enz_prod': 0.000005,
                'r_enz_loss': 0.001,
                'MICtoSOC': 0.5,
                'cue_0': 0.63,
                'cue_slope': -0.016,
                'v_max_0': 100000000,
                'v_max_uptake_0': 100000000,
                'km_0': 500,
                'km_uptake_0': 0.1,
                'km_slope': 5,
                'km_uptake_slope': 0.01,
                'Ea': 47,
                'Ea_uptake': 47,
                'gas_const': 0.008314
            }
temp = np.linspace(0, 100, 1000)
# temperature varying
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

## Secondary parameters dependent on temperature
# v_max_uptake should vary with temperature as well as
# km_uptake
# df['v_max_uptake'] and df['km_uptake'] are df with temp as index
df['assim'] = (df['v_max_uptake'] * params['initMIC']) * \
    (params['initDOC']/(df['km_uptake'] + params['initDOC']))

df['co2'] = df['assim'] * (1- df['cue'])

decomp = params['v_max'] *
df['dSOC'] = params['inputSOC'] + death * params['MICtoSOC'] - decomp

# First step of MIC
eprod = params['r_enz_prod'] * params['initMIC']
# microbial biomass death
death = params['r_death'] * params['initMIC']
# assimilation as Michaelis-Menten function


# at first step
# with CUE constant
# d_mic should be the variation of mic with time
d_mic = assim * df['cue'] - death - eprod
