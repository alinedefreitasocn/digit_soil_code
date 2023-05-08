# creating a dictionary with the initial
# values for spinup model
spinup_enzyme = {
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

# dictionary with the spinup values for the
# conventional model
spinup_conventional = {
                    'endtime': 10000000,
                    'interval': 100000,
                    'temp_init': 20,
                    'initSOC': 100,
                    'initDOC': 0.5,
                    'initMIC': 0.5,
                    'initEnz': 0.01,
                    'inputSOC': 0.0005,
                    'inputDOC': 0.0005,
                    'f_uptake': 0.0005,
                    'kDOC_0': 10000,
                    'kSOC_0': 1300,
                    'kMIC_0': 1600,
                    'Ea_DOC': 40,
                    'Ea_SOC': 47,
                    'Ea_MIC': 40,
                    'DOCtoSOC': 0.2,
                    'SOCtoDOC': 0.2,
                    'MICtoOC': 0.2,
                    'MICtoSOC': 0.5,
                    'gas_const': 0.008314
                    }

