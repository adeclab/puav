import squarelaw as mos
import numpy as np
import scipy.constants as const
import matplotlib.pyplot as plt

def idrain(current, Vdi, beta):
    return np.power( Vdi / np.sqrt( 2 / beta) + np.sqrt(current), 2)

if __name__ == "__main__":
    w     = 10
    l     = 2
    kp    = 100 * const.micro
    vth   = 0.3
    lamb  = 0.1
    vgs   = 2.5
    vds   = 1.5
    vdsat = vgs - vth


    x = np.linspace(0, 150, 1000)
    cur = np.vectorize( mos.drain)
    iD1 = mos.drain( vgs, 1.5, w, l, kp, vth, lamb)
    iD2 = idrain(iD1, x, w * kp / l / 2)

    fig, ax = plt.subplots()
    plt.plot( x, iD2, 'r', linewidth = 2)
    plt.show()
