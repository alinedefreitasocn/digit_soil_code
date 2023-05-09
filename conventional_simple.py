import numpy as np
import pandas as pd

params = {
                'endtime': 262800,
                'step_time': 8760,
                'temp': 20,
                'initSOC': 111.121,
                'initDOC': 0.521927,
                'initMIC': 2.20661,
                'inputSOC': 0.0005,
                'inputDOC': 0.0005,
                'f_uptake': 0.0005,
                'k_doc_0': 10000,
                'k_soc_0': 1300,
                'k_mic_0': 1600,
                'Ea_soc': 47,
                'Ea_mic': 40,
                'Ea_doc': 40,
                'Ea_uptake': 47,
                'DOCtoSOC': 0.2,
                'SOCtoDOC': 0.2,
                'MICtoOC': 0.2,
                'MICtoSOC': 0.5,
                'gas_const': 0.008314
            }

time = np.arange(0, 262800, 8760)
temp = np.linspace(20, 25, len(time))

df = pd.DataFrame(data=temp, index=time, columns=['temp'])

# kdoc varies with temperature
df['kDOC'] = params['k_doc_0'] * \
    np.exp(-(params['Ea_doc'])/(params['gas_const']*(df['temp'] + 273)))

df['kSOC'] = params['k_soc_0'] * \
    np.exp(-((params['Ea_soc'])/(params['gas_const']*(df['temp']+273))))

df['kMIC'] = params['k_mic_0'] * \
    np.exp(-params['Ea_mic']/params['gas_const']*(df['temp'] + 273))


DOC_decomp = df['kDOC'] * doc
# running with init value
DOC_decomp = df['kDOC'] * params['initDOC']

death = k_mic * mic
SOC_decomp = df['kSOC'] * soc
# running with init value
SOC_decomp = df['kSOC'] * params['initSOC']

dSOC = params['inputSOC'] + params['DOCtoSOC'] * DOC_decomp + \
    params['MICtoOC'] * params['MICtoSOC'] * death - SOC_decomp
