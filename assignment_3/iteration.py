#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 12:46:24 2022

@author: ianniebres
"""

#%% Imports
import numpy as np

def iterate(z0, N, x, y):
    """
    Function to iterate z_{n+1} = z_n^2 + c, where c = x + iy.

    Parameters
    ----------
    z0 : float
        The initial value of z.
    N : int
        Number of iterations.
    x : float
        Real part of c.
    y : float
        Imaginary part of c.

    Returns
    -------
    z : array_like (complex)
        Array holding z values at each iteration.
    z_abs : array_like (float)
        Array holding the magnitude of z at each iteration.
    it_num : int
        The iteration number at which z diverges.

    """
    c = x + y*1j
    z = np.zeros(N, dtype=complex)
    z_abs = np.zeros(N, dtype=float)
    z_abs[0] = z0.real**2 + z0.imag**2
    z[0] = z0
    
    for i in range(1, N):
        z[i] = z[i-1]**2 + c
        z_abs[i] = z[i].real**2 + z[i].imag**2
    
    it_num = 0
    
    if len(np.where(z_abs > 4)[0]) != 0:
        it_num = np.where(z_abs > 4)[0][0] # index
        
    return z, z_abs, it_num