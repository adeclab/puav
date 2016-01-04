# -*- coding: utf-8 -*-
from squarelaw import *
from scipy import interpolate


if __name__ == "__main__":
    vgs = 0.35

    x, ro = np.loadtxt('short_ro.csv',
        delimiter = ',',
        skiprows = 1,
        unpack = True)

    ro = ro / const.kilo

    arrow = dict(facecolor = 'black',
        arrowstyle = '->')

    fig, ax = plt.subplots()
    plt.plot( x, ro, 'r', linewidth = 2)

    ax.annotate("Tutaj tranzystor wchodzi w nasycenie\n dla $V_{DS} = V_{DSsat}$",
        xy = ( 0.135 , 35),
        textcoords = 'axes fraction', xytext = (0.3, 0.2), size = 15,
        arrowprops = arrow)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.figtext( 0.9, 0.1, r"$V_{DS}, \ V$")
    plt.figtext( 0.1, 0.91, r"$r_o, \ k \Omega$")

    ax.set_xticks( [])
    # # ax.set_xticklabels( ['$V_{GS}$'])
    ax.set_yticks( [])
    # # ax.set_yticklabels( ['$I_D$'])

    plt.show()
