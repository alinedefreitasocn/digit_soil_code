import warming_model
from warming_model import soil_model
from warming_model import myfigures

# setting initial parameters
params = warming_model.params_enzyme_default

# running equations
df = soil_model.soil_warming(params)

# creating figures
fig, axs = myfigures.paper_fig()
df.soc.plot(ax=axs[0,0], style='k--', label='test')
axs[0,0].set_ylabel('SOC (mg $g^{-1}$)')

# dummy plot
df.soc.plot(ax=axs[0,1], style='k--', label='test 2')
axs[0,1].set_ylabel('SOC (mg $g^{-1}$)')
df.soc.plot(ax=axs[0,2], style='k--', label='test 3')
axs[0,2].set_ylabel('SOC (mg $g^{-1}$)')

# doc
df.doc.plot(ax=axs[1, 0], style='k-', label='DOC')
axs[1,0].set_ylabel('DOC ($\mu$ g $g^{-1}$)')
# dummy
df.doc.plot(ax=axs[1, 1], style='k-', label='DOC')
axs[1,1].set_ylabel('DOC ($\mu$ g $g^{-1}$)')
df.doc.plot(ax=axs[1, 2], style='k-', label='DOC')
axs[1,2].set_ylabel('DOC ($\mu$ g $g^{-1}$)')

# co2
df.co2.plot(ax=axs[2, 0], style='k-', label='$CO^{2}$')
axs[2,0].set_ylabel('$CO^{2}$ efflux ($\mu$g $g^{-1}$ $h^{-1}$)')
df.doc.plot(ax=axs[2, 1], style='k-', label='$CO^{2}$')
axs[2,1].set_ylabel('$CO^{2}$ efflux ($\mu$g $g^{-1}$ $h^{-1}$)')
df.doc.plot(ax=axs[2, 2], style='k-', label='$CO^{2}$')
axs[2,2].set_ylabel('$CO^{2}$ efflux ($\mu$g $g^{-1}$ $h^{-1}$)')

# mic
df.mic.plot(ax=axs[3, 0], style='k-', label='Biomass')
axs[3,0].set_ylabel('Biomass (mg $g^{-1}$)')
df.mic.plot(ax=axs[3, 1], style='k-', label='Biomass')
axs[3,1].set_ylabel('Biomass (mg $g^{-1}$)')
df.mic.plot(ax=axs[3, 2], style='k-', label='Biomass')
axs[3,2].set_ylabel('Biomass (mg $g^{-1}$)')

# enz
df.enz.plot(ax=axs[4, 0], style='k-', label='Enzymes')
axs[4,0].set_ylabel('Enzyme ($\mu$g $g^{-1}$)')
df.enz.plot(ax=axs[4, 1], style='k-', label='Enzymes')
axs[4,1].set_ylabel('Enzyme ($\mu$g $g^{-1}$)')
df.enz.plot(ax=axs[4, 2], style='k-', label='Enzymes')
axs[4,2].set_ylabel('Enzyme ($\mu$g $g^{-1}$)')

myfigures.adjust_figure(fig, axs)

df.to_csv('warming_soil_output.csv')