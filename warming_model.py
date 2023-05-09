"""
Based on Allison et al, 2010 create a warming soil model

Create dt as range from 0 to 30 years (in hours)

The model starts by setting the soil organic carbon (SOC),
dissolved organic carbon (DOC), microbial biomass, and enzyme pools
to their initial values. Microbial biomass changes
by the amount of DOC assimilated, times the carbon use
(or microbial growth) efficiency, minus
biomass death and enzyme production
"""
from distutils.cygwinccompiler import Mingw32CCompiler
import numpy as np
import pandas as pd
# importing fuction to create hight quality figtures
from myfigures import paper_fig
# importing initial parameters
import running_spinup

# start by creating a class Soil to run the model
class EnzymeModel:
    def __init__(self):
        self.init_params = running_spinup.init_params()
    
    def dynamics(self):
        """
        input is self parameters and index?? So everytime it changes
        """
        # enzyme production
        self.eprod = r_enz_prod * mic
        # microbial biomass death
        self.death = r_death * mic
        # assimilation as Michaelis-Menten function
        self.assim = v_max_uptake * mic * (doc/(km_uptake + doc))
        pass

    def d_mic(self):
        """
        should count the variation of mic with time
        """
        # microbial biomass change
        d_mic = assim * cue - death - eprod
        pass

    def MME(self):
        """
        Michaelis-Menten equation
        Vmax represents the maximum velocity achieved by the system,
        at maximum (saturating) substrate concentrations.
        KM (the Michaelis constant;) is the substrate concentration
        at which the reaction velocity is 50% of the Vmax.
        You need to fit into data??
        how we can fit this kind of model to experimental data
        in Python using some staightforward optimization
        https://gilgi.org/blog/biochemical-kinetics-reaction-velocities/

        for the enzime acts on the substrate the substrate get converted into
        product and product if finally release.
        With time, the concentration of substract decrise and
        the product increase.
        the slope of the graph gives the velocity of reaction.
        the velocity increase linear at the beginning of the graph (1st order
        reaction) then reaches a plateu (the increase in substract
        concentration no longer increase the velocity of reaction)
        The Michaelis constant is used to represent both the 1st order reaction
        and the plateu velocities of reaction.
        """
        def rate(s, v_max, k_m):
            """
            Return the reaction rate (v) as a function of
            substrate concentration (s).
            """
            return (v_max * s) / (k_m + s)


    def get_assimilation(self):
        """
        assimilation is a Michaelis-Menten function scaled to
        the size of the microbial biomass
        the cell surface area available for uptake will be
        directly proportional to the number of cells. Microbes
        may not assimilate more DOC than is available in the DOC pool.
        """
        assim = v_max_uptake * mic * (doc/(k_m + doc))
        return assim

    def warming_soil(self):
        """
        Returns CO2 efflux, SOC, DOC, Biomass and Enzyme
        projections for the range of 0 to 30 years (in h)
        """
        mic = (assim * cue) - death - eprod
        pass

class conventional_model():
    def __init__(self, init_param):
        """
        Initial paramentes as dictionary or DataFrame
        """
        self.params = init_param
        self.temp = np.linspace(0, 25, 100)

    def dynamics(self):
        """
        returns the value of kDOC along temperature variation
        as a df with temperature and kdoc related to temp
        """
        df = pd.DataFrame({'temp': self.temp})
        # the gas denominator will be the same for the
        # 3 equations
        gas = self.params['gas_const']*(df['temp'] + 273)

        df['kdoc'] = self.params['kDOC_0'] * \
            np.exp(-self.params['Ea_DOC']/gas)

        df['kSOC'] = self.params['kSOC_0'] * \
            np.exp(-self.params['Ea_SOC']/gas)

        df['kMIC'] = self.params['kMIC_0'] * \
            np.exp(-self.params['Ea_MIC']/gas)

        # dSOC/dt

        self.dynamics = df
        return df
    
    def cue_decay(self):
        cue = 0.63 - 0.016*(self.temp + 273)