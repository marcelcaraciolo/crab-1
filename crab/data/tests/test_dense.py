#-*- coding: utf-8 -*-

import numpy as np
from numpy.testing import assert_equal, assert_almost_equal
from nose.tools import assert_raises
from ..dense import DenseVector

def test_dense_vector():
    row = DenseVector([0, 1], ['A' , 'B'])
    col = DenseVector([0, 2], ['C', 'D'])
    assert_equal(row, np.array([0,1]))
    assert_equal(col, np.array([0,2]))

    #representation assertive
    assert_equal(repr(row), 'DenseVector(length 2, [A => 0,B => 1])')
    assert_equal(repr(col), 'DenseVector(length 2, [C => 0,D => 2])')

    #without labels
    row = DenseVector([0, 1])
    assert_equal(repr(row), 'DenseVector(length 2, [0 1])')

    #more than 10 items
    row = DenseVector(range(11), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' , 'k', 'l'])
    assert_equal(repr(row), 'DenseVector(length 11, [a => 0,b => 1,c => 2,d => 3,e => 4,f =>' + \
            ' 5,g => 6,h => 7,i => 8,k => 9,...,l => 10])')

    #TEST LEN(LABELS) == LEN(ARRAY)
    assert_raises(AssertionError, DenseVector,[2,3,4], ['A','B'])


def test_dense_vector_operators():
    #operators
    col = DenseVector([1, 2], ['C', 'D'])
    assert_equal(col.dot(col), 5)

    assert_equal(col.dot(4), DenseVector([4,8], ['C', 'D']))
    assert_equal(4 * col, DenseVector([4,8], ['C', 'D']))

    assert_equal(col.multiply(col), DenseVector([1,4], ['C', 'D']))

    assert_almost_equal(col.normalize(), DenseVector([0.4472136, 0.89442719], ['C', 'D']))

    assert_equal(col.transpose_dot(col), 5)
