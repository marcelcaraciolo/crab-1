#-*- coding: utf-8 -*-

import numpy as np
from numpy.testing import assert_equal
from ..dense import DenseVector
from ..categorical import OrderedSet

def test_getlabel():
    row = DenseVector([0, 1], ['A' , 'B'])
    col = DenseVector([0, 2], ['C', 'D'])
    assert_equal(row.label(0), 'A')
    assert_equal(col.label(1), 'D')

    no_labeled = DenseVector([0,1])
    assert_equal(no_labeled.label(0), 0)

def test__index():
    row = DenseVector([0, 1], ['A' , 'B'])
    col = DenseVector([0, 2], ['C', 'D'])
    
    assert_equal(row.index('A'), 0)
    assert_equal(col.index('D'), 1)

def test__entry_named():
    row = DenseVector([0, 1], ['A' , 'B'])
    col = DenseVector([0, 2], ['C', 'D'])
    
    assert_equal(row.entry_named('B'), 1)
    assert_equal(col.entry_named('D'), 2)

def test__all_labels():
    row = DenseVector([0, 1], ['A' , 'B'])
    col = DenseVector([0, 2], ['C', 'D'])
    assert_equal(row.all_labels(), [OrderedSet(['A','B'])])
    assert_equal(col.all_labels(), [OrderedSet(['C','D'])])

