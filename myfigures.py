"""
Creating my personalized figures in article quality
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter,MaxNLocator

def paper_fig():
    mpl.rcParams['pdf.fonttype'] = 42
    mpl.rcParams['ps.fonttype'] = 42
    mpl.rcParams['font.family'] = 'Arial'

    # creating publication quality figures
    fig, axs = plt.subplots(figsize=(9, 11),
                            dpi=300, 
                            nrows=5, 
                            ncols=3)
    fig.tight_layout(pad=2.0)
    axs[0, 0].legend(title='Base Model', title_fontsize=30, bbox_to_anchor=(0.65, 1.25))
    # fig, axs = plt.subplots(figsize=(10,6), 
    #                        dpi=300)
    # This figure is positioned by its anchor point, 
    # left bottom corner (0.1,0.1), and the size 
    # parameters (0.5,0.8)
    #axs[:].tick_params(axis='both',labelsize=15)
    #plt.show()
    fig.savefig('test.pdf', dpi=300)
    return fig, axs


