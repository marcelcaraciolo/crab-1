#-*-coding: utf-8 -*-

import numpy as np

"""
Base class(es) for all data structure objects.
"""

class NDenseArray(object):

    """
    The N-dimensional dense representations that Crab inherit from.
    """
    @property
    def _constructor(self):
        """class constructor (for this class it's just  `__class__`"""
        return self.__class__


class NSparseArray(object):
    """
    The N-dimensional sparse representations that Crab inherit from.
    """

    def __init__(self, *args, **kwargs):
        raise NotImplementedError('NSparseArray is an abstract class')

 
class DenseArray(NDenseArray, np.ndarray):

    '''
    The crab implementation for dense arrays.
    Inherits from np.ndarray
    '''
    
    def __new__(cls, input_array, *args, **kwargs):
        raise NotImplemented('DenseArray is an abstract class')

    def __getitem__(self, indices):
        data = np.ndarray.__getitem__(self, indices)
        return data

    def multiply(self, other):
        """
        Element-wise multiplication.
        """
        from operators import multiply as safe_multiply
        return safe_multiply(self, other)

    def dot(self, other):
        """
        Matrix or scalar multiplication.
        """
        from operators import dot as safe_dot
        return safe_dot(self, other)
    
    def transpose_dot(self, other):
        """
        Multiply this matrix *transposed* by another matrix. This can save
        a lot of computation when multiplying two sparse matrices.
        """
        from  operators import transpose_dot
        return transpose_dot(self, other)

    def to_dense(self):
        return self

    def to_pickle(self, path):
        '''
        Pickle (serialize) object to imput file path
        
       Parameters
        ----------
        path :  string
            File Path
        '''
        raise NotImplementedError("You need to implement this class for your custom implementation.")
 

