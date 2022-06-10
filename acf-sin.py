#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 14:03:29 2022

@author: mozhde
"""

#Auto Correlation Function of Sin wave in 1D
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,10, 20)
st = np.sin(t)

def acf(signal=st, t=4, t_init = 0):
    sum = 0
    count = 0
    m = len(signal)   
    for i in range(t_init, m - t):
#        print('t0 =', i, 't1 =', i + t)
        sum += signal[i] * signal[i + t]
        count += 1
    return (sum / count)

acf_sin = []
for j in range(len(st) - 1):
    acf_sin.append(acf(t=j))
    
cst = np.cos(t)
plt.plot(acf_sin, label = 'ACF sin')
plt.plot(cst, label = 'cos')
plt.legend()