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

# python PDE

from socket import SOCK_CLOEXEC
import numpy as np
import pandas as pd

# def set_time_temp(params):
#     """
#     Creating df with date and time
#     """
#     ## Creating a temperature and time range
#     time = np.arange(0, params['endtime'], params['step_time'])
#     tt = {'temp': np.linspace(20, 25, len(time)),
#           'time': time}
#     df_tt = pd.DataFrame(tt).set_index('time')
#     return df_tt

# taking just the time, we don't know how temperature varies
time = np.arange(0, params['endtime'], params['step_time'])

# modeling the parameters that are regulated by the temperature
def temperature_regulating(params, df_tt):
    """
    Input: params: initial parameters as a dictionary
    temp: temperatura array varying from 20 to 25

    returns dataframe with temperature as index
    """

    df_tt['km'] = params['km_slope'] * df_tt['temp'] + params['km_0']
    df_tt['v_max_uptake'] = params['v_max_uptake_0'] * \
        np.exp(-params['Ea_uptake']/(params['gas_const'] *(df_tt['temp'] + 273)))

    df_tt['km_uptake'] = params['km_uptake_slope'] * df_tt['temp'] + params['km_uptake_0']
    df_tt['cue'] = params['cue_slope'] * df_tt['temp'] + params['cue_0']
    df_tt['v_max'] = params['v_max_0'] * \
        np.exp(-params['Ea']/(params['gas_const'] * (df_tt['temp'] + 273)))

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


def derivatives(params, df):
    """
    Running the time derivatives
    Set the initial values and update it on every iterations.
    Save on my df
    """
    # seting mic, soc and doc to its initial parameters
    df['mic'] = params['initMIC']
    df['doc'] = params['initDOC']
    df['co2'] = 1
    # df['assim'] = 1

    for t in df.index[:-1]:
        # dMIC/dt
        assim = df.loc[t, 'v_max_uptake'] * \
            df.loc[t, 'mic'] * (df.loc[t, 'doc']/ \
                                (df.loc[t, 'km_uptake'] + df.loc[t, 'doc']))
        # assigning assim to the next time step
        # probably wont be necessary for this one
        # df.loc[t + params['step_time'], 'assim'] = assim

        # r_death and r_enz_prod are constant
        death = params['r_death'] * df.loc[t, 'mic']
        eprod = params['r_enz_prod'] * df.loc[t, 'mic']

        mic = assim * df.loc[t, 'cue'] - death - eprod
        df.loc[t + params['step_time'], 'mic'] = mic
        # MIC = assim * cue - death - eprod

        co2 = assim * (1 - df.loc[t, 'cue'])
        df.loc[t + params['step_time'], 'co2'] = co2
        # dSOC/dt
        #soc = params['inputSOC'] + death * params['MICtoSOC'] - decomp


def conventional_model(params, df):
    pass

def conventional_temp_sense(params, df):

    df['soc'] = params['initSOC']
    df['doc'] = params['initDOC']
    df['mic'] = params['initMIC']

    for t in df.index[:-1]:
        kdoc = params['kDOC_0'] * \
            np.exp(-params['Ea_DOC']/params['gas_const'] * (df.loc[t, 'temp'] + 273))
        ksoc = params['kSOC_0'] * \
            np.exp(-params['Ea_SOC']/params['gas_const'] * (df.loc[t, 'temp'] + 273))
        kmic = params['kMIC_0'] * \
            np.exp(-params['Ea_MIC']/params['gas_const'] * (df.loc[t, 'temp'] + 273))

        soc_dec = ksoc * df.loc[t, 'soc']
        doc_dec = kdoc * df.loc[t, 'doc']
        death = kmic * df.loc[t, 'mic']

        soc = (params['inputSOC'] + params['DOCtoSOC'] * \
               doc_dec + params['MICtoOC'] * params['MICtoSOC'] * death - soc_dec)
        # adding new soc to df
        df.loc[t + params['step_time'], 'soc'] = soc * params['step_time']

        doc = (params['inputDOC'] + params['SOCtoDOC'] * \
               soc_dec + params['MICtoOC'] * (1 - params['MICtoSOC']) \
                * death - params['f_uptake'] * df.loc[t, 'doc'] - doc_dec)
        # adding new doc to df
        df.loc[t + params['step_time'], 'doc'] = doc * params['step_time']

        mic = params['f_uptake'] * df.loc[t, 'doc'] - death
        # adding new mic to df
        df.loc[t + params['step_time'], 'mic'] = mic * params['step_time']
