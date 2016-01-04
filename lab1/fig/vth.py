# -*- coding: utf-8 -*-
from squarelaw import *
from scipy import interpolate


def tangent(x, y, a, p, q):
    spl = interpolate.splrep(x, y)
    small_t = np.linspace(a + p, a + q)
    fa = interpolate.splev(a, spl, der = 0)
    fp = interpolate.splev(a, spl, der = 1)
    tan = fa + fp * ( small_t - a)
    plt.plot( a, fa, 'om', small_t, tan, 'k--')
    return small_t[np.where( np.diff( np.sign(tan)))[0] + 1]

if __name__ == "__main__":
    vgs = 0.35

    x, id = np.loadtxt('id_vs_vgs.csv',
        delimiter = ',',
        skiprows = 1,
        unpack = True)

    id = id * const.mega

    arrow = dict(facecolor = 'black',
        arrowstyle = '->')

    # x = np.linspace(0, 1, 100)
    # mos = np.vectorize( drain)
    # id = mos( x, vds, w, l, kp, vth, lamb)

    fig, ax = plt.subplots()
    plt.plot( x, id, 'r', linewidth = 2)
    vth = tangent( x, id, vgs + 0.1, -0.18, 0.23)
    plt.plot( vth, 0, 'om')

    ax.annotate(r"$V_{TH} = %d \ mV$" % ( vth / const.milli),
        xy = ( vth , 0),
        textcoords = 'axes fraction', xytext = (0.1, 0.4), size = 15,
        arrowprops = arrow)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_bounds(0, 120)

    plt.figtext( 0.9, 0.15, r"$V_{GS}, \ V$")
    plt.figtext( 0.1, 0.95, r"$I_D, \ \mu A$")

    # ax.set_xticks( )
    # # ax.set_xticklabels( ['$V_{GS}$'])
    ax.set_yticks( np.linspace(0, 120, 7))
    # # ax.set_yticklabels( ['$I_D$'])

    plt.show()

    fig, ax = plt.subplots()
    spl = interpolate.splrep(x, id)
    gm = interpolate.splev(x, spl, der = 1)

    plt.plot( x, gm, 'r', linewidth = 2)
    vth = tangent( x, gm, vgs - 0.05, -0.1, 0.11)
    plt.plot( vth, 0, 'om')

    ax.annotate(r"$V_{TH} = %d \ mV$" % ( vth / const.milli),
        xy = ( vth , 0),
        textcoords = 'axes fraction', xytext = (0.5, 0.4), size = 15,
        arrowprops = arrow)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_bounds(0, 160)

    plt.figtext( 0.9, 0.1, r"$V_{GS}, \ V$")
    plt.figtext( 0.1, 0.95, r"$g_m, \ \mu A/V$")

    ax.set_yticks( np.linspace(0, 160, 6))

    plt.show()
