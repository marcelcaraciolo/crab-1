#-*- coding: utf-8 -*-

import numpy as np
from numpy.testing import assert_equal
from ..dense import DenseVector

def test_dense_vector():
    row = DenseVector([0, 1], ['A' , 'B'])
    col = DenseVector([0, 2], ['C', 'D'])
    assert_equal(row, np.array([0,1]))
    assert_equal(col, np.array([0,2]))

    #representation assertive
    assert_equal(repr(row), 'DenseVector(length 2, [0 1])')
    assert_equal(repr(col), 'DenseVector(length 2, [0 2])')

