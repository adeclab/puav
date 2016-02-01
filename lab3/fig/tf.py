# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import scipy.signal as sig
import scipy.constants as const
import matplotlib.pyplot as plt

Adc = 1000.0
fp1 = 10.0 * const.kilo
fun = Adc * fp1
fz  = 100000 * const.kilo
fp2 = 1000000 * const.kilo

wp1 = 2 * const.pi * fp1
wp2 = 2 * const.pi * fp2
wz  = 2 * const.pi * fz
num = [Adc * -1.0/wz, Adc * 1.0]
den = [1.0/(wp1 * wp2), (wp1 + wp2)/(wp1 * wp2), 1]

if __name__ == "__main__":
    tf = sig.lti(num, den)
    w = np.logspace(3, 10)
    a, mag, phase = tf.bode(w=2*const.pi*w)

    fig, (ax1, ax2) = plt.subplots(nrows=2)
    ax1.semilogx(w, mag)
    ax1.set_ylabel('Wzmocnienie [dB]')
    ax1.set_yticks([60, 0])
    ax2.semilogx(w,
            np.rad2deg(np.unwrap(np.deg2rad(phase))))
    ax2.set_yticks([0, -45, -90, -180])
    ax2.set_ylabel('Faza [$^{\circ}$]')
    ax2.set_xlabel('Częstotliwość [Hz]')
    ax1.axvline(fp1, color='r')
    ax1.axvline(fz, color='r')
    ax1.axvline(fun, color='r')
    ax1.axvline(fp2, color='r')
    ax2.axvline(fp1, color='r')
    ax2.axvline(fz, color='r')
    ax2.axvline(fun, color='r')
    ax2.axvline(fp2, color='r')
    plt.show()
