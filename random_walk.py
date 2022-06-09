#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:11:09 2022

@author: mozhde
"""
from random import random
import matplotlib.pyplot as plt
from numpy import array, savetxt
from copy import deepcopy


def gen_rw(n_walk):
    walk = []
    x = [0.0, 0.0, 0.0]
    for n in range(n_walk):
        for i in range(3):
            num = random()       
            if (num > 0.5): 
                x[i] += 1
            else: 
                x[i] -= 1  
        print(x)
        x1 = deepcopy(x)
        walk.append(x1) 
#        print(walk)
    return array(walk)
    

walks = gen_rw(256)
savetxt('walk.txt', walks)

plt.plot(walks[:, 0], walks[:, 1], 'p')
#plt.ylim(-4.05, -3.95)