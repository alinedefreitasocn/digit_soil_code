"""
Creating my personalized figures in article quality
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter,MaxNLocator
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])
y = x**2

def paper_fig():
    mpl.rcParams['pdf.fonttype'] = 42
    mpl.rcParams['ps.fonttype'] = 42
    mpl.rcParams['font.family'] = 'Arial'

    # creating publication quality figures
    fig, axs = plt.subplots(figsize=(9, 11),
                            dpi=300,
                            nrows=5,
                            ncols=3)
                            #layout="constrained")
    # fig.tight_layout(pad=2.0)
    axs[0,0].plot(x, y, label='blah', color='k', linewidth = 0.5)
    axs[0, 0].legend(title='Base Model',
                     bbox_to_anchor=(0.7, 1.8)
                     ).get_frame().set_linewidth(0.0)
    axs[0,1].plot(x, y, label='blah', color='k', linewidth=0.5)
    axs[0, 1].legend(title='Enzyme Model',
                     bbox_to_anchor=(0.7, 1.8)
                     ).get_frame().set_linewidth(0.0)

    for ax in fig.axes:
        ax.set_xlabel('years')
    # , title_fontsize=30
    # fig, axs = plt.subplots(figsize=(10,6),
    #                        dpi=300)
    # This figure is positioned by its anchor point,
    # left bottom corner (0.1,0.1), and the size
    # parameters (0.5,0.8)
    #axs[:].tick_params(axis='both',labelsize=15)
    #plt.show()

    return fig, axs
plt.subplots_adjust(top=0.9, wspace = 0.7, hspace = 0.5)
fig.savefig('test.pdf', dpi=300)
plt.close('all')
