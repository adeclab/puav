# -*- coding: utf-8 -*-
from squarelaw import *
from scipy import interpolate

def tangent(x, y, a):
    spl = interpolate.splrep(x, y)
    small_t = np.linspace(a - 0.23, a + 0.2)
    fa = interpolate.splev(a, spl, der = 0)
    fp = interpolate.splev(a, spl, der = 1)
    tan = fa + fp * ( small_t - a)
    plt.plot( a, fa, 'om', small_t, tan, 'k--')


if __name__ == "__main__":
    w    = 10
    l    = 2
    kp   = 100 * const.micro
    vth  = 0.3
    lamb = 0.05
    vds  = 0.5

    arrow = dict(facecolor = 'black',
        arrowstyle = '<-')

    x = np.linspace(0, 1, 100)
    mos = np.vectorize( drain)
    id = mos( x, vds, w, l, kp, vth, lamb)

    fig, ax = plt.subplots()
    plt.plot( x, id, 'r', linewidth = 2)
    tangent( x, id, vth + 0.2 )

    ax.annotate(r"$nachylenie = g_m = \frac{\delta I_D}{\delta V_{GS}}$",
        xy = ( vth + 0.2, drain( vth + 0.2, vds, w, l, kp, vth, lamb)),
        textcoords = 'axes fraction', xytext = (0.1, 0.4), size = 15,
        arrowprops = arrow)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_bounds(0, 1.05 * max(id))

    plt.figtext( 0.9, 0.19, '$v_{GS}$')
    plt.figtext( 0.1, 0.9, '$i_D$')

    ax.set_xticks( [vth + 0.2])
    ax.set_xticklabels( ['$V_{GS}$'])
    ax.set_yticks( [drain( vth + 0.2, vds, w, l, kp, vth, lamb)])
    ax.set_yticklabels( ['$I_D$'])

    plt.show()
