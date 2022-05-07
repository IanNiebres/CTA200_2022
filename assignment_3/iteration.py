#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 12:46:24 2022

@author: ianniebres
"""

#%% Imports
import numpy as np

def iterate(z0, N, x, y):
    c = x + y*1j
    z = np.zeros(N, dtype=complex)
    z_abs = np.zeros(len(z))
    z[0] = z0
    z_abs[0] = float(z[0].real**2 +z[0].imag**2)
    
    for i in range(N-1):
        z[i+1] = z[i]**2 + c
        z_abs[i] = float(z[i].real**2 +z[i].imag**2)
        
    return z, z_abs