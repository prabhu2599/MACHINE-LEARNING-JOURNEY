#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:31:33 2020

@author: prabhugantayat
"""
import numpy as np
import pandas as pd

if(np):
    print("1- Numpy imported")
    
print("2-",np.version.version)

nullVector = np.zeros(10)
print("3-",nullVector)

print("4-",nullVector.nbytes)

#df1 = str(help(np.add))
print("5- help(np.add)")

nullVector[4] = 1
print("6- ",nullVector)

fromVector = np.arange(10,49,3)
print("7- ",fromVector)

reverseVector = np.flip(fromVector)
print("8- ",reverseVector)

dimVector = np.ones((3, 3)) * abs(np.random.randn(3,3)*10)
print("9- ",dimVector)

inputArr1 = np.array([1,2,0,0,4,0])
arrNonZeroIndex = np.nonzero(inputArr1)
print("10- ",inputArr1[arrNonZeroIndex])
