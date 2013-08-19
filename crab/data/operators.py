#-*- coding: utf-8 -*-

'''
Operators for linear and algebric calculations that support the Crab Matrices.
'''
import numpy as np

def multiply(v1, v2):
    '''
    Elemmentwise or scalar multiplication
    '''
    return np.multiply(v1, v2)

def dot(v1, v2):
    '''
    Matrix multiplication
    '''
    return np.dot(v1, v2)

def transpose_dot(v1, v2):
    '''
    Matrix multiplication over the transpose of V1 
    
    v1.T * v2
    '''
    return dot(v1.T, v2)





