#-*- coding: utf-8 -*-

import numpy as np
from numpy.testing import assert_equal, assert_almost_equal
from nose.tools import assert_raises
from ..dense import DenseVector
from ..dense import DenseMatrix

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

def test_dense_matrix():
    matrix_1 = DenseMatrix([[0, 1], [2, 3]], ['A', 'B'], ['C', 'D'])
 
    row_0 = DenseVector([0, 1], ['C', 'D'])
    col_0 = DenseVector([0, 2], ['A', 'B'])
    assert_equal(matrix_1[0], row_0)
    assert_equal(matrix_1[0,:],row_0)
    assert_equal(matrix_1[:,0],col_0)
    assert_equal(matrix_1.get_row(0), row_0)
    assert_equal(matrix_1.get_col(0),col_0)


def test_dense_matrix_label_lookups():

    matrix_1 = DenseMatrix([[0, 1], [2, 3]], ['A', 'B'], ['C', 'D'])
    matrix_2 = DenseMatrix([[0, 1], [2, 3]], ['A', 'B'], None)

    assert np.all(matrix_1.row_named('A') == matrix_1[0])
    assert np.all(matrix_1.col_named('D') == matrix_1[:, 1])
    assert np.all(matrix_2.row_named('A') == matrix_2[0])
    assert np.all(matrix_2.col_named(1) == matrix_2[:, 1])
    assert matrix_1.entry_named('B', 'C') == matrix_1[1, 0]
    assert matrix_2.entry_named('B', 0) == matrix_2[1, 0]

def test_dense_matrix_to_array():
    matrix_1 = DenseMatrix([[0, 1], [2, 3]], ['A', 'B'], ['C', 'D'])
    assert np.all(matrix_1.to_array() == np.array([[0,1],[2,3]]))

