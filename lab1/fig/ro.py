# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy             as np
import scipy.constants   as const
import matplotlib.pyplot as plt
from scipy import interpolate


def sat( vgs, vds, w, l, kp, vth, lamb):
    vdsat = vgs - vth
    return ( ( kp / 2) * ( w / l) * (vgs - vth) ** 2) * \
        ( 1 + lamb * ( vds - vdsat))


def triode( vgs, vds, w, l, kp, vth, lamb):
    return kp * w / l * ( ( vgs - vth) * vds - vds ** 2 / 2)


def drain( vgs, vds, w, l, kp, vth, lamb):
    if vgs > vth:
        if vds < vgs - vth:
            return triode( vgs, vds, w, l, kp, vth, lamb)
        else:
            return sat( vgs, vds, w, l, kp, vth, lamb)
    else:
        return 0.0


def drain_sat( vds, w, l, kp):
    return ( kp / 2) * ( w / l) * vds ** 2


def tangent(x, y, a, p, q):
    spl = interpolate.splrep(x, y)
    small_t = np.linspace(a + p, a + q)
    fa = interpolate.splev(a, spl, der = 0)
    fp = interpolate.splev(a, spl, der = 1)
    tan = fa + fp * ( small_t - a)
    plt.plot( a, fa, 'om', small_t, tan, 'k--')
    return small_t[np.where( np.diff( np.sign(tan)))[0] + 1]

if __name__ == "__main__":
    w    = 10
    l    = 2
    kp   = 100 * const.micro
    vth  = 0.3
    lamb = 0.15
    vgs  = 0.5

    arrow = dict(facecolor = 'black',
        arrowstyle = '->')

    x = np.linspace(0, 1, 100)
    mos = np.vectorize( drain)
    id = mos( vgs, x, w, l, kp, vth, lamb)

    fig, ax = plt.subplots()
    plt.plot( x, id, 'r', linewidth = 2)

    vds = vgs - 0.9 * vth
    ids = mos( vgs, vds, w, l, kp, vth, lamb)
    x2 = np.linspace( vds - 0.1, vds + 0.5)
    tangent( x, id, vds, -0.1, 0.5)
    plt.plot( x2, ids * np.ones(x2.size), 'k--')
    point = 0.75 * ( vgs - vth)
    ax.annotate('Odwrotność nachylenia\n jest wartością rezystancji wyjściowej',
        xy = ( vds, ids),
        textcoords = 'axes fraction', xytext = (0.35, 0.25), size = 15,
        arrowprops = arrow)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.set_xticks([vds])
    ax.set_xticklabels(['$V_{DS}$'])
    ax.set_yticks([ids])
    ax.set_yticklabels(['$I_{D}$'])

    plt.figtext( 0.9, 0.1, '$v_{DS}$')
    plt.figtext( 0.1, 0.9, '$i_D$')

    plt.show()
