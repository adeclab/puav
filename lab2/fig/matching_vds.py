# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy             as np
import scipy.constants   as const
import matplotlib.pyplot as plt


def sat( vgs, vds, w, l, kp, vth, lamb):
    vdsat = vgs - vth
    return ( ( kp / 2) * ( w / l) * (vgs - vth) ** 2) * \
        ( 1 + lamb * ( vds - vdsat))


def triode( vgs, vds, w, l, kp, vth, lamb):
    return kp * w / l * ( ( vgs - vth) * vds - ( ( vds ** 2) / 2))


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

if __name__ == "__main__":
    w    = 10
    l    = 2
    kp   = 100 * const.micro
    vth  = 0.3
    lamb = 0.1
    vgs  = 0.7

    arrow = dict(facecolor = 'black',
        arrowstyle = '->')

    x = np.linspace(0, 1, 100)
    x2 = np.linspace(0, vgs - vth + 0.01)
    mos = np.vectorize( drain)
    id = mos( vgs, x, w, l, kp, vth, lamb)
    iref = mos( vgs, vgs - vth + 0.01, w, l, kp, vth, lamb)

    fig, ax = plt.subplots()
    plt.plot( x, id, 'r', linewidth = 2)
    plt.axhline( iref, linewidth = 2)

    point = 0.75 * ( vgs - vth)
    ax.annotate('$I_{REF}$ = $I_O$',
        xy = ( vgs - vth, drain( vgs, vgs - vth, w, l, kp, vth, lamb)),
        textcoords = 'axes fraction', xytext = (0.1, 0.9), size = 15,
        arrowprops = arrow)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.set_xticks([])
    ax.set_yticks([])

    plt.xlabel('Napięcie dren - źródło')
    plt.ylabel('Prąd drenu')
    plt.show()
