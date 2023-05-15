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

#from socket import SOCK_CLOEXEC
import numpy as np
import pandas as pd


def soil_warming(params, temp=25):
    """
    Running the time derivatives
    Set the initial values and update it on every iterations.
    Save as df for better visualization and plot. Export as csv
    """
    
    # generating the time slice
    time = np.arange(0, params['endtime'], params['step_time'])

    # seting mic, soc and doc to its initial parameters
    mic = params['initMIC']
    doc = params['initDOC']
    soc = params['initSOC']
    enz = params['initEnz']
    co2 = 1

    # creating empty lists to save the new value on each
    # time step
    mic_hist = [mic]
    doc_hist = [doc]
    soc_hist = [soc]
    co2_hist = [co2]
    enz_hist = [enz]

    # The temperature sensitivity of decomposition is modelled in 
    # the same way as uptake, with temperature dependency built 
    # into the extracellular enzyme parameters
    v_max = params['v_max_0'] * \
        np.exp(-params['Ea']/(params['gas_const'] * (temp + 273)))
    
    # calculating the temperature sensitive parameters
    # km values are calculated as a linear function of 
    # temperature between 0 and 50ºC
    km = params['km_slope'] * temp + params['km_0']

    # The model calculates a temperature-specific v_max
    # using the Arrhenius equation, where v_max_uptake_0
    # is the pre-exponential coefficient, gas_const is 
    # the ideal gas constant, and Ea is the activation energy, 
    # or the amount of energy required to convert substrate into product:
    v_max_uptake = params['v_max_uptake_0'] * \
        np.exp(-params['Ea_uptake']/(params['gas_const'] *(temp + 273)))

    km_uptake = params['km_uptake_slope'] * temp + params['km_uptake_0']

    # CUE is also a linear function of temperature
    cue = params['cue_slope'] * temp + params['cue_0']


    # calculating variation for each step time
    # starting from time 1 because time zero is
    # already defined
    for t in time[1:]:
        # assimilation as a Michaelis-Menten function sclaed
        # to the size of microbial biomass pool
        assim = v_max_uptake * \
            mic * (doc/(km_uptake + doc))

        # r_death and r_enz_prod are constant and time
        # dependent
        # Microbial biomass death is modeled as a first-order 
        # process with a rate constant r_death
        death = params['r_death'] * mic
        
        # Enzyme production is modelled as a constant fraction 
        # (r_enz_prod) of microbial biomass
        # r enz prod is time dependent
        eprod = params['r_enz_prod'] * mic

        # r_enz_loss is constant
        # enzyme turnover is modelled as a first-order 
        # process with a rate constant
        eloss = params['r_enz_loss'] * enz

        # The enzyme pool increases with enzyme production and 
        # decreases with enzyme turnover
        enz = eprod - eloss
        enz_hist.append(enz)

        # decomposition of SOC is catalysed according to 
        # Michaelis-Menten kinetics by the enzyme pool
        decomp = v_max * enz * (soc/(km + soc))

        # calculating the new values for mic, soc, doc, co2
        # new value for mic
        # Microbial biomass changes by the amount of DOC assimilated, 
        # times the carbon use (or microbial growth) efficiency, 
        # minus biomass death and enzyme production
        mic = assim * cue - death - eprod
        # saving to the serie of values
        mic_hist.append(mic)

        # calculating co2 and saving to the serie of values
        # CO2 production is the fraction of DOC assimilated 
        # by microbes that is not allocated to biomass production
        co2 = assim * (1 - cue)
        co2_hist.append(co2)

        # soc/dt
        # The SOC pool increases with external inputs and a fraction of 
        # dead microbial biomass (mictosoc) and decreases due to 
        # decomposition losses
        soc = soc + death * params['MICtoSOC'] - decomp
        soc_hist.append(soc)

        # doc/dt
        # The DOC pool receives external inputs, the remaining fraction 
        # of dead microbial biomass, the decomposition flux, 
        # and dead enzymes, while assimilation of DOC by microbial 
        # biomass is subtracted
        doc = params['inputDOC'] + death * \
            (1 - params['MICtoSOC']) + decomp + eloss - assim
        doc_hist.append(doc)

    dict = {'doc': doc_hist,
            'soc': soc_hist,
            'co2': co2_hist,
            'mic': mic_hist,
            'enz': enz_hist}
    df = pd.DataFrame(dict, index=time)
    return df
