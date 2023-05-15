"""
Creating my personalized figures in article quality
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter,MaxNLocator
import numpy as np



def paper_fig(nrows=5, ncols=3):
    mpl.rcParams['pdf.fonttype'] = 42
    mpl.rcParams['ps.fonttype'] = 42
    mpl.rcParams['font.family'] = 'Arial'

    # creating publication quality figures
    fig, axs = plt.subplots(figsize=(9, 11),
                            dpi=300,
                            nrows=nrows,
                            ncols=ncols)
                            #layout="constrained")

    # adjusting the size of the figure to fit the legend outside of plot
    plt.subplots_adjust(top=0.9, wspace = 0.7, hspace = 0.5)

    return fig, axs

def adjust_figure(fig, ax):
    """
    Adjusting the figure after plot and saving as pdf
    """
    xtick_loc = [0, 24*365*10, 24*365*20, 24*365*30]
    xtick_labels = [0, 10, 20, 30]
    
    
    for axs in fig.axes:
        # setting the same xtick labels
        axs.set_xticks(xtick_loc, labels=xtick_labels)
        axs.set_xlabel('years')


    ax[0, 0].legend(title='Base Model',
                     bbox_to_anchor=(0.7, 1.8)
                     ).get_frame().set_linewidth(0.0)
    ax[0, 1].legend(title='Enzyme Acclimation',
                     bbox_to_anchor=(0.7, 1.8)
                     ).get_frame().set_linewidth(0.0)
    ax[0, 2].legend(title='Change Input',
                     bbox_to_anchor=(0.7, 1.8)
                     ).get_frame().set_linewidth(0.0)
    

    fig.savefig('figure_example.pdf', dpi=300)
    plt.close('all')
